from PySide6.QtWidgets import QApplication, QMainWindow
from sim_gui import Ui_MainWindow
from viewport3d import Viewport3D

class SimulationPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.l1a.valueChanged.connect(self.l1a_changed)

        self.sc = Viewport3D(self, width=6, height=4, dpi=100)
        self.ui.horizontalLayout.addWidget(self.sc)
        self.sc.draw_robot(0.101, 0.106, 0.106, 0.100)

    def l1a_changed(self, value):
        self.sc.draw_robot(0.101, value / 100.0, 0.106, 0.100)


def main():
    app = QApplication([])
    window = SimulationPanel()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
