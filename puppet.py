import asyncio
from pyppeteer import launch

import pyfakewebcam
import numpy as np
from numpy import asarray

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.google.com')
    await page.screenshot({'path': 'screen.jpg', 'width': '800', 'height': '600'})
    await browser.close()
    await show()


async def show():
    height = 480
    width = 640
    size = width, height

    img = Image.open("screen.jpg")
    img.thumbnail((width, height))

    camera = pyfakewebcam.FakeWebcam('/dev/video20', width, height)
    camera.schedule_frame(asarray(img))


asyncio.get_event_loop().run_until_complete(main())
