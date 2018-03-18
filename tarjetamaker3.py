
# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from PyQt4 import QtCore, QtGui
from tarjetamaker3.tarjeta_ui import Ui_tarjeta_ui
import sys

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def start_tarjeta_maker():
    app = QtGui.QApplication(sys.argv)
    tarjeta_ui = QtGui.QWidget()
    ui = Ui_tarjeta_ui()
    ui.setupUi(tarjeta_ui)
    tarjeta_ui.show()
    sys.exit(app.exec_())

# create a new menu item, "test"
action = QAction("Tarjeta Maker", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(start_tarjeta_maker)
# and add it to the tools menu
mw.form.menuTools.addAction(action)