from urllib.request import urlopen
from urllib.parse import quote
from html.parser import HTMLParser
from tkinter import *
from tkinter import ttk
from unidecode import unidecode # You can install this library with pip install unidecode
from bs4 import BeautifulSoup
from selenium import webdriver
import os.path
# TODO Have it save after each word.
# TODO Add backup feature
# TODO Have it auto import existing words
# TODO Set up the example blowser only if you search for examples
# TODO Add an add example button

###########################################################################
# Method: _getExample                                                     #
###########################################################################
# This method grabs example using the selenium web driver                 #
###########################################################################
def _getExample(parser, word, f=None, numberOfExamples=3):

    # Use selenium with beautiful soup to get the text from each of the examples
    browser.get("http://www.spanishdict.com/examples/" + word)
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html5lib')

    parser.printLine("\n")

    strings = []

    x = 1
    for example in soup.findAll("div", {"class": "megaexamples-pair"}):
        if x < numberOfExamples+1:
            print("---Example " + str(x) + " ---")
            print("Spanish: " + example.contents[0].text)
            print("English: " + example.contents[1].text)
            print("-------------")
            parser.printLine("\n---Example " + str(x) + " ---\n")
            strings.append("Spanish: " + example.contents[0].text + '\n')
            strings.append("English: " + example.contents[1].text + '\n')
            parser.printLine(strings[-2])
            parser.printLine(strings[-1])
            parser.printLine("-------------\n")
        else:
            break
        x += 1

    # This is only used by the write word function. It just checks if a file has been passed in
    if f:
        examples = ""
        for string in strings:
            examples += string.replace("\n", "<br/>")

        f.write(parser.getSpanishWordBox().replace(";", ":").strip() + ";" + parser.getMeaning().replace("\n", "<br/>").strip(
            '<br/>').replace(";", ":") + examples.strip(
            '<br/>').replace(";", ":") + ";" + ";" + parser.getPartofSpeech().replace(";", ":") + "\n")

    return strings


###########################################################################
# Method: _destroy_right_pane                                             #
###########################################################################
# This method's only purpose is to destroy the right pane of the window   #
###########################################################################
def _destroy_right_pane():

    global right_pane
    global bottom_pane

    # Destroy the right pane
    paned_window.forget(right_pane)
    paned_window.forget(bottom_pane)

###########################################################################
# Method: _create_right_pane                                              #
###########################################################################
# This method is called when a user clicks a button on the left hand side.#
# After they click the button, a function is called. That function will   #
# call _create_right_pane to create a pane on the right hand side         #
# for itself.                                                             #
###########################################################################
def _create_right_pane(width, height, bwidth=90, bheight=40):
    # TODO need to find a way to have it autoresize
    # Create the second pane. This pane will contain the options for setting the data within the messages
    global right_pane
    global bottom_pane

    # Delete the old right pane so that we can create a new one
    _destroy_right_pane()
    right_pane = PanedWindow(paned_window, width=width, height=height, orient=VERTICAL, borderwidth=3, relief=GROOVE)
    paned_window.add(right_pane)
    bottom_pane = PanedWindow(paned_window, width=bwidth, height=bheight, orient=VERTICAL, borderwidth=3, relief=GROOVE)
    paned_window.add(bottom_pane)


