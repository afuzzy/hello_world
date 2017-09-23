# coding=utf-8
"""
GOAL FOR THIS TASK
* Add 5 text editors. Use one to set the window title. Use the others to set the window coordinates and size. In order to do this, drop the main() function and implement the proper class for your window. Coordinates and title should be set on click. Keywords: QLineEdit, setGeometry, QString and int.
* When window moves, update the text editors with actual coordinates. Keywords: moveEvent (don't remember exactly). Don't forget to call super methods (and learn about them).
* Align the editors in UI properly. Learn about Layouts. For this example, use QFormLayout. """

"""
You’ve forgot to call super. Please learn and explain what happens if you do and if you don’t. For example, when you create and ancestor class not from QWidget, but from this actual class, override the moveEvent - again - and don’t call super.
Also, it’s a bad idea to call your parameters the same as their types, might be a misunderstanding source. I know PyCharm is automatically creating this for you, but it’s a mistake by them. Please correct.
"""

from PyQt4 import QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        # call for ancestor`s class __init__
        super(Window, self).__init__()

        # moved main variables from class variables to instance variables, so they are not shared between all objects anymore
        self.xcoord = 50
        self.ycoord = 60
        self.xsize = 250
        self.ysize = 100
        self.initWindowTitle = "Change me"

        # Create layout
        layout_box = QtGui.QFormLayout(self)

        # validator for int inputs
        self.onlyInt = QtGui.QIntValidator()

        # input parameters list for window control
        windowParamsList = [["X coord", self.xcoord], ["Y coord", self.ycoord], ["X size", self.xsize],
                            ["Y size", self.ysize]]

        self.label = []
        self.edit = []
        # window position and size controls created inside loop based on list [label, initial_value]
        for param in windowParamsList:
            self.label.append(QtGui.QLabel(windowParamsList[windowParamsList.index(param)][0], self))
            self.edit.append(QtGui.QLineEdit(self))
            self.edit[windowParamsList.index(param)].setValidator(self.onlyInt)
            self.edit[windowParamsList.index(param)].setText(str(windowParamsList[windowParamsList.index(param)][1]))
            self.edit[windowParamsList.index(param)].setMaximumWidth(30)
            self.edit[windowParamsList.index(param)].editingFinished.connect(self.editingFinished)
            layout_box.addRow(self.label[windowParamsList.index(param)], self.edit[windowParamsList.index(param)])

        # window tittle
        self.label_windowName = QtGui.QLabel("Window title", self)
        self.edit_WindowName = QtGui.QLineEdit(self)
        self.edit_WindowName.setText(self.initWindowTitle)
        self.edit_WindowName.editingFinished.connect(self.editingFinished)
        layout_box.addRow(self.label_windowName, self.edit_WindowName)

        # Set initial window geo
        self.setGeometry(self.xcoord, self.ycoord, self.xcoord + self.xsize, self.ycoord + self.ysize)
        self.setWindowTitle(self.initWindowTitle)


    def editingFinished(self):
        self.setGeometry(int(self.edit[0].text()), int(self.edit[1].text()), int(self.edit[2].text()),
                         int(self.edit[3].text()))
        self.setWindowTitle(self.edit_WindowName.text())

    def moveEvent(self, QMoveEventMy):
        self.edit[0].setText(str(self.geometry().x()))
        self.edit[1].setText(str(self.geometry().y()))
        super(Window, self).moveEvent(QMoveEventMy)

    def resizeEvent(self, QResizeEventMy):
        self.edit[2].setText(str(self.geometry().width()))
        self.edit[3].setText(str(self.geometry().height()))
        super(Window, self).resizeEvent(QResizeEventMy)


# main check added to make sure we are running a program, not just importing module
if __name__ == "__main__":
    app = QtGui.QApplication([])
    GUI = Window()
    GUI.show()
    # testing with second window
    GUI2 = Window()
    GUI2.show()

    exit(app.exec_())
