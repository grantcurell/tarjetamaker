# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarjeta_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL

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

class Ui_tarjeta_ui(object):

    list = []

    def setupUi(self, tarjeta_ui):
        tarjeta_ui.setObjectName(_fromUtf8("tarjeta_ui"))
        tarjeta_ui.resize(1873, 1038)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tarjeta_ui.sizePolicy().hasHeightForWidth())
        tarjeta_ui.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(tarjeta_ui)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tab_object_main = QtGui.QTabWidget(tarjeta_ui)
        self.tab_object_main.setObjectName(_fromUtf8("tab_object_main"))
        self.tab_import_words = QtGui.QWidget()
        self.tab_import_words.setObjectName(_fromUtf8("tab_import_words"))
        self.gridLayout = QtGui.QGridLayout(self.tab_import_words)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scroll_area_import_words = QtGui.QScrollArea(self.tab_import_words)
        self.scroll_area_import_words.setWidgetResizable(True)
        self.scroll_area_import_words.setObjectName(_fromUtf8("scroll_area_import_words"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1829, 974))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.text_edit_import_words = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.text_edit_import_words.setObjectName(_fromUtf8("text_edit_import_words"))
        self.gridLayout_6.addWidget(self.text_edit_import_words, 0, 0, 1, 1)
        self.push_button_save_words = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.push_button_save_words.setObjectName(_fromUtf8("push_button_save_words"))
        self.gridLayout_6.addWidget(self.push_button_save_words, 0, 1, 1, 1)
        self.scroll_area_import_words.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll_area_import_words, 0, 0, 1, 1)
        self.tab_object_main.addTab(self.tab_import_words, _fromUtf8(""))
        self.tab_create_cards = QtGui.QWidget()
        self.tab_create_cards.setObjectName(_fromUtf8("tab_create_cards"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_create_cards)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_front = QtGui.QLabel(self.tab_create_cards)
        self.label_front.setObjectName(_fromUtf8("label_front"))
        self.gridLayout_2.addWidget(self.label_front, 0, 1, 1, 1)
        self.label_back = QtGui.QLabel(self.tab_create_cards)
        self.label_back.setObjectName(_fromUtf8("label_back"))
        self.gridLayout_2.addWidget(self.label_back, 2, 1, 1, 1)
        self.push_button_add_card = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_add_card.setObjectName(_fromUtf8("push_button_add_card"))
        self.gridLayout_2.addWidget(self.push_button_add_card, 4, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_create_cards)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_spanishdict = QtGui.QWidget()
        self.tab_spanishdict.setObjectName(_fromUtf8("tab_spanishdict"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_spanishdict)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.text_browser_spanish_dict = QtGui.QTextBrowser(self.tab_spanishdict)
        self.text_browser_spanish_dict.setObjectName(_fromUtf8("text_browser_spanish_dict"))
        self.gridLayout_3.addWidget(self.text_browser_spanish_dict, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_spanishdict, _fromUtf8(""))
        self.tab_dle = QtGui.QWidget()
        self.tab_dle.setObjectName(_fromUtf8("tab_dle"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_dle)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.text_browser_dle = QtGui.QTextBrowser(self.tab_dle)
        self.text_browser_dle.setObjectName(_fromUtf8("text_browser_dle"))
        self.gridLayout_4.addWidget(self.text_browser_dle, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_dle, _fromUtf8(""))
        self.tab_wordreference = QtGui.QWidget()
        self.tab_wordreference.setObjectName(_fromUtf8("tab_wordreference"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_wordreference)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.text_browser_wordreference = QtGui.QTextBrowser(self.tab_wordreference)
        self.text_browser_wordreference.setObjectName(_fromUtf8("text_browser_wordreference"))
        self.gridLayout_5.addWidget(self.text_browser_wordreference, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_wordreference, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 3, 1)
        self.text_edit_card_back = QtGui.QTextEdit(self.tab_create_cards)
        self.text_edit_card_back.setObjectName(_fromUtf8("text_edit_card_back"))
        self.gridLayout_2.addWidget(self.text_edit_card_back, 1, 1, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.tab_create_cards)
        self.textEdit_3.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout_2.addWidget(self.textEdit_3, 3, 1, 1, 1)
        self.push_button_write_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_write_word.setObjectName(_fromUtf8("push_button_write_word"))
        self.gridLayout_2.addWidget(self.push_button_write_word, 5, 1, 1, 1)
        self.push_button_next_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_next_word.setObjectName(_fromUtf8("push_button_next_word"))
        self.gridLayout_2.addWidget(self.push_button_next_word, 4, 1, 1, 1)
        self.push_button_skip_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_skip_word.setObjectName(_fromUtf8("push_button_skip_word"))
        self.gridLayout_2.addWidget(self.push_button_skip_word, 6, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tab_object_main.addTab(self.tab_create_cards, _fromUtf8(""))
        self.tab_quick_lookup = QtGui.QWidget()
        self.tab_quick_lookup.setObjectName(_fromUtf8("tab_quick_lookup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_quick_lookup)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.text_browser_quick_lookup = QtGui.QTextBrowser(self.tab_quick_lookup)
        self.text_browser_quick_lookup.setObjectName(_fromUtf8("text_browser_quick_lookup"))
        self.gridLayout_7.addWidget(self.text_browser_quick_lookup, 1, 0, 1, 1)
        self.inline_edit_quicklook = QtGui.QLineEdit(self.tab_quick_lookup)
        self.inline_edit_quicklook.setObjectName(_fromUtf8("inline_edit_quicklook"))
        self.gridLayout_7.addWidget(self.inline_edit_quicklook, 1, 1, 1, 1)
        self.push_button_lookup = QtGui.QPushButton(self.tab_quick_lookup)
        self.push_button_lookup.setObjectName(_fromUtf8("push_button_lookup"))
        self.gridLayout_7.addWidget(self.push_button_lookup, 2, 1, 1, 1)
        self.label_quicklook_word = QtGui.QLabel(self.tab_quick_lookup)
        self.label_quicklook_word.setObjectName(_fromUtf8("label_quicklook_word"))
        self.gridLayout_7.addWidget(self.label_quicklook_word, 0, 1, 1, 1)
        self.push_button_add_to_list = QtGui.QPushButton(self.tab_quick_lookup)
        self.push_button_add_to_list.setObjectName(_fromUtf8("push_button_add_to_list"))
        self.gridLayout_7.addWidget(self.push_button_add_to_list, 3, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 2)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.tab_object_main.addTab(self.tab_quick_lookup, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tab_object_main)

        self.retranslateUi(tarjeta_ui)
        self.tab_object_main.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(tarjeta_ui)

        def _save_words(self):
            del list[:]
            for word in self.text_edit_import_words.toPlainText():
                list.append(word)

            with open('word_list', 'w+', encoding="utf-8") as f:
                for word in list:
                    f.write(word + '\n')
                f.close()

        QObject.connect(self.push_button_save_words, SIGNAL("clicked()"), self._save_words)

    def retranslateUi(self, tarjeta_ui):
        tarjeta_ui.setWindowTitle(_translate("tarjeta_ui", "Form", None))
        self.push_button_save_words.setText(_translate("tarjeta_ui", "Save Words", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_import_words), _translate("tarjeta_ui", "Import Words", None))
        self.label_front.setText(_translate("tarjeta_ui", "Front", None))
        self.label_back.setText(_translate("tarjeta_ui", "Back", None))
        self.push_button_add_card.setText(_translate("tarjeta_ui", "Add Card", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_spanishdict), _translate("tarjeta_ui", "SpanishDict", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dle), _translate("tarjeta_ui", "DLE", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_wordreference), _translate("tarjeta_ui", "WordReference", None))
        self.push_button_write_word.setText(_translate("tarjeta_ui", "Write Word", None))
        self.push_button_next_word.setText(_translate("tarjeta_ui", "Next Word", None))
        self.push_button_skip_word.setText(_translate("tarjeta_ui", "Skip Word (Remove From List)", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_create_cards), _translate("tarjeta_ui", "Create Cards", None))
        self.push_button_lookup.setText(_translate("tarjeta_ui", "Lookup", None))
        self.label_quicklook_word.setText(_translate("tarjeta_ui", "Word", None))
        self.push_button_add_to_list.setText(_translate("tarjeta_ui", "Add To List", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_quick_lookup), _translate("tarjeta_ui", "Quick Lookup", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    tarjeta_ui = QtGui.QWidget()
    ui = Ui_tarjeta_ui()
    ui.setupUi(tarjeta_ui)
    tarjeta_ui.show()
    sys.exit(app.exec_())