def importWords():

    _destroy_right_pane()

    global list

    def _saveWords():
        del list[:]
        textInput = TextBox.get("1.0",'end-1c')
        for word in textInput.split('\n'):
            list.append(word)

    def _writeToFile():
        textInput = TextBox.get("1.0",'end-1c')
        with open('word_list', 'w+', encoding="utf-8") as f:
            for word in textInput.split('\n'):
                f.write(word + '\n')
            f.close()

    _create_right_pane(250,500)
    scrollbar = Scrollbar(right_pane)
    scrollbar.pack(side=RIGHT, fill=Y)
    TextBox = Text(right_pane, height=500, width=250, bg="black", fg="grey")
    TextBox.pack(side=LEFT, fill=Y)
    scrollbar.config(command=TextBox.yview)
    TextBox.config(yscrollcommand=scrollbar.set)

    if len(list) != 0:
        for word in list:
            TextBox.insert(END, word + '\n')
    else:
        if os.path.isfile("word_list"):
            with open("word_list", encoding="utf-8") as f:
                for word in f.readlines():
                    word = word.strip()

                    # This try except block eliminates blank spaces that shouldn't be there
                    try:
                        if word[0].isalpha():
                            list.append(word)
                            TextBox.insert(END, word + "\n")
                    except IndexError:
                        pass
        else:
            TextBox.insert(END, "Add words here. One on each line.")

    ttk.Button(bottom_pane, text="Save Words", command=_saveWords).pack()
    ttk.Button(bottom_pane, text="Write To File", command=_writeToFile).pack()


class SPAHTMLParser(HTMLParser):
        grabData = False
        grabExample = False

        isTitle = False
        isExample = False
        isPartofSpeech = False
        isContext = False
        isTranslation = False

        textBox = Text
        spanishWordBox = Text
        spanishWord = ''
        meaning = Text
        partOfSpeech = Text

        first = True
        sideBars = False

        x = 0
        y = 0

        def addTextBox(self, pane, width, height):
            scrollbar = Scrollbar(pane)
            scrollbar.pack(side=RIGHT, fill=Y)
            self.textBox = Text(pane, height=height, width=width, bg="black", fg="grey")
            self.textBox.pack(side=LEFT, fill=Y)
            scrollbar.config(command=self.textBox.yview)
            self.textBox.config(yscrollcommand=scrollbar.set)

        def _addSideBars(self):
            self.sideBars = True # This makes it so that the sidebars get populated with the correct wording

            # TODO FIX THE LABELING
            #Label(bottom_pane, text="Spanish Word:").grid(row=0, column=0, pady=7)
            #Label(bottom_pane, text="Meaning:").grid(row=0, column=2, pady=7)
            Label(bottom_pane, text="Part of Speech:").grid(row=2, column=0, pady=7)

            self.spanishWordBox = Text(bottom_pane, height=30, width=40, bg="black", fg="grey")
            self.meaning = Text(bottom_pane, height=30, width=40, bg="black", fg="grey")
            self.partOfSpeech = Text(bottom_pane, height=1, width=20, bg="black", fg="grey")

            self.spanishWordBox.grid(row=0, column=0)
            self.meaning.grid(row=0, column=1)
            self.partOfSpeech.grid(row=2, column=1)


        def clearTextBox(self):
            self.textBox.delete('1.0', END)

        def printLine(self, URL):
            self.textBox.insert(END, URL)

        # You need this function because it used to populate the text boxes on the right with everything from the
        # first dictionary found.
        def resetFirst(self):
            self.first = True

        def getSpanishWordBox(self):
            return self.spanishWordBox.get("1.0",'end-1c').strip()

        def setSpanishWordBox(self, word):
            self.spanishWordBox.insert(END, " " + word + "\n")

        def setSpanishWord(self, word):
            self.spanishWord = word

        def getMeaning(self):
            return self.meaning.get("1.0",'end-1c')

        def meaningIsEmpty(self):
            if self.meaning.get("1.0",'end-1c').strip() == "":
                return True
            else:
                return False

        def getPartofSpeech(self):
            if self.partOfSpeech.get("1.0",'end-1c').strip() == "":
                self.partOfSpeech.insert(END, "unknown")
            return self.partOfSpeech.get("1.0",'end-1c')

        def clearTextBoxesRight(self):
            self.spanishWordBox.delete('1.0', END)
            self.meaning.delete('1.0', END)
            self.partOfSpeech.delete('1.0', END)
            self.spanishWord = ''

        # Marks the word in anki
        def markWord(self):
            self.partOfSpeech.insert(END, "marked ")

        def addToMeaning(self, text):
            if self.sideBars:
                self.meaning.insert(END, text + '\n')
                return True
            else:
                return False

        def processHtml(self, html, quickLook=False):
            soup = BeautifulSoup(html, 'html.parser')

            word = soup.find("h1", {"class": "source-text"}).string.strip()

            if not quickLook:
                self.setSpanishWord(word.lower())
                self.setSpanishWordBox(word)

            def _processTag(tag, first):
                if tag is not None:
                    for string in tag.stripped_strings:
                        if len(string) > 2:
                            self.printLine(repr(string).replace('\'', '') + '\n')

                            if first and "Copyright" not in string:

                                if not unidecode(self.spanishWord) in unidecode(string.lower()):
                                    self.meaning.insert(END, string + '\n')
                                else:
                                    if not unidecode(string.lower().strip()) == unidecode(self.spanishWord) and not quickLook:
                                        self.spanishWordBox.insert(END, " " + string + '\n')

                    self.printLine("\n\n-------------------------- END DICTIONARY --------------------------\n\n")

                    tag = None

                    return False

                return True

            first = True

            first = _processTag(soup.find("div", {"class": "dictionary-entry dictionary-neodict"}), first)

            first = _processTag(soup.find('div', {'class': 'dictionary-entry dictionary-neoharrap'}), first)

            first = _processTag(soup.find('div', {'class': 'dictionary-entry dictionary-collins'}), first)

