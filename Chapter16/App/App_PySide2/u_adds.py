# -*- coding: utf-8 -*-         #   PYTHON 2   #
import re                                      # Python regular expressions.
from PySide2.QtGui import QSyntaxHighlighter   # Import syntax highlighter.
from PySide2.QtGui import QTextCharFormat      # Char formatting from QtGui.
from PySide2.QtCore import Qt                  # For color of the format.


class UHighLight(QSyntaxHighlighter):          # Class of the highlighter.

    words = u"(?iu)[\\w\']+"                   # Used regular expressions.

    def __init__(self, *args):                 # Constructor of the class.
        super(UHighLight, self).__init__(*args)
        self.dicts = None                      # Default dicts None.

    def setDict(self, dicts):                  # Set the dicts depends
        self.dict = dicts                      # from used languages.

    def highlightBlock(self, text):            # Function for formatting
        if not self.dict:                      # the text inside this text 
            return                             # edit field, sets the format
        formats = QTextCharFormat()            # of the text that not match
        formats.setUnderlineColor(Qt.red)      # to the dicts. Red underline.
        formats.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
        for w in re.finditer(self.words, text):
            if not self.dict.check(w.group()):
                self.setFormat(w.start(), w.end() - w.start(), formats)
