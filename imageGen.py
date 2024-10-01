import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise1 = PerlinNoise(octaves=20)
noise2 = PerlinNoise(octaves=20)
#noise3 = PerlinNoise(octaves=20)
#noise4 = PerlinNoise(octaves=20)

xpix, ypix = 1024, 1024
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 1 * noise2([i/xpix, j/ypix])
        #noise_val += 1 * noise3([i/xpix, j/ypix])
        #noise_val += 1 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='twilight')

plt.imsave('image.png', pic, cmap='twilight')