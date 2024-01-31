import matplotlib
matplotlib.use('Qt5Agg')
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from model import Model

class Viewport3D(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.model = Model()

        self.axes = fig.add_subplot(111, projection='3d')
        
        self.axes.set_xlabel('x(m)')
        self.axes.set_ylabel('y(m)')
        self.axes.set_zlabel('z(m)')

        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_zticklabels([])

        self.axes.grid(True)

        super(Viewport3D, self).__init__(fig)

    def draw_robot(self, d, l1, l2, l3):
        self.axes.clear()
        
        p = self.model.FKM_actuators(d, l1, l2, l3)

        self.axes.scatter(p[:, 0], p[:, 1], p[:, 2], marker='.')
        self.draw()


