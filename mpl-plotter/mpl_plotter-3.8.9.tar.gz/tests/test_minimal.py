import unittest
import numpy as np


from tests.setup import show


class TestAll(unittest.TestCase):

    def test_two_d(self):
        from mpl_plotter.two_d import line, scatter, heatmap, quiver, streamline, fill_area

        line(show=show)

        scatter(show=show)

        heatmap(show=show)

        quiver(show=show)

        streamline(show=show)

        fill_area(show=show)

        # Input
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        line(x=x, y=y, show=show, aspect=1)

    def test_three_d(self):
        from mpl_plotter.three_d import line, scatter, surface

        line(show=show)

        scatter(show=show)

        surface(show=show)

        # Wireframe
        surface(show=show, alpha=0, line_width=0.5, edge_color="red", cstride=12, rstride=12)
