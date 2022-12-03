import asyncio
import string
from typing import final
import urllib.request
import os


async def download_complete(url:string):
    """
    A coroutine to download the specified url
    """
    req = urllib.request.urlopen(url)
    filename = os.path.basename(url)

    with open(filename, "wb") as filehandle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            filehandle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg


async def main(urls):
    """
    Creates a group of coroutines and waits for them to finish
    """
    co_routines = [download_complete(url) for url in urls]
    completed, pending = await asyncio.wait(co_routines)
    for item in completed:
        print(item.result())


if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    ev_loop = asyncio.get_event_loop()
    try:
        ev_loop.run_until_complete(main(urls))
    finally:
        ev_loop.close()