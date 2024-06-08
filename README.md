# Simple and free accuweather API
Their free api only offers up to 50 calls per day, so this script will provide unlimited calls for the same (or more) information.
Caches search queries.

# Installation
1. in terminal
```bash
git clone https://github.com/Hecker5556/accuweather_api
```
2. 
```bash
pip install -r requirements.txt
```

I used python 3.10.9

# Usage
```python
import asyncio
info = asyncio.run(accuweather_api().search("columbia, south carolina"))
```
```python
async def main():
    info = await accuweather_api("mycache.json").search("columbia, south carolina")
```

# Extra information
Accuweather's search api doesn't support states, so if you want to grab south carolina for example you'll need to specify a specific city

# Example result
```json
{
    "clouds_map": "https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&zoom=5&lon=-80.907&lat=33.819&imgwidth=768&imgheight=432&language=en-us&base_data=radar&theme=dark",
    "forecast": {
        "day-0": {
            "day": "Today",
            "date": "6/8",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/1.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/weather-today/330679",
            "temp-hi": "90°F",
            "temp-lo": "67°F",
            "weather_day": "Sunny; pleasant, low humidity",
            "weather_night": "Night: Partly cloudy",
            "precipitation": "0%"
        },
        "day-1": {
            "day": "Sun",
            "date": "6/9",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/weather-tomorrow/330679",
            "temp-hi": "97°F",
            "temp-lo": "70°F",
            "weather_day": "Variable cloudiness",
            "weather_night": "Some clouds; humid",
            "precipitation": "20%"
        },
        "day-2": {
            "day": "Mon",
            "date": "6/10",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=3",
            "temp-hi": "88°F",
            "temp-lo": "62°F",
            "weather_day": "Mostly cloudy",
            "weather_night": "Mainly clear",
            "precipitation": "11%"
        },
        "day-3": {
            "day": "Tue",
            "date": "6/11",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=4",
            "temp-hi": "85°F",
            "temp-lo": "61°F",
            "weather_day": "Mostly cloudy",
            "weather_night": "Clear",
            "precipitation": "3%"
        },
        "day-4": {
            "day": "Wed",
            "date": "6/12",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=5",
            "temp-hi": "87°F",
            "temp-lo": "68°F",
            "weather_day": "Mostly cloudy",
            "weather_night": "Partly cloudy and humid",
            "precipitation": "9%"
        },
        "day-5": {
            "day": "Thu",
            "date": "6/13",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/18.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=6",
            "temp-hi": "90°F",
            "temp-lo": "71°F",
            "weather_day": "Some rain and a thunderstorm",
            "weather_night": "Partly cloudy and humid",
            "precipitation": "84%"
        },
        "day-6": {
            "day": "Fri",
            "date": "6/14",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/12.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=7",
            "temp-hi": "89°F",
            "temp-lo": "70°F",
            "weather_day": "Some rain and a thunderstorm",
            "weather_night": "Humid; a t-storm around early",
            "precipitation": "59%"
        },
        "day-7": {
            "day": "Sat",
            "date": "6/15",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/4.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=8",
            "temp-hi": "90°F",
            "temp-lo": "72°F",
            "weather_day": "Sun through high clouds",
            "weather_night": "Partly cloudy",
            "precipitation": "4%"
        },
        "day-8": {
            "day": "Sun",
            "date": "6/16",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/7.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=9",
            "temp-hi": "91°F",
            "temp-lo": "73°F",
            "weather_day": "A thick cloud cover",
            "weather_night": "Humid; a few showers late",
            "precipitation": "25%"
        },
        "day-9": {
            "day": "Mon",
            "date": "6/17",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/12.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=10",
            "temp-hi": "94°F",
            "temp-lo": "74°F",
            "weather_day": "A couple of morning showers",
            "weather_night": "Overcast and humid",
            "precipitation": "55%"
        }
    },
    "RealFeel Shade™": "82°F",
    "Wind": "NNW 6 mph",
    "Wind Gusts": "10 mph",
    "Air Quality": "Fair",
    "location": "World>North America>United States>South Carolina>Columbia",
    "temperature": "84°F",
    "weather": "Low humidity with sunshine; a beautiful start to the weekend",
    "Max UV Index": "12 Extreme",
    "Probability of Precipitation": "0%",
    "Probability of Thunderstorms": "0%",
    "Precipitation": "0.00 in",
    "Cloud Cover": "3%"
}
```