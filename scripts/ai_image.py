
import random
from PIL import Image, ImageDraw, ImageColor, ImageFilter
import numpy as np

def buat_random_color_scheme():
    return [random.randint(0, 255) for _ in range(3)]
def complex_noise_pattern(width, height):
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
def fractal_noise(x, y, octaves=8):
    value = 0.0
    amplitude = 1.0
    frequency = 1.0
    for _ in range(octaves):
        value += (random.random() * 2 - 1) * amplitude
        amplitude /= 2
        frequency *= 2
    return (value + 1) * 0.5
def image(width=512, height=512, complexity=10):
    img = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(img)
    patterns = [buat_random_color_scheme() for _ in range(complexity)]
    for i in range(0, width, 5):
        for j in range(0, height, 5):
            if (i + j) % 2 == 0:
                color = random.choice(patterns)
            else:
                noise = complex_noise_pattern(1, 1)
                color = tuple(noise.flatten())
            fractal_intensity = fractal_noise(i / width, j / height)
            modulated_color = tuple(int(c * fractal_intensity) for c in color)
            if fractal_intensity > 0.5:
                draw.rectangle([i, j, i+5, j+5], fill=modulated_color)
            else:
                draw.point((i, j), fill=modulated_color)
            if random.random() < 0.1:
                blend_img = Image.new('RGB', (50, 50), tuple(random.choice(patterns)))
                img.paste(blend_img, (i, j), blend_img)
    if complexity > 8:
        img = img.filter(ImageFilter.GaussianBlur(complexity // 3))
    return img
if __name__ == "__main__":
    img = image()
    img.show()
