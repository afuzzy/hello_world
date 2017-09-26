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
#class Window(QtGui.QMainWindow):
    def __init__(self):
        # call for ancestor`s class __init__
        super(Window, self).__init__()

        # moved main variables from class variables to instance variables, so they are not shared between all objects anymore
        self.xcoord = 50
        self.ycoord = 60
        self.xsize = 250
        self.ysize = 300
        self.initWindowTitle = "Change me"


        # Create layout
        layout_box = QtGui.QFormLayout(self)

        # menu bar
        self.menuBar = QtGui.QMenuBar()
        self.fileOpenAction = QtGui.QAction('&Open', self)
        self.fileOpenAction.triggered.connect(self.openPyFile)
        self.exitAction = QtGui.QAction('&Exit', self)
        self.exitAction.triggered.connect(self.close_application)
        self.fileMenu = self.menuBar.addMenu('&File')
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.exitAction)
        layout_box.addRow(self.menuBar)


        # validator for int inputs
        self.onlyInt = QtGui.QIntValidator()


        # input parameters list for window control
        windowParamsList = [["X coord", self.xcoord], ["Y coord", self.ycoord], ["X size", self.xsize],
                            ["Y size", self.ysize]]

        self.labels = []
        self.edits = []
        # window position and size controls created inside loop based on list [label, initial_value]
        # trying different loops here for better code readability
        """ 
        #old version       
        for param in windowParamsList:
            self.labels.append(QtGui.QLabel(windowParamsList[windowParamsList.index(param)][0], self))
            self.edits.append(QtGui.QLineEdit(self))
            self.edits[windowParamsList.index(param)].setValidator(self.onlyInt)
            self.edits[windowParamsList.index(param)].setText(str(windowParamsList[windowParamsList.index(param)][1]))
            self.edits[windowParamsList.index(param)].setMaximumWidth(30)
            self.edits[windowParamsList.index(param)].editingFinished.connect(self.editingFinished)
            layout_box.addRow(self.labels[windowParamsList.index(param)], self.edits[windowParamsList.index(param)])
        """


        """
        # enumerate solution looks more readable of cource. It works!!!
        for counter,param in enumerate(windowParamsList):
            self.labels.append(QtGui.QLabel(param[0],self))
            self.edits.append(QtGui.QLineEdit(self))
            self.edits[counter].setValidator(self.onlyInt)
            self.edits[counter].setText(str(param[1]))
            self.edits[counter].setMaximumWidth(30)
            self.edits[counter].editingFinished.connect(self.editingFinished)
            layout_box.addRow(self.labels[counter], self.edits[counter])
        """

        """
        # solution with iterating over both list fields! It works!!!
        counter=0
        for label,value in windowParamsList:
            self.labels.append(QtGui.QLabel(label,self))
            self.edits.append(QtGui.QLineEdit(self))
            self.edits[counter].setValidator(self.onlyInt)
            self.edits[counter].setText(str(value))
            self.edits[counter].setMaximumWidth(30)
            self.edits[counter].editingFinished.connect(self.editingFinished)
            layout_box.addRow(self.labels[counter], self.edits[counter])
            counter+=1
        del counter
        """

        """        
        # solution with enumerate and iterating over both list fields! It works!!!
        # this looks amost elegant and readable
        for counter, (label, value) in enumerate(windowParamsList):
            self.labels.append(QtGui.QLabel(label, self))
            self.edits.append(QtGui.QLineEdit(self))
            self.edits[counter].setValidator(self.onlyInt)
            self.edits[counter].setText(str(value))
            self.edits[counter].setMaximumWidth(30)
            self.edits[counter].editingFinished.connect(self.editingFinished)
            layout_box.addRow(self.labels[counter], self.edits[counter])
        """

        # and last smart improvement, even better
        for counter, (label, value) in enumerate(windowParamsList):
            self.labels.append(QtGui.QLabel(label, self))
            edit=QtGui.QLineEdit(self)
            edit.setValidator(self.onlyInt)
            edit.setText(str(value))
            edit.setMaximumWidth(30)
            edit.editingFinished.connect(self.editingFinished)
            self.edits.append(edit)
            layout_box.addRow(self.labels[counter], self.edits[counter])


        # window tittle edit interface
        self.label_windowTitle = QtGui.QLabel("Window title", self)
        self.edit_WindowTitle = QtGui.QLineEdit(self)
        self.edit_WindowTitle.setText(self.initWindowTitle)
        self.edit_WindowTitle.editingFinished.connect(self.editingFinished)
        layout_box.addRow(self.label_windowTitle, self.edit_WindowTitle)

        #Code window
        self.label_Code = QtGui.QLabel("Code to run", self)
        self.edit_Code = QtGui.QTextEdit(self)
        layout_box.addRow(self.label_Code, self.edit_Code)

        #Run button
        self.runButton = QtGui.QPushButton('Run', self)
        self.runButton.clicked.connect(self.runButtonAction)
        layout_box.addRow(self.runButton)


        # Set initial window geo and title
        self.move(int(self.edits[0].text()), int(self.edits[1].text()))
        self.resize(int(self.edits[2].text()), int(self.edits[3].text()))
        self.setWindowTitle(self.initWindowTitle)

        """    
        #old way (did not respect frame)
        def editingFinished(self):
            self.setGeometry(int(self.edits[0].text()), int(self.edits[1].text()), int(self.edits[2].text()),
                             int(self.edits[3].text()))
            self.setWindowTitle(self.edit_WindowTitle.text())

        def moveEvent(self, QMoveEventMy):
            self.edits[0].setText(str(self.geometry().x()))
            self.edits[1].setText(str(self.geometry().y()))
            super(Window, self).moveEvent(QMoveEventMy)
        """


    #new way, now it respects window framing
    def editingFinished(self):

        self.move(int(self.edits[0].text()), int(self.edits[1].text()))
        self.resize(int(self.edits[2].text()), int(self.edits[3].text()))
        self.setWindowTitle(self.edit_WindowTitle.text())

    #new way, not sure if it is better
    def moveEvent(self, QMoveEvent):
        self.edits[0].setText(str(self.pos().x()))
        self.edits[1].setText(str(self.pos().y()))
        super(Window, self).moveEvent(QMoveEvent)


    def resizeEvent(self, QResizeEvent):
        self.edits[2].setText(str(self.size().width()))
        self.edits[3].setText(str(self.size().height()))
        super(Window, self).resizeEvent(QResizeEvent)

    def close_application(self):
        exit()

    def openPyFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        text = open(fileName).read()
        self.edit_Code.setText(text)
    def runButtonAction(self):
        code=str(self.edit_Code.toPlainText())
        exec(code)


# main check added to make sure we are running a program, not just importing module
if __name__ == "__main__":
    app = QtGui.QApplication([])
    GUI = Window()
    GUI.show()
    exit(app.exec_())
