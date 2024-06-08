import cairosvg, aiohttp, asyncio, os

async def get_all(limit: int = 45):
    async with aiohttp.ClientSession() as session:
        mainurl = "https://www.awxcdn.com/adc-assets/images/weathericons/"
        index = 1
        for index in range(0, limit):
            url = mainurl + f"{index}.svg"
            async with session.get(url) as r:
                if r.status != 200:
                    continue
                if not os.path.exists("converted"):
                    os.mkdir("converted")
                with open(f"converted/{index}.svg", 'wb') as f1:
                    while True:
                        chunk = await r.content.read(1024)
                        if not chunk:
                            break
                        f1.write(chunk)
            index += 1
            print(f"downloaded {index}.svg")
        index = 1
        for file in os.listdir("converted"):
            file = f"converted/{file}"
            if file.endswith("png"):
                continue
            try:
                png = cairosvg.svg2png(url=file)
            except:
                print(file)
                exit(1)
            with open(f"converted/{index}.png", "wb") as f1:
                f1.write(png)
            os.remove(file)
            index += 1
if __name__ == "__main__":
    asyncio.run(get_all())