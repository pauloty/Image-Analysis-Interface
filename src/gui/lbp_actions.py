from lbp import *
from Extractors import *
from PyQt4 import QtCore, QtGui
from ActionsGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class LBP(QtGui.QFrame, Ui_lbp):
    mainWindow = None

    def __init__(self, parent=None):
        super(LBP, self).__init__(parent)
        self.setupUi(self)
        self.fillCombobox()
        self.processPushButton.clicked.connect(self.process)
        self.clearTextPushButton.clicked.connect(self.clearMessages)
        self.pathButton.clicked.connect(self.path)

    def setMainWindow(self, mainWindow):
        self.mainWindow = mainWindow

    def process(self):
        method = self.comboBox.currentText()
        radius = self.radiusSpinBox.value()
        sampling_points = self.npointsSpinBox.value()
        path = self.directoryLineEdit.text()
        self.messagesPlainTextEdit.setPlainText("Processing, please wait")

        # Call LBP method for the high and low density images
        images = []
        images.append(self.mainWindow.high)
        images.append(self.mainWindow.low)
        lbp(images, sampling_points, radius, method)

        self.messagesPlainTextEdit.setPlainText("Success")

    def fillCombobox(self):
        methods = ["default", "ror", "uniform", "nri_uniform", "var"]
        for x in methods:
            self.comboBox.addItem(x)

    def clearMessages(self):
        self.messagesPlainTextEdit.clear()

    def path(self):
        fileName = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))

        if fileName:
            print(fileName)
            self.directoryLineEdit.setText(fileName)

