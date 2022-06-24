import numpy as np
np.random.seed(5)

class grid:

    def __init__(self, grid:np.float64 = None, grid_image=None) -> None:
        
        self.grid = grid
        self.grid_image = grid_image

    def generate_random_grid(self, gridX:int, gridY:int):
        size = (gridX, gridY)
        self.grid = np.random.choice([0, 1], size=size, p=[0.2, 0.8])

    def get_grid(self) -> np.float64:
        return self.grid

    #future implementation to set grid using image
    def set_grid_by_image(self, grid_image) -> np.float64:
        pass

    #future implementation to access grid using image
    def get_grid_by_image(self, grid_image) -> np.float64:
        return self.grid_image