def getWords():


    _create_right_pane(800, 900, 300, 90)

    parser = SPAHTMLParser()
    parser.addTextBox(right_pane, 800, 900)
    parser._addSideBars()
    global exampleWord
    exampleWord = ''

    def _activateCheckbox():
        checkBox.includeExample = not checkBox.includeExample

    def nextWord():

        parser.clearTextBox()
        parser.clearTextBoxesRight()
        parser.resetFirst()

        if len(list)>0:

            # Don't read the empty elements - make sure they are skipped and removed
            try:
                while list[-1].strip() == "":
                    list.pop()
            except IndexError:
                pass

            word = quote(list[-1].replace(" ", "%20"))
            # TODO THIS SHOULD BE CLEANED UP
            global exampleWord
            exampleWord = word

            print("http://www.spanishdict.com/translate/" + list[-1].replace(" ", "%20"))
            url_string = unidecode("http://www.spanishdict.com/translate/" + word)
            #html =

            #parser.feed(html)
            parser.processHtml(urlopen(url_string).read().decode('utf-8'))

            #parser.printLine("http://www.spanishdict.com/translate/" + list[-1])

            # TODO THIS DOES NOT WORK BECAUSE IT GUESSES FOR NOUNS (TRY VERJA)
            #url_string = unidecode("http://www.spanishdict.com/conjugate/" + quote(list[-1].replace(" ", "%20")))
            #html = urlopen(url_string).read().decode('utf-8')
            #if "<span class=\"conj-irregular\">" in html:
            #    parser.markWord()

            if checkBox.includeExample:
                strings = _getExample(parser, word, None, 100).replace("<br/>", '\n')

                if len(strings) > 1:
                    parser.addToMeaning(strings[0])
        else:
            parser.printLine("No more words in list!")

    def writeWord():
        with open('new_cards', 'a+', encoding="utf-8") as f:
            # You need the <br/>s in anki for newlines. The strip makes sure there isn't one randomly trailing
            if not parser.meaningIsEmpty():
                if not checkBox.includeExample:
                    f.write(parser.getSpanishWordBox().replace("\n", "<br/>").strip('<br/>').replace(";", ":") + ";" + parser.getMeaning().replace("\n", "<br/>").strip('<br/>').replace(";", ":") + ";" + ";" + parser.getPartofSpeech().replace(";", ":") + "\n")
                # This begins the section which handles adding cards if examples are included
                else:
                    _getExample(parser, quote(list[-1].replace(" ", "%20")), f, 1)
            list.pop()
            f.close()
            nextWord()

    def skipWord():
        list.pop()
        nextWord()

    def _writeAll():
        with open('new_cards', 'a+', encoding="utf-8") as f:
            for word in list:
                writeWord()

    ttk.Button(bottom_pane, text='Next Word', command=nextWord).grid(row=3, column=0, padx=7, pady=7)
    ttk.Button(bottom_pane, text='Write Word', command=writeWord).grid(row=4, column=0, padx=7, pady=7)
    ttk.Button(bottom_pane, text='Skip Word\n(Remove From List)', command=skipWord).grid(row=5, column=0, padx=7, pady=7)
    ttk.Button(bottom_pane, text='Write All Words', command=_writeAll).grid(row=6, column=0, padx=7, pady=7)

    # This code is for adding a checkbox to ask if you want to include an example
    includeExample = BooleanVar
    checkBox = ttk.Checkbutton(bottom_pane, text="Add Example", variable=includeExample, onvalue=True, offvalue=False, command=_activateCheckbox)
    checkBox.includeExample = False
    checkBox.grid(row=7, column=0, padx=7, pady=7)

    ttk.Button(bottom_pane, text='Get Example', command= lambda: _getExample(parser, exampleWord, None, 100)).grid(row=8, column=0, padx=7, pady=7)

