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