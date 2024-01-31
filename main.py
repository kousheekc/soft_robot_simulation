from PySide6.QtWidgets import QApplication, QMainWindow
from sim_gui import Ui_MainWindow
from viewport3d import Viewport3D
from model import Model

class SimulationPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = Model(0.1, 0.1, [0.2, 0.2, 0.2, 0.2, 0.2, 0.2])

        self.ui.l1a.valueChanged.connect(self.l1a_changed)
        self.ui.l1b.valueChanged.connect(self.l1b_changed)
        self.ui.l1c.valueChanged.connect(self.l1c_changed)
        self.ui.l2a.valueChanged.connect(self.l2a_changed)
        self.ui.l2b.valueChanged.connect(self.l2b_changed)
        self.ui.l2c.valueChanged.connect(self.l2c_changed)

        self.sc = Viewport3D(self, width=6, height=4, dpi=100)
        self.ui.horizontalLayout.addWidget(self.sc)

        line1, line2 = self.model.update("l1a", 0.2)
        self.sc.draw_robot(line1, line2)

    def l1a_changed(self, value):
        line1, line2 = self.model.update("l1a", value/100)
        self.sc.draw_robot(line1, line2)

    def l1b_changed(self, value):
        line1, line2 = self.model.update("l1b", value/100)
        self.sc.draw_robot(line1, line2)

    def l1c_changed(self, value):
        line1, line2 = self.model.update("l1c", value/100)
        self.sc.draw_robot(line1, line2)

    def l2a_changed(self, value):
        line1, line2 = self.model.update("l2a", value/100)
        self.sc.draw_robot(line1, line2)

    def l2b_changed(self, value):
        line1, line2 = self.model.update("l2b", value/100)
        self.sc.draw_robot(line1, line2)

    def l2c_changed(self, value):
        line1, line2 = self.model.update("l2c", value/100)
        self.sc.draw_robot(line1, line2)

def main():
    app = QApplication([])
    window = SimulationPanel()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
