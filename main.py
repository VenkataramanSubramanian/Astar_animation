from grid import grid
from astar import astar
import numpy as np
import matplotlib.pyplot as plt
from matplot import plotting


'''

    The main class can be improved by taking input from user in cmd line

    grid_size
    number_of_person
    randomizing the start and end position for every person (check possible path exist)

'''
class main():

    person_path = []

    x_value = 20
    y_value = 20

    grid_obj = grid()
    grid_obj.generate_random_grid(x_value,y_value)
    generated_grid = grid_obj.get_grid()

    print(generated_grid)

    number_of_person = 1
    start_1 = (0,0)
    end_1   = (10,10)
    path_returned = astar(generated_grid, start_1, end_1)
    person_path.append(path_returned)
    plot_obj = plotting(generated_grid,person_path)
    plot_obj.plotting_grid()
    
main()