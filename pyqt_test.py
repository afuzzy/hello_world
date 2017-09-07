"""
PyQt window with button
author: Anton Ognyev
"""
import sys
from PyQt4 import QtGui
def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Just do it')
    b=QtGui.QPushButton("Click me",w)
    b.setToolTip('Click to quit!')
    b.setCheckable(True)
    b.clicked.connect(exit)
    b.move(90,70)

    w.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()