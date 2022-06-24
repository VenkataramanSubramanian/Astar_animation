import matplotlib.pyplot as plt
import numpy as np

class plotting():

    def __init__(self, grid:np.float64, paths:np.array) -> None:
        self.grid = grid
        self.paths = paths

    def plotting_grid(self):

        x_value = len(self.grid)
        y_value = len(self.grid[0])

        obstacle_location = np.where(self.grid==0)      
        obs_x = [i for i in obstacle_location[0]]
        obs_y = [i for i in obstacle_location[1]]
        plt.plot(obs_x, obs_y, "sk")
        plt.xlim([-1, x_value])
        plt.xticks(np.arange(0, x_value+1, 1.0))
        plt.ylim([-1, y_value])
        plt.yticks(np.arange(0, y_value+1, 1.0))
        plt.gca().get_yaxis().set_visible(False)
        plt.gca().get_xaxis().set_visible(False)

        plt.title("Astar Plotting")

        for path in self.paths:

            start_pt = path[0]
            end_pt   = path[-1]
            plt.plot(start_pt[0],start_pt[1], "bs")
            plt.plot(end_pt[0],end_pt[1], "gs")

        for path in self.paths:
            for x, y in path[1:]:
                plt.plot(x, y, color='r', marker='o')
                plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])
                plt.pause(0.1)
            # path_x = [path[p][0] for p in range(len(path))]
            # path_y = [path[p][1] for p in range(len(path))]
            # plt.plot(path_x, path_y, 'r--', linewidth='3')
        
        plt.show()

