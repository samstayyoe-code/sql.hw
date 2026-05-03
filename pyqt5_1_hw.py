from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        top_row = QHBoxLayout()

        self.display = QLineEdit()
        self.display.setText("0")
        self.btn_clear = QPushButton("C")

        top_row.addWidget(self.display)
        top_row.addWidget(self.btn_clear)

        main_layout.addLayout(top_row)

        row1=QHBoxLayout()
        btn7=QPushButton("7")
        btn8=QPushButton("8")
        btn9=QPushButton("9")
        btndiv=QPushButton("/")

        row1.addWidget(btn7)
        row1.addWidget(btn8)
        row1.addWidget(btn9)
        row1.addWidget(btndiv)

        row2 = QHBoxLayout()
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        btn_mul = QPushButton("*")

        row2.addWidget(btn4)
        row2.addWidget(btn5)
        row2.addWidget(btn6)
        row2.addWidget(btn_mul)


        row3 = QHBoxLayout()
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn_sub = QPushButton("-")

        row3.addWidget(btn1)
        row3.addWidget(btn2)
        row3.addWidget(btn3)
        row3.addWidget(btn_sub)

        row4 = QHBoxLayout()
        btn0 = QPushButton(".")
        btn_dot = QPushButton("0")
        btn_eq = QPushButton("=")
        btn_add = QPushButton("+")


        row4.addWidget(btn0)
        row4.addWidget(btn_dot)
        row4.addWidget(btn_eq)
        row4.addWidget(btn_add)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addLayout(row4)

        self.setLayout(main_layout)


        btn7.clicked.connect(lambda: self.press("7"))
        btn8.clicked.connect(lambda: self.press("8"))
        btn9.clicked.connect(lambda: self.press("9"))
        btndiv.clicked.connect(lambda: self.press("/"))

        btn4.clicked.connect(lambda: self.press("4"))
        btn5.clicked.connect(lambda: self.press("5"))
        btn6.clicked.connect(lambda: self.press("6"))
        btn_mul.clicked.connect(lambda: self.press("*"))

        btn1.clicked.connect(lambda: self.press("1"))
        btn2.clicked.connect(lambda: self.press("2"))
        btn3.clicked.connect(lambda: self.press("3"))
        btn_sub.clicked.connect(lambda: self.press("-"))

        btn0.clicked.connect(lambda: self.press("0"))
        btn_dot.clicked.connect(lambda: self.press("."))
        btn_add.clicked.connect(lambda: self.press("+"))

        btn_eq.clicked.connect(self.calculate)
        self.btn_clear.clicked.connect(self.clear_display)


    def press(self, text):
        current = self.display.text()
        if current == "0":
            self.display.setText(text)
        else:
            self.display.setText(current + text)





    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText("Error")


    def clear_display(self):
        self.display.clear()




app = QApplication([])
window = Calculator()
window.show()
app.exec_()
