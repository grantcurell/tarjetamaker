# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarjeta_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from __future__ import with_statement
from __future__ import absolute_import
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
import os
from urllib2 import urlopen
from urllib import quote
from HTMLParser import HTMLParser
from unidecode import unidecode # You can install this library with pip install unidecode
from bs4 import BeautifulSoup
from selenium import webdriver
import os.path
from io import open

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
    browser = webdriver

    def __init__(self):
        chop = webdriver.ChromeOptions()
        chop.add_extension(u'AdBlock_v3.11.2.crx')
        self.browser = webdriver.Chrome(chrome_options=chop)

    def setupUi(self, tarjeta_ui):
        tarjeta_ui.setObjectName(_fromUtf8(u"tarjeta_ui"))
        tarjeta_ui.resize(1873, 1038)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tarjeta_ui.sizePolicy().hasHeightForWidth())
        tarjeta_ui.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(tarjeta_ui)
        self.horizontalLayout.setObjectName(_fromUtf8(u"horizontalLayout"))
        self.tab_object_main = QtGui.QTabWidget(tarjeta_ui)
        self.tab_object_main.setObjectName(_fromUtf8(u"tab_object_main"))
        self.tab_import_words = QtGui.QWidget()
        self.tab_import_words.setObjectName(_fromUtf8(u"tab_import_words"))
        self.gridLayout = QtGui.QGridLayout(self.tab_import_words)
        self.gridLayout.setObjectName(_fromUtf8(u"gridLayout"))
        self.scroll_area_import_words = QtGui.QScrollArea(self.tab_import_words)
        self.scroll_area_import_words.setWidgetResizable(True)
        self.scroll_area_import_words.setObjectName(_fromUtf8(u"scroll_area_import_words"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1829, 974))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8(u"scrollAreaWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8(u"gridLayout_6"))
        self.text_edit_import_words = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.text_edit_import_words.setObjectName(_fromUtf8(u"text_edit_import_words"))
        self.gridLayout_6.addWidget(self.text_edit_import_words, 0, 0, 1, 1)
        self.push_button_save_words = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.push_button_save_words.setObjectName(_fromUtf8(u"push_button_save_words"))
        self.gridLayout_6.addWidget(self.push_button_save_words, 0, 1, 1, 1)
        self.scroll_area_import_words.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll_area_import_words, 0, 0, 1, 1)
        self.tab_object_main.addTab(self.tab_import_words, _fromUtf8(u""))
        self.tab_create_cards = QtGui.QWidget()
        self.tab_create_cards.setObjectName(_fromUtf8(u"tab_create_cards"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_create_cards)
        self.gridLayout_2.setObjectName(_fromUtf8(u"gridLayout_2"))
        self.label_front = QtGui.QLabel(self.tab_create_cards)
        self.label_front.setObjectName(_fromUtf8(u"label_front"))
        self.gridLayout_2.addWidget(self.label_front, 0, 1, 1, 1)
        self.label_back = QtGui.QLabel(self.tab_create_cards)
        self.label_back.setObjectName(_fromUtf8(u"label_back"))
        self.gridLayout_2.addWidget(self.label_back, 2, 1, 1, 1)
        self.push_button_add_card = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_add_card.setObjectName(_fromUtf8(u"push_button_add_card"))
        self.gridLayout_2.addWidget(self.push_button_add_card, 4, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_create_cards)
        self.tabWidget_2.setObjectName(_fromUtf8(u"tabWidget_2"))
        self.tab_spanishdict = QtGui.QWidget()
        self.tab_spanishdict.setObjectName(_fromUtf8(u"tab_spanishdict"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_spanishdict)
        self.gridLayout_3.setObjectName(_fromUtf8(u"gridLayout_3"))
        self.text_browser_spanish_dict = QtGui.QTextBrowser(self.tab_spanishdict)
        self.text_browser_spanish_dict.setObjectName(_fromUtf8(u"text_browser_spanish_dict"))
        self.gridLayout_3.addWidget(self.text_browser_spanish_dict, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_spanishdict, _fromUtf8(u""))
        self.tab_dle = QtGui.QWidget()
        self.tab_dle.setObjectName(_fromUtf8(u"tab_dle"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_dle)
        self.gridLayout_4.setObjectName(_fromUtf8(u"gridLayout_4"))
        self.text_browser_dle = QtGui.QTextBrowser(self.tab_dle)
        self.text_browser_dle.setObjectName(_fromUtf8(u"text_browser_dle"))
        self.gridLayout_4.addWidget(self.text_browser_dle, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_dle, _fromUtf8(u""))
        self.tab_wordreference = QtGui.QWidget()
        self.tab_wordreference.setObjectName(_fromUtf8(u"tab_wordreference"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_wordreference)
        self.gridLayout_5.setObjectName(_fromUtf8(u"gridLayout_5"))
        self.text_browser_wordreference = QtGui.QTextBrowser(self.tab_wordreference)
        self.text_browser_wordreference.setObjectName(_fromUtf8(u"text_browser_wordreference"))
        self.gridLayout_5.addWidget(self.text_browser_wordreference, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_wordreference, _fromUtf8(u""))
        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 3, 1)
        self.text_edit_card_front = QtGui.QTextEdit(self.tab_create_cards)
        self.text_edit_card_front.setObjectName(_fromUtf8(u"text_edit_card_back"))
        self.gridLayout_2.addWidget(self.text_edit_card_front, 1, 1, 1, 1)
        self.text_edit_card_back = QtGui.QTextEdit(self.tab_create_cards)
        self.text_edit_card_back.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.text_edit_card_back.setObjectName(_fromUtf8(u"textEdit_3"))
        self.gridLayout_2.addWidget(self.text_edit_card_back, 3, 1, 1, 1)
        self.push_button_write_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_write_word.setObjectName(_fromUtf8(u"push_button_write_word"))
        self.gridLayout_2.addWidget(self.push_button_write_word, 5, 1, 1, 1)
        self.push_button_next_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_next_word.setObjectName(_fromUtf8(u"push_button_next_word"))
        self.gridLayout_2.addWidget(self.push_button_next_word, 4, 1, 1, 1)
        self.push_button_skip_word = QtGui.QPushButton(self.tab_create_cards)
        self.push_button_skip_word.setObjectName(_fromUtf8(u"push_button_skip_word"))
        self.gridLayout_2.addWidget(self.push_button_skip_word, 6, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tab_object_main.addTab(self.tab_create_cards, _fromUtf8(u""))
        self.tab_quick_lookup = QtGui.QWidget()
        self.tab_quick_lookup.setObjectName(_fromUtf8(u"tab_quick_lookup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_quick_lookup)
        self.gridLayout_7.setObjectName(_fromUtf8(u"gridLayout_7"))
        self.text_browser_quick_lookup = QtGui.QTextBrowser(self.tab_quick_lookup)
        self.text_browser_quick_lookup.setObjectName(_fromUtf8(u"text_browser_quick_lookup"))
        self.gridLayout_7.addWidget(self.text_browser_quick_lookup, 1, 0, 1, 1)
        self.inline_edit_quicklook = QtGui.QLineEdit(self.tab_quick_lookup)
        self.inline_edit_quicklook.setObjectName(_fromUtf8(u"inline_edit_quicklook"))
        self.gridLayout_7.addWidget(self.inline_edit_quicklook, 1, 1, 1, 1)
        self.push_button_lookup = QtGui.QPushButton(self.tab_quick_lookup)
        self.push_button_lookup.setObjectName(_fromUtf8(u"push_button_lookup"))
        self.gridLayout_7.addWidget(self.push_button_lookup, 2, 1, 1, 1)
        self.label_quicklook_word = QtGui.QLabel(self.tab_quick_lookup)
        self.label_quicklook_word.setObjectName(_fromUtf8(u"label_quicklook_word"))
        self.gridLayout_7.addWidget(self.label_quicklook_word, 0, 1, 1, 1)
        self.push_button_add_to_list = QtGui.QPushButton(self.tab_quick_lookup)
        self.push_button_add_to_list.setObjectName(_fromUtf8(u"push_button_add_to_list"))
        self.gridLayout_7.addWidget(self.push_button_add_to_list, 3, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 2)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.tab_object_main.addTab(self.tab_quick_lookup, _fromUtf8(u""))
        self.horizontalLayout.addWidget(self.tab_object_main)

        self.retranslateUi(tarjeta_ui)
        self.tab_object_main.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(tarjeta_ui)

        QObject.connect(self.push_button_save_words, SIGNAL(u"clicked()"), self._save_words)
        QObject.connect(self.push_button_next_word, SIGNAL(u"clicked()"), self._create_card)
        QObject.connect(self.push_button_write_word, SIGNAL(u"clicked()"), self._write_word)
        QObject.connect(self.push_button_lookup, SIGNAL(u"clicked()"), self._quick_lookup)
        QObject.connect(self.push_button_add_to_list, SIGNAL(u"clicked()"), self._add_to_list)
        QObject.connect(self.push_button_skip_word, SIGNAL(u"clicked()"), self._skip_word)
        QObject.connect(self.push_button_skip_word, SIGNAL(u"clicked()"), self._skip_word)

        ###########################################
        # Import cards                            #
        ###########################################
        if len(self.list) != 0:
            for word in self.list:
                self.text_edit_import_words.insertPlainText(word + u'\n')
        else:
            if os.path.isfile(u"word_list"):
                with open(u"word_list", encoding=u"utf-8") as f:
                    for word in f.readlines():
                        word = word.strip()

                        # This try except block eliminates blank spaces that shouldn't be there
                        try:
                            if word[0].isalpha():
                                self.list.append(word)
                                self.text_edit_import_words.insertPlainText(word + u"\n")
                        except IndexError:
                            pass
            else:
                self.text_edit_import_words.insertPlainText(u"Add words here. One on each line.")

    # Not auto-generated functions
    def _save_words(self):
        del self.list[:]
        for word in self.text_edit_import_words.toPlainText():
            self.list.append(word)

        with open(u'word_list', u'w+', encoding=u"utf-8") as f:
            for word in self.list:
                f.write(word + u'\n')
            f.close()

    def create_cards_printline(self, text, box):

        if box == u"spanishDict":
            self.text_browser_spanish_dict.insertPlainText(text)
        elif box == u"dle":
            self.text_browser_dle.insertPlainText(text)
        elif box == u"wordreference":
            self.text_browser_wordreference.insertPlainText(text)
        else:
            print u"WARNING: Nothing matched"

    def quick_lookup_printline(self, text):
        self.text_browser_quick_lookup.insertPlainText(text)

    def create_cards_printline_front(self, text):
        self.text_edit_card_front.insertPlainText(text)

    def _clear_create_card_text_boxes(self):

        self.text_browser_spanish_dict.clear()
        self.text_browser_dle.clear()
        self.text_browser_wordreference.clear()
        self.text_edit_card_front.clear()
        self.text_edit_card_back.clear()

    def _create_card(self):

        self._clear_create_card_text_boxes()

        parser = SPAHTMLParser(self)

        if len(self.list) > 0:

            # Don't read the empty elements - make sure they are skipped and removed
            try:
                while self.list[-1].strip() == u"":
                    self.list.pop()
            except IndexError:
                pass

            word = quote(self.list[-1].replace(u" ", u"%20"))

            # SpanishDict
            print u"http://www.spanishdict.com/translate/" + self.list[-1].replace(u" ", u"%20")
            url_string = unidecode(u"http://www.spanishdict.com/translate/" + word)
            parser.process_spanishdict(urlopen(url_string).read().decode(u'utf-8'))

            # Word Reference
            self.browser.get(unidecode(u"http://www.wordreference.com/definicion/" + word))
            parser.process_wordreference(self.browser.page_source)

            # DLE
            self.browser.get(unidecode(u"http://dle.rae.es/" + word))
            parser.process_dle(self.browser.page_source)

            # Google Chrome
            self.browser.get(unidecode(u'https://www.google.com/search?tbm=isch&q=' + word))


        else:
            parser.printLine(u"No more words in list!", u"spanishDict")

    def _skip_word(self):
        self.list.pop()

    def _write_word(self):
        with open(u'new_cards', u'a+', encoding=u"utf-8") as f:
            # You need the <br/>s in anki for newlines. The strip makes sure there isn't one randomly trailing
            f.write(self.text_edit_card_front.toPlainText().replace(u"\n", u"<br/>").strip(u'<br/>').replace(u";", u":") + u";" + self.text_edit_card_back.toPlainText().replace(u"\n", u"<br/>").strip(u'<br/>').replace(u";", u":") + u";" + u";" + u"" + u"\n")
            # This begins the section which handles adding cards if examples are included
            self.list.pop()
            f.close()
            self._create_card()

    ###########################################
    # Quick Lookup                            #
    ###########################################

    def _clear_quick_lookup_text_boxes(self):
        self.text_browser_quick_lookup.clear()

    def _quick_lookup(self):

        parser = SPAHTMLParser(self)

        print u"http://www.spanishdict.com/translate/" + self.inline_edit_quicklook.text().replace(u" ", u"%20")
        url_string = unidecode(u"http://www.spanishdict.com/translate/" + self.inline_edit_quicklook.text().replace(u" ", u"%20"))
        parser.process_spanishdict(urlopen(url_string).read().decode(u'utf-8'), True)

    def _add_to_list(self):

        self.list.append(self.inline_edit_quicklook.text())
        self.text_edit_import_words.insertPlainText(self.inline_edit_quicklook.text() + u"\n")

    def retranslateUi(self, tarjeta_ui):
        tarjeta_ui.setWindowTitle(_translate(u"tarjeta_ui", u"Form", None))
        self.push_button_save_words.setText(_translate(u"tarjeta_ui", u"Save Words", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_import_words), _translate(u"tarjeta_ui", u"Import Words", None))
        self.label_front.setText(_translate(u"tarjeta_ui", u"Front", None))
        self.label_back.setText(_translate(u"tarjeta_ui", u"Back", None))
        self.push_button_add_card.setText(_translate(u"tarjeta_ui", u"Add Card", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_spanishdict), _translate(u"tarjeta_ui", u"SpanishDict", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dle), _translate(u"tarjeta_ui", u"DLE", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_wordreference), _translate(u"tarjeta_ui", u"WordReference", None))
        self.push_button_write_word.setText(_translate(u"tarjeta_ui", u"Write Word", None))
        self.push_button_next_word.setText(_translate(u"tarjeta_ui", u"Next Word", None))
        self.push_button_skip_word.setText(_translate(u"tarjeta_ui", u"Skip Word (Remove From List)", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_create_cards), _translate(u"tarjeta_ui", u"Create Cards", None))
        self.push_button_lookup.setText(_translate(u"tarjeta_ui", u"Lookup", None))
        self.label_quicklook_word.setText(_translate(u"tarjeta_ui", u"Word", None))
        self.push_button_add_to_list.setText(_translate(u"tarjeta_ui", u"Add To List", None))
        self.tab_object_main.setTabText(self.tab_object_main.indexOf(self.tab_quick_lookup), _translate(u"tarjeta_ui", u"Quick Lookup", None))

class SPAHTMLParser(HTMLParser):

    x = 0
    y = 0

    tarjeta_ui = Ui_tarjeta_ui

    def __init__(self, tarjeta_ui):
        self.tarjeta_ui = tarjeta_ui

    def process_spanishdict(self, html, quick_look=False):
        soup = BeautifulSoup(html, u'html.parser')

        word = soup.find(u"h1", {u"class": u"source-text"}).string.strip()

        if not quick_look:
            self.tarjeta_ui.create_cards_printline_front(word.lower())

        def _processTag(tag):
            if tag is not None:
                for string in tag.stripped_strings:
                    if len(string) > 2:
                        print repr(string).replace(u'\'', u'') + u'\n'

                        if quick_look:
                            self.tarjeta_ui.quick_lookup_printline(repr(string).replace(u'\'', u'') + u'\n')
                        else:
                            self.tarjeta_ui.create_cards_printline(repr(string).replace(u'\'', u'') + u'\n', u"spanishDict")

                if quick_look:
                    self.tarjeta_ui.quick_lookup_printline(u"\n\n-------------------------- END DICTIONARY --------------------------\n\n")
                else:
                    self.tarjeta_ui.create_cards_printline(u"\n\n-------------------------- END DICTIONARY --------------------------\n\n", u"spanishDict")

                return False

            return True

        _processTag(soup.find(u"div", {u"class": u"dictionary-entry dictionary-neodict"}))

        _processTag(soup.find(u'div', {u'class': u'dictionary-entry dictionary-neoharrap'}))

        _processTag(soup.find(u'div', {u'class': u'dictionary-entry dictionary-collins'}))

    def process_wordreference(self, html):

        soup = BeautifulSoup(html, u'html.parser')

        def _processTag(tag):
            if tag is not None:
                for string in tag.stripped_strings:
                    if len(string) > 2:
                        print repr(string).replace(u'\'', u'') + u'\n'
                        self.tarjeta_ui.create_cards_printline(repr(string).replace(u'\'', u'') + u'\n', u"wordreference")

        _processTag(soup.find(u'ol', {u'class': u'entry'}))

    def process_dle(self, html):

        soup = BeautifulSoup(html, u'html.parser')

        def _process_tag(tag):
            if tag is not None:
                for string in tag.stripped_strings:
                    if len(string) > 2:
                        print repr(string).replace(u'\'', u'') + u'\n'
                        self.tarjeta_ui.create_cards_printline(repr(string).replace(u'\'', u'') + u'\n', u"dle")

        for tag in soup.find_all(u"p", [u"j", u"j2", u"k6", u"m"]):
            print tag.text
            self.tarjeta_ui.create_cards_printline(tag.text + u"\n", u"dle")
