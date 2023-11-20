import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import  Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        self.setFixedSize(1000,1000)


    def run(self):
        self.do_paint = True
        self.pushButton.hide()
        self.update()


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def draw_flag(self, qp):
        for i in range(10):
            qp.setBrush(QColor(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)))
            a = random.randint(20, 400)
            coord1 = random.randint(0, 1000)
            coord2= random.randint(1,1000)
            qp.drawEllipse(coord1, coord2, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
