import matplotlib
matplotlib.use('Qt5Agg')
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Viewport3D(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')
        self.set_axes_settings()
        super(Viewport3D, self).__init__(fig)

    def set_axes_settings(self):
        self.axes.set_xlabel('x(m)')
        self.axes.set_ylabel('y(m)')
        self.axes.set_zlabel('z(m)')

        # self.axes.set_xticklabels([])
        # self.axes.set_yticklabels([])
        # self.axes.set_zticklabels([])

        self.axes.set_xlim([-0.3, 0.3])
        self.axes.set_ylim([-0.3, 0.3])
        self.axes.set_zlim([0, 0.6])

        self.axes.set_box_aspect([1, 1, 1])

        self.axes.grid(True)

    def draw_robot(self, p):
        self.axes.clear()
        self.set_axes_settings()
        self.axes.plot3D(p[:, 0], p[:, 1], p[:, 2], linestyle='-')
        self.draw()


