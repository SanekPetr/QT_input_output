import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('send.ui', self)
        self.send_button.clicked.connect(self.sand)

    def sand(self):
        input_line = self.input_line.text()
        output_line = self.lineEdit.text()

        self.lineEdit.setText(str(input_line))



if __name__ == '__main__':
    ex = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(ex.exec())

