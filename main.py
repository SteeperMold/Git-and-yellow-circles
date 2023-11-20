import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui")
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(173, 255, 47))
        radius = random.randint(50, 200)
        qp.drawEllipse(200, 200, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec_())

