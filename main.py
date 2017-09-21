"""
GOAL FOR THIS TASK
* Add 5 text editors. Use one to set the window title. Use the others to set the window coordinates and size. In order to do this, drop the main() function and implement the proper class for your window. Coordinates and title should be set on click. Keywords: QLineEdit, setGeometry, QString and int.
* When window moves, update the text editors with actual coordinates. Keywords: moveEvent (don't remember exactly). Don't forget to call super methods (and learn about them).
* Align the editors in UI properly. Learn about Layouts. For this example, use QFormLayout. """

from PyQt4 import QtGui

class Window(QtGui.QWidget):
    xcord = 50
    ycord = 50
    xsize = 250
    ysize = 100
    initWindowName = "Change me"

    def __init__(self):
        # parent class __init__
        super(Window, self).__init__()

        # Create layout
        self.onlyInt = QtGui.QIntValidator()
        self.l1 = QtGui.QLabel("X coord")
        self.e1 = QtGui.QLineEdit()
        self.e1.setValidator(self.onlyInt)
        self.e1.setText(str(self.xcord))
        self.e1.setMaximumWidth(30)
        self.e1.editingFinished.connect(self.editingFinished)
        self.l2 = QtGui.QLabel("Y coord")
        self.e2 = QtGui.QLineEdit()
        self.e2.editingFinished.connect(self.editingFinished)
        self.e2.setValidator(self.onlyInt)
        self.e2.setText(str(self.ycord))
        self.e2.setMaximumWidth(30)
        self.l3 = QtGui.QLabel("X size")
        self.e3 = QtGui.QLineEdit()
        self.e3.setMaximumWidth(30)
        self.e3.editingFinished.connect(self.editingFinished)
        self.e3.setText(str(self.xsize))
        self.e3.setValidator(self.onlyInt)
        self.l4 = QtGui.QLabel("Y size")
        self.e4 = QtGui.QLineEdit()
        self.e4.editingFinished.connect(self.editingFinished)
        self.e4.setValidator(self.onlyInt)
        self.e4.setText(str(self.ysize))
        self.e4.setMaximumWidth(30)
        self.l5 = QtGui.QLabel("Window name")
        self.e5 = QtGui.QLineEdit()
        self.e5.setText(self.initWindowName)
        self.e5.editingFinished.connect(self.editingFinished)
        fbox = QtGui.QFormLayout()
        fbox.addRow(self.l1, self.e1)
        fbox.addRow(self.l2, self.e2)
        fbox.addRow(self.l3, self.e3)
        fbox.addRow(self.l4, self.e4)
        fbox.addRow(self.l5, self.e5)
        self.setLayout(fbox)
        # Set initial geo
        self.setGeometry(self.xcord, self.ycord, self.xcord + self.xsize, self.ycord + self.ysize)
        self.setWindowTitle(self.initWindowName)
        # have to find pythonlogo.png later
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        self.show()
        exit(app.exec_())

    def editingFinished(self):
        self.setGeometry(int(self.e1.text()), int(self.e2.text()), int(self.e3.text()), int(self.e4.text()))
        self.setWindowTitle(self.e5.text())

    def moveEvent(self, QMoveEvent):
        self.e1.setText(str(self.geometry().x()))
        self.e2.setText(str(self.geometry().y()))

    def resizeEvent(self, QResizeEvent):
        self.e3.setText(str(self.geometry().width()))
        self.e4.setText(str(self.geometry().height()))


app = QtGui.QApplication([])
GUI = Window()
