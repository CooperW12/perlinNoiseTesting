import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise1 = PerlinNoise(octaves=4)
noise2 = PerlinNoise(octaves=9)
noise3 = PerlinNoise(octaves=5)
noise4 = PerlinNoise(octaves=8)

xpix, ypix = 500, 500
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.2 * noise3([i/xpix, j/ypix])
        noise_val += 0.7 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='twilight')

plt.imsave('image.png', pic, cmap='twilight')