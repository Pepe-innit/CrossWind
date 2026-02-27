import random
import pygame

class Fish:
    WEIGHT_RANGES = {
        "Bass": (0.5, 1.0),
        "Carp": (1.5, 3.0),
        "Catfish": (3.0, 5.0),
        "Flopper": (5.0, 7.5)
    }

    IMAGE_PATHS = {
        "Bass": "assets/CrossWinds_BassRAR.png",
        "Carp": "assets/CrossWinds_CarpRAR.png",
        "Catfish": "assets/CrossWinds_CatfishRAR.png",
        "Flopper": "assets/CrossWinds_FlopperRAR.png"
    }



    def __init__(self, name):
        self.name = name

        min_w, max_w = self.WEIGHT_RANGES.get(name, (0.5, 1.0))

        self.weight = round(random.uniform(min_w, max_w), 2)

        self.image = pygame.image.load(self.IMAGE_PATHS[name]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))