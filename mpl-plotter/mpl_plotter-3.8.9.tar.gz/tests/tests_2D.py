import unittest
import numpy as np
import matplotlib.pyplot as plt

from mpl_plotter.two_d import heatmap, line, quiver, scatter, streamline, fill_area


from tests.setup import show


class Tests(unittest.TestCase):

    def test_line(self):
        x = np.linspace(0, 10, 1000)
        y = np.sinh(x)
        line(x, y, norm=y, aspect=1,
             grid=True, grid_lines='-.', x_tick_number=5, color_bar=True, show=show)

    def test_scatter(self):
        def t1():
            scatter(grid=True, grid_lines='-.', cmap='magma', x_tick_number=5,
                    color_bar=True, show=show)

        def t2():
            x = np.linspace(0, 10, 1000)
            y = np.sinh(x)
            scatter(x=x, y=y, color="green",
                    plot_label="Green bubbles", legend=True, legend_loc=(0.5, 0.5),
                    resize_axes=True, show=show)
        t1()
        plt.clf()
        t2()

    def test_heatmap(self):
        heatmap(color_bar=True, show=show)

    def test_quiver(self):
        quiver(x_bounds=[0, 1], y_bounds=[0, 1],
               x_custom_tick_locations=[0.2, 0.8], y_custom_tick_locations=[0.2, 0.8],
               x_custom_tick_labels=[100, 1000], y_custom_tick_labels=[9, -9],
               color_bar=True, show=show)

    def test_streamline(self):
        x = np.linspace(0, 10, 1000)
        y = np.linspace(0, 10, 1000)
        x, y = np.meshgrid(x, y)
        u = np.cos(x)
        v = np.cos(y)
        streamline(x=x, y=y, u=u, v=v, color=u, color_bar=True, show=show)

    def test_fill(self):
        fill_area(show=show)
