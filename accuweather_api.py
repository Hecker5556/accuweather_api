import aiohttp, asyncio, json, os, re
from aiohttp_socks import ProxyConnector
from yarl import URL
from html import unescape
from typing import Literal
class accuweather_api:
    def __init__(self, cache_file_name: str = "cache.json"):
        self.cache = cache_file_name
        self.unit = None
        self.darkmap = None
        self.proxy = None
    def _make_connector(self, proxy: str = None):
        return ProxyConnector.from_url(proxy) if proxy and proxy.startswith("socks5") else aiohttp.TCPConnector()
    async def _search(self, query: str):
        url = "https://www.accuweather.com/web-api/autocomplete"
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.8',
            'Cookie': f"awx_user=tp:{self.unit}",
            'priority': 'u=1, i',
            'referer': 'https://www.accuweather.com/',
            'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
        if os.path.exists(self.cache):
            with open(self.cache, "r") as f1:
                try:
                    cache = json.load(f1)
                except:
                    cache = {}
        else:
            cache = {}
        if not (key := cache.get(query)):
            async with self.session.get(URL(f"{url}?query={query}", encoded=False), proxy=self.proxy, headers=self.headers) as r:
                print(r.url)
                autocompletes = await r.json(encoding="utf-8")
            if autocompletes:
                key = autocompletes[0].get("key")
                with open(self.cache, "w") as f1:
                    cache[query] = key
                    json.dump(cache, f1)
            else:
                async with self.session.get(URL(f'https://www.accuweather.com/en/search-locations?query={query}', encoded=True), proxy=self.proxy, headers=self.headers, allow_redirects=False) as r:
                    key = re.search(r"key=(.*?)&", r.headers.get("location")).group(1)
                with open(self.cache, "w") as f1:
                    cache[query] = key
                    json.dump(cache, f1)  
        else:
            print('found key in cache')
        url = 'https://www.accuweather.com/web-api/three-day-redirect'
        async with self.session.get(URL(f"{url}?key={key}",encoded=True), proxy=self.proxy, headers=self.headers,) as r:
            response = await r.text("utf-8")    
        self.info = {}
        bigmappattern = r"https://api\.accuweather\.com/maps/v1/radar/static/(?:.*?)base_data=radar"
        bigmap = unescape(re.search(bigmappattern, response).group(0))
        self.info['clouds_map'] = bigmap
        if self.darkmap:
            self.info['clouds_map'] += "&theme=dark"
        futurespattern = r"<a class=\"daily-list-item (?:has-alerts)?\" href=\"(.*?)\">([\s\S]*?)</a>"
        futureweathers = re.findall(futurespattern, response)
        daypattern = re.compile(r"<p class=\"day\">(.*?)</p>")
        datepattern = re.compile(r"<p>(.*?)</p>")
        weatherimagepattern = re.compile(r"<img class=\"icon\"(?:.*?)src=\"(.*?)\" />")
        temphipattern = re.compile(r"<span class=\"temp-hi\">(.*?)</span>")
        templopattern = re.compile(r"<span class=\"temp-lo\">(.*?)</span>")
        weatherdescpattern = re.compile(r"<p class=\"no-wrap\">(.*?)</p>")
        percippattern = re.compile(r"</svg>(?:[\s\S].*?)(\d*?)%")
        forecast = {}
        index = 0
        for url, weather in futureweathers:
            whichday = re.search(daypattern, weather).group(1)
            whichdate = re.search(datepattern, weather).group(1)
            weatherimage = re.search(weatherimagepattern, weather).group(1)
            temphi = unescape(re.search(temphipattern, weather).group(1))
            templow = unescape(re.search(templopattern, weather).group(1))
            weatherdesc = re.findall(weatherdescpattern, weather)
            precip = re.search(percippattern, weather).group(1)
            temp = {}
            temp["day"] = whichday
            temp["date"] = whichdate
            temp["image"] = weatherimage
            temp["url"] = f"https://www.accuweather.com{url}"
            temp["temp-hi"] = temphi + self.unit
            temp["temp-lo"] = templow + self.unit
            if len(weatherdesc) > 1:
                temp['weather_day'] = weatherdesc[0]
                temp['weather_night'] = weatherdesc[1]
            else:
                temp['weather'] = weatherdesc[0]
            temp['precipitation'] = f"{precip}%"
            forecast[f"day-{index}"] = temp
            index += 1
        self.info['forecast'] = forecast
        extrainfopattern = r"<div class=\"spaced-content detail\">([\s\S]*?)</div>"
        labelpattern = r"<span class=\"label\">(.*?)</span>"
        valuepattern = r"<span class=\"value\"(?: style=\"color: (?:.*?)\")?>(.*?)</span>"
        if extrainfo := re.findall(extrainfopattern, response):
            for detail in extrainfo:
                self.info[unescape(re.search(labelpattern, detail).group(1))] = unescape(re.search(valuepattern, detail).group(1))
                if self.info[unescape(re.search(labelpattern, detail).group(1))].endswith("°"):
                    self.info[unescape(re.search(labelpattern, detail).group(1))] += self.unit
        if breadcrumbs := re.search(r"<div class=\"crumbs\">([\s\S]*?)</div>", response):
            breadcrumbs = breadcrumbs[0]
            breadcrumbs = re.findall(r"<a href=\"(?:.*?)\" class=\"(?:.*?)\">(.*?)</a>", breadcrumbs)
            self.info['location'] = ">".join(map(lambda x: unescape(x), breadcrumbs))
        await self._extract_extra(self.info['forecast']['day-0']['url'])
        print(json.dumps(self.info, ensure_ascii=False, indent=4))
        return self.info
    async def _extract_extra(self, url: str):
        async with self.session.get(url, headers=self.headers, proxy=self.proxy) as r:
            response = await r.text("utf-8")
        if extracontent := re.search(r"<div class=\"half-day-card-content\">([\s\S]*?)<div class=\"quarter-day-ctas\">", response):
            extracontent = extracontent[0]
            self.info['weather'] = re.search(r"<div class=\"phrase\">(.*?)</div>", extracontent).group(1)
            if warnings := re.search(r"<div class=\"inline-alert-subheading\">([\s\S]*?)</div>", extracontent):
                self.info['warnings'] = {}
                self.info['warnings']['description'] = re.search(r"<p class=\"alert-description\">(.*?)</p>", warnings[0]).group(1)
                self.info['warnings']['time'] = re.search(r"<p>(.*?)</p>", warnings[0]).group(1)
            if panels := re.search(r'<div class=\"panels\">([\s\S]*?)$', extracontent):
                panels = panels[0]
                extrainfopattern = r"<p class=\"panel-item\">(.*?)<span class=\"value\">(.*?)</span></p>"
                extrainfo = re.findall(extrainfopattern, panels)
                for key, value in extrainfo:
                    self.info[key] = value
                    if self.info[key].endswith("°"):
                        self.info[key] += self.unit
    async def search(self, query: str, unit: Literal['C', 'F'] = 'C', darkmap: bool = True, proxy: str = None) -> dict:
        """
# Arguments:
    query (str) - the search query
    
    unit ('C' OR 'F') - temperature unit to use

    darkmap (bool) - whether the radar map to be in dark mode

    proxy (str) - optional proxy to use
# Returns:
    A dict object with forecasts, temperature, perticipation, alerts, and whatever accuweather provides on the site
        """
        self.unit = unit
        self.darkmap = darkmap
        if proxy and proxy.startswith("http"):
            self.proxy = proxy
        else:
            self.proxy = None
        if not hasattr(self, "session"):
            async with aiohttp.ClientSession(connector=self._make_connector(proxy)) as session:
                self.session = session
                info = await self._search(query)
        else:
            info = await self._search(query)
        return info
if __name__ == "__main__":
    asyncio.run(accuweather_api("cache_weather.txt").search("columbia, south carolina", unit="F", darkmap=True))