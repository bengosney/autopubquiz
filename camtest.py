# see red_blue.py in the examples dir
import time
import pyfakewebcam
import numpy as np
from numpy import asarray

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

height = 480
width = 640
size = width, height

img = Image.open("background.jpg")
img.thumbnail((width, width))

# img = Image.new('RGB', (width, height), (255, 255, 255))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Roboto-Regular.ttf", 24)
draw.text((0, 0), "What does the computer software acronym JVM stand for?", (255, 255, 255), font=font)

bob = asarray(img)

blue = np.zeros((height, width, 3), dtype=np.uint8)
blue[:, :, 2] = 255

red = np.zeros((height, width, 3), dtype=np.uint8)
red[:, :, 0] = 255

camera = pyfakewebcam.FakeWebcam('/dev/video20', width, height)

while True:
    camera.schedule_frame(bob)
