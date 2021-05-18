import unittest

import numpy as np
import matplotlib.pyplot as plt

from mpl_plotter.setup import figure
from mpl_plotter.setup import custom_canvas2
from mpl_plotter.two_d import line, quiver, heatmap, streamline, fill_area
from mpl_plotter.three_d import surface


from tests.setup import show


class Tests(unittest.TestCase):

    def test_basic(self):

        backend = "Qt5Agg"  # None -> regular non-interactive matplotlib output

        fig = figure(figsize=(10, 10), backend=backend)

        ax0 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, aspect=1, fig=fig)
        ax1 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, aspect=1, fig=fig)
        ax2 = plt.subplot2grid((2, 2), (0, 1), rowspan=1, aspect=1, fig=fig)
        ax3 = plt.subplot2grid((2, 2), (1, 1), rowspan=1, aspect=12, fig=fig)

        axes = [ax0, ax1, ax2, ax3]
        plots = [line, quiver, streamline, fill_area]

        for i in range(len(plots)):
            plots[i](fig=fig, ax=axes[i],
                     backend=backend
                     )

        if show:
            plt.show()

    def test_demo(self):

        fig = figure((18, 8))

        ax1 = plt.subplot2grid((2, 6), (0, 0), colspan=2, rowspan=2, projection='3d', facecolor="#fff6e6")
        ax2 = plt.subplot2grid((2, 6), (0, 3), rowspan=1, aspect=1)
        ax3 = plt.subplot2grid((2, 6), (1, 3), rowspan=1, aspect=1)
        ax4 = plt.subplot2grid((2, 6), (0, 5), rowspan=1, aspect=1)
        ax5 = plt.subplot2grid((2, 6), (1, 5), rowspan=1, aspect=1)

        surface(fig=fig, ax=ax1,
                title="Demo",
                title_size=70,
                title_weight="bold",
                title_font="Pump Triline",
                title_color="#e69300",
                plot_label="Surface",
                background_color_plot="#fff6e6",
                edge_color="lightgrey", edges_to_rgba=True,
                azim=-160,
                elev=43)
        fill_area(fig=fig, ax=ax2,
                  plot_label="Fill", aspect=1, grid=False)
        quiver(fig=fig, ax=ax3,
               plot_label="Quiver", grid=False)
        heatmap(fig=fig, ax=ax4,
                title="No label",
                plot_label="Heatmap", grid=False)
        streamline(fig=fig, ax=ax5,
                   line_density=1,
                   title="No label",
                   plot_label="Streamline", grid=False)

        custom_canvas2(fig=fig, ax=ax2,
                       background_color_figure="#fff6e6",
                       legend=True, legend_loc=(0.6725, 0.425),
                       resize_axes=False)

        if show:
            plt.show()
