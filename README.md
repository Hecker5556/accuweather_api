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
    "clouds_map": "https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile?apikey=de13920f574d420984d3080b1fa6132b&zoom=5&lon=-80.907&lat=33.819&imgwidth=768&imgheight=432&language=en-us&base_data=radar",
    "forecast": {
        "day-0": {
            "day": "Today",
            "date": "6/7",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/2.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/weather-today/330679",
            "temp-hi": "33°",
            "temp-lo": "17°",
            "weather_day": "Mostly sunny and less humid",
            "weather_night": "Night: Clear",
            "precipitation": "0%"
        },
        "day-1": {
            "day": "Sat",
            "date": "6/8",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/1.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/weather-tomorrow/330679",
            "temp-hi": "33°",
            "temp-lo": "18°",
            "weather_day": "Pleasant with sunshine",
            "weather_night": "Partly cloudy",
            "precipitation": "0%"
        },
        "day-2": {
            "day": "Sun",
            "date": "6/9",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=3",
            "temp-hi": "34°",
            "temp-lo": "21°",
            "weather_day": "Variable cloudiness",
            "weather_night": "Some clouds",
            "precipitation": "4%"
        },
        "day-3": {
            "day": "Mon",
            "date": "6/10",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=4",
            "temp-hi": "31°",
            "temp-lo": "18°",
            "weather_day": "Mostly cloudy",
            "weather_night": "Partly cloudy",
            "precipitation": "25%"
        },
        "day-4": {
            "day": "Tue",
            "date": "6/11",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=5",
            "temp-hi": "30°",
            "temp-lo": "18°",
            "weather_day": "Mostly cloudy and less humid",
            "weather_night": "Partly cloudy",
            "precipitation": "25%"
        },
        "day-5": {
            "day": "Wed",
            "date": "6/12",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/6.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=6",
            "temp-hi": "31°",
            "temp-lo": "20°",
            "weather_day": "Mostly cloudy and humid",
            "weather_night": "Showers around in the evening",
            "precipitation": "25%"
        },
        "day-6": {
            "day": "Thu",
            "date": "6/13",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/18.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=7",
            "temp-hi": "31°",
            "temp-lo": "20°",
            "weather_day": "Periods of rain and a t-storm",
            "weather_night": "Partly cloudy",
            "precipitation": "65%"
        },
        "day-7": {
            "day": "Fri",
            "date": "6/14",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/18.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=8",
            "temp-hi": "33°",
            "temp-lo": "21°",
            "weather_day": "Occasional rain and a t-storm",
            "weather_night": "Partly cloudy and humid",
            "precipitation": "55%"
        },
        "day-8": {
            "day": "Sat",
            "date": "6/15",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/4.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=9",
            "temp-hi": "34°",
            "temp-lo": "21°",
            "weather_day": "High clouds and humid",
            "weather_night": "Mainly clear and humid",
            "precipitation": "9%"
        },
        "day-9": {
            "day": "Sun",
            "date": "6/16",
            "image": "https://www.awxcdn.com/adc-assets/images/weathericons/1.svg",
            "url": "https://www.accuweather.com/en/us/columbia/29201/daily-weather-forecast/330679?day=10",
            "temp-hi": "33°",
            "temp-lo": "21°",
            "weather_day": "Brilliant sunshine",
            "weather_night": "Humid with increasing clouds",
            "precipitation": "2%"
        }
    },
    "RealFeel Shade™": "32°",
    "Wind": "WNW 13 km/h",
    "Wind Gusts": "28 km/h",
    "Air Quality": "Poor",
    "location": "World>North America>United States>South Carolina>Columbia",
    "weather": "Mostly sunny and less humid",
    "Max UV Index": "11 Extreme",
    "Probability of Precipitation": "0%",
    "Probability of Thunderstorms": "0%",
    "Precipitation": "0.0 mm",
    "Cloud Cover": "22%"
}
```