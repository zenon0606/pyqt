from PyQt5.QtWidgets import *
import sys
import hashlib

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)

        #label setting
        self.label = QLabel("<h1>hash_value</h1>", self)
        
        self.textbox = QLineEdit()
        self.textbox.resize(140,20)

        #combobox stting
        self.combobox = QComboBox()
        self.combobox.addItem("md5")
        self.combobox.addItem("sha1")
        self.combobox.addItem("sha224")
        self.combobox.addItem("sha256")
        self.combobox.addItem("sha384")
        self.combobox.addItem("sha512")
        self.combobox.currentTextChanged.connect(self.combobox_changed)
        
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.combobox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('let\'s hash')
        self.show()

    def combobox_changed(self, text):
        #text = self.combobox.currentText()
        #print(text)
        #a = hashlib.md5(b"md5").hexdigest()
        str = "yoshimura hisanori"
        txt = ""
        if text == "md5":
            txt = hashlib.md5(str.encode('utf-8')).hexdigest()
            pass
        elif text == "sha1":
            txt = hashlib.sha1(str.encode('utf-8')).hexdigest()
            pass
        elif text == "sha224":
            txt = hashlib.sha224(str.encode('utf-8')).hexdigest()
            pass
        elif text == "sha256":
            txt = hashlib.sha256(str.encode('utf-8')).hexdigest()
            pass
        elif text == "sha384":
            txt = hashlib.sha384(str.encode('utf-8')).hexdigest()
            pass
        elif text == "sha512":
            txt = hashlib.sha512(str.encode('utf-8')).hexdigest()
            pass

        self.textbox.setText(txt)
        #self.textbox.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	#font setting
	style = '''
		QLabel{
			color: red;
			font-size: 15pt;
		}
		'''
	app.setStyleSheet(style)
	
	window = Window()
	sys.exit(app.exec_())

