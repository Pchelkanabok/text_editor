from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QMessageBox, QShortcut, QFontDialog
from PyQt5.QtGui import *
# from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtGui import QKeySequence  # для горячих клавиш
import sys
import commands_lib


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("TextEditor")
        self.setGeometry(300, 250, 550, 300)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.document = self.text_edit.document()
        self.cursor = QTextCursor(self.document)

        self.open_new_file_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.open_new_file_shortcut.activated.connect(self.shortcut_open)

        self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.save_current_file_shortcut.activated.connect(self.shortcut_save)

        self.create_menu_bar()

    def shortcut_save(self):
        commands_lib.save_current_file(self)

    def shortcut_open(self):
        commands_lib.open_file(self)

    def closeEvent(self, event):
        messagebox = QMessageBox()
        title = "Quit Application?"
        message = "If you quit without saving, any changes made to the file will be lost.\n" \
                  "Save file before quitting?"
        reply = messagebox.question(self, title, message, messagebox.Yes | messagebox.No |
                                    messagebox.Cancel, messagebox.Cancel)
        if reply == messagebox.Yes:
            return_value = commands_lib.save_current_file(self)
            if not return_value:
                event.ignore()
        elif reply == messagebox.No:
            event.accept()
        else:
            event.ignore()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        filemenu = QMenu("&File", self)
        self.menuBar.addMenu(filemenu)
        filemenu.addAction('Open', self.action_clicked)
        filemenu.addAction('Save', self.action_clicked)

        align = QMenu("&Align", self)
        self.menuBar.addMenu(align)
        align.addAction('Left', self.action_align)
        align.addAction('Center', self.action_align)
        align.addAction('Right', self.action_align)

        style = QMenu('&Font Style', self)
        self.menuBar.addMenu(style)
        style.addAction('Bold', self.action_edit_style)
        style.addAction('Italic', self.action_edit_style)
        style.addAction('Underline', self.action_edit_style)

        fonts = QMenu('&Fonts', self)
        self.menuBar.addMenu(fonts)
        fonts.addAction('Times New Roman', self.action_edit_font)
        fonts.addAction('Arial', self.action_edit_font)
        # style.addAction('Underline', self.action_edit_style)

        save_as = filemenu.addMenu("&Save as...")
        save_as.addAction('Save to txt', self.action_save_as)
        save_as.addAction('Convert to PDF', self.action_save_as)

    @QtCore.pyqtSlot()
    def action_align(self):
        action = self.sender()
        if action.text() == "Left":
            print("Left")
        elif action.text() == "Center":
            print("Center")
        elif action.text() == "Right":
            print("Right")

    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            commands_lib.open_file(self)
        elif action.text() == "Save":
            commands_lib.save_current_file(self)

    def action_save_as(self):
        action = self.sender()
        if action.text() == "Save as txt":
            commands_lib.save_as_txt(self)

        elif action.text() == "Save as PDF":
            commands_lib.save_as_pdf(self)

    def action_edit_style(self):
        action = self.sender()
        if action.text() == "Bold":
            #self.text_edit.setFontWeight(QFont.Bold)
            #self.text_edit.setFontWeight(75)
            print(self.text_edit.textCursor().selectedText())
            print(self.text_edit.textCursor().selectionStart())
            print(self.text_edit.textCursor().selectionEnd())
            font, b_ok = QFontDialog.getFont()
            print(font, b_ok)

            if b_ok:
                print(font.family())
                print(font.italic())
                print(font.bold())
                print(font.weight())
                print(font.pointSize())
                #print(font.strikeout())
                #self.text_edit.textCursor().selectedText().setFont(font)
                #all_text = self.text_edit.toPlainText()
                #print(all_text)
                #text_1 = ''
                #text_2 = ''
                #for i in range (0,self.text_edit.textCursor().selectionStart()):
                #    text_1 = text_1 + all_text[i]
                #for i in range (0,self.text_edit.textCursor().selectionEnd()):
                #    text_2 = text_2 + all_text[i]
                #self.text_edit.setText(ttt_1)
                #self.text_edit.append(text_1)

                #self.text_edit.setFont(font)
                #self.text_edit.cursor().setPos(0,self.text_edit.textCursor().selectionStart())
                #self.text_edit.textCursor().setPosition
                #self.cursor.selectedText().
                #curs = self.text_edit.textCursor()
                #curs.setPosition(0)
                #curs.setPosition(self.text_edit.textCursor().selectionStart(), QtGui.QTextCursor.KeepAnchor)
                #self.text_edit.setTextCursor(curs)
                self.text_edit.setFontFamily(font.family())
                self.text_edit.setFontWeight(font.weight())
                self.text_edit.setFontItalic(font.italic())
                self.text_edit.setFontPointSize(font.pointSize())
                self.text_edit.setFontUnderline(font.underline())
                self.text_edit.set
                #self.text_edit.
                #self.text_edit.setFont(font)

                #self.text_edit.setFontWeight(font)
                #self.text_edit.setFontItalic(font)
                #self.text_edit.setFontPointSize(font)



            #self.text_edit.textCursor().selectedText().setFont(font)

            #print('Bold')
            # c = self.text_edit.textCursor().selectedText()
            # if font_info.bold():
            #print(QtGui.QFontInfo(self.text_edit.textCursor().selectedText()))
            #font_info = self.text_edit.textCursor().selectedText()
            #print(font_info.bold())
            #print(self.text_edit.textCursor().selectedText())

            # self.text_edit.setFontWeight(setBold(True))

            # font = self.text_edit.textCursor().selectedText()
            # print(font.fontInfo())

        elif action.text() == "Italic":
            # print('Italic')
            font_info = self.text_edit.fontInfo()
            print(font_info.bold())

        elif action.text() == "Underline":
            # print('Underline')
            pass

    def action_edit_font(self):
        action = self.sender()
        if action.text() == "Times New Roman":
            print('Times New Roman')

        elif action.text() == "Arial":
            print('Arial')


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
