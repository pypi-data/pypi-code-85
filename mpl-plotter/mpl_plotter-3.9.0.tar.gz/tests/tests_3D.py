import unittest
import numpy as np
from mpl_plotter.three_d import line, scatter, surface


from tests.setup import show


class Tests(unittest.TestCase):

    def test_line(self):
        line(show=show, azim=33, elev=27, demo_pad_plot=True)

    def test_scatter(self):
        scatter(point_size=60,
                grid=True, grid_lines='-.',
                cmap='plasma', x_tick_number=5,
                color_bar=True, show=show,
                azim=33, elev=27,)

    def test_surface(self):
        surface(show=show,
                azim=-122, elev=35,
                alpha=1, demo_pad_plot=True,
                lighting=False, antialiased=False, shade=False,
                edge_color="black", edges_to_rgba=True, line_width=0.5,
                rstride=1, cstride=1,
                blend_edges=True, pane_fill="red")


    def test_wireframe(self):
        surface(show=show,
                azim=-122, elev=35,
                alpha=0,
                lighting=False, antialiased=False, shade=False,
                edge_color="red", edges_to_rgba=False, line_width=0.5,
                rstride=12, cstride=12)