def quickLookup():

    def _activateCheckbox():
        checkBox.includeExample = not checkBox.includeExample

    def _lookup():

        parser.clearTextBox()

        # You need the unidecode function to strip out unicode characters. EX: colección se convirte en coleccion
        html = urlopen("http://www.spanishdict.com/translate/" + unidecode(entry.get().replace(" ", "%20"))).read().decode('utf-8')

        parser.processHtml(html, True)

        if checkBox.includeExample:
            _getExample(parser, entry.get(), None, 100)

    def _add():

        list.append(entry.get())

    _create_right_pane(900, 900, 150, 40)

    parser = SPAHTMLParser()
    parser.addTextBox(right_pane, 900, 800)

    Label(bottom_pane, text="Word:").grid(row=0, column=0, padx=7, pady=7)
    entry = Entry(bottom_pane, text="Enter word here")
    entry.grid(row=1, column=0)
    ttk.Button(bottom_pane, text="Lookup", command=_lookup).grid(row=2, column=0, padx=7, pady=7)
    ttk.Button(bottom_pane, text="Add to list", command=_add).grid(row=3, column=0, padx=7, pady=7)

    # This code is for adding a checkbox to ask if you want to include an example
    includeExample = BooleanVar
    checkBox = ttk.Checkbutton(bottom_pane, text="Add Example", variable=includeExample, onvalue=True, offvalue=False, command=_activateCheckbox)
    checkBox.includeExample = False
    checkBox.grid(row=4, column=0, padx=7, pady=7)

Tk().title("Tarjeta Maker - By Grant Curell")

# Create a paned window to contain our buttons
paned_window = PanedWindow()
paned_window.pack(fill=BOTH, expand=1)

# Create the first pane. This pane will be on the left and contain the buttons for message selection
left_pane = PanedWindow(paned_window, orient=VERTICAL)
paned_window.add(left_pane)

# Insert the buttons for selecting a message type into the left hand pane.

# This button allows a user to import words
ttk.Button(left_pane, text='Import Words', command=importWords).grid(row=0, column=0, pady=3, padx=3)

# This button allows the user to search for words
ttk.Button(left_pane, text='Get Words', command=getWords).grid(row=1, column=0, pady=3, padx=3)

# This button allows the user to do a quick lookup
ttk.Button(left_pane, text='Quick Lookup', command=quickLookup).grid(row=2, column=0, pady=3, padx=3)

middle_pane = PanedWindow(paned_window, orient=VERTICAL)
paned_window.add(middle_pane)
dst_ip = StringVar()

# TODO need to figure out how to pass arguments here

# Create a placeholder for the right pane.
right_pane = PanedWindow()
bottom_pane = PanedWindow()

global list
global browser
list = []

chop = webdriver.ChromeOptions()
chop.add_extension('AdBlock_v3.11.2.crx')
browser = webdriver.Chrome(chrome_options = chop)

mainloop()