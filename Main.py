import sys
from PyQt5.QtWidgets import QApplication
from GUI import Main_GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Main_GUI()
    gui.show()
    sys.exit(app.exec_())