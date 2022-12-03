import asyncio
import os
import async_timeout
import aiohttp

async def download_complete(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as filehandle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    filehandle.write(chunk)
            print(f"{filename} was created...")
            return await response.release()

async def main(loop):
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            print(await download_complete(session, url))

if __name__ == "__main__":
    ev_loop = asyncio.get_event_loop()
    ev_loop.run_until_complete(main(ev_loop))
    ev_loop.close()

