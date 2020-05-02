import asyncio
from asyncio import sleep
from pprint import pprint
from pyppeteer import launch
import pyfakewebcam
from numpy import asarray
from PIL import Image

working = True


async def screenshot():
    browser = await launch()
    page = await browser.newPage()
    while working:
        try:
            print("Screenshot")
            await page.goto('http://127.0.0.1:8000/active/sunday-quiz-15883998427516189/', {'timeout': 15000})
            await page.screenshot({'path': 'screen.jpg', 'width': '800', 'height': '600'})
        except Exception as e:
            pprint(e)
            await browser.close()
            browser = await launch()
            page = await browser.newPage()

        await sleep(.1)

    await browser.close()


async def show():
    height = 480
    width = 640
    size = width, height
    camera = pyfakewebcam.FakeWebcam('/dev/video20', width, height)
    while working:
        print("frame")
        img = Image.open("screen.jpg")
        img.thumbnail((width, height))

        camera.schedule_frame(asarray(img))
        await sleep(.2)


def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(screenshot())
        asyncio.ensure_future(show())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()


if __name__ == '__main__':
    main()
