import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'DeOldify'))

import collections
import collections.abc
collections.Sized = collections.abc.Sized

from DeOldify.deoldify import device
from DeOldify.deoldify.device_id import DeviceId
from DeOldify.deoldify.visualize import get_image_colorizer

import torch

def colorize_image(input_path: str, output_path: str, render_factor: int = 35):
    device.set(device=DeviceId.GPU0 if torch.cuda.is_available() else DeviceId.CPU)
    colorizer = get_image_colorizer(artistic=True)
    colorized = colorizer.get_transformed_image(input_path, render_factor=render_factor)
    colorized.save(output_path)
    print(f"Изображение сохранено: {output_path}")

colorize_image("6.jpg", "6_colorized.jpg", render_factor=35)