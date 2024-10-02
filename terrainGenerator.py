import matplotlib.pyplot as plt
from PIL import Image
import noise.perlin
import numpy as np
import noise
import random 


shape= (1024, 1024)
scale = 100
octaves = 4
persistence =.5
lacunarity = 2
seed = [random.randint(0,1000000),random.randint(0,1000000)]
world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(
        (i + seed[0])/scale,
        (j + seed[1])/scale,
        octaves = octaves,
        persistence = persistence,
        lacunarity = lacunarity,
        repeatx = 1024,
        repeaty = 1024,
        base = 0
        )
        
deepOcean = [94, 129, 172]
ocean = [115, 146, 183]
fish = [58, 75, 94]
beach = [235, 203, 139]
seashell = [185, 85, 189]
wreckage = [105, 70, 1]
land = [143, 176, 115]
tree = [15, 64, 0]
forest = [106, 122, 92]
mountain = [76, 86, 106]
tallMountain = [121, 133, 159]
snow = [216, 222, 233]


def addColor(world):
    coloredWorld = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            
            if world[i][j] < -.2:
                coloredWorld[i][j] = deepOcean
            elif world[i][j] < 0:
                coloredWorld[i][j] = ocean
            elif world[i][j] < .05:
                if world[i][j] < .01:
                    r = random.randint(0,100)
                    if r < 1:
                        coloredWorld[i][j] = wreckage
                    else:
                        coloredWorld[i][j] = beach
                else:
                    coloredWorld[i][j] = beach
            elif world[i][j] < .15:
                    coloredWorld[i][j] = land
            elif world[i][j] < .25:
                r = random.randint(0,100)
                if r < 10:
                   coloredWorld[i][j] = tree
                else:
                    coloredWorld[i][j] = forest
            elif world[i][j] < .3:
                coloredWorld[i][j] = mountain
            elif world[i][j] < .4:
                coloredWorld[i][j] = tallMountain
            elif world[i][j] < 1:
                coloredWorld[i][j] = snow
    return coloredWorld

coloredWorld = addColor(world)

img = Image.fromarray(coloredWorld.astype('uint8'), 'RGB')
img.show()
img.save('terrain.png')

