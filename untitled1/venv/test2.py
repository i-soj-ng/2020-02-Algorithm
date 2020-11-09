import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.keymanual = QComboBox()
        self.combos = ['Name', 'Age', 'Score']
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.initUI()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name: ', self)
        nameline = QLineEdit(self)
        age = QLabel("Age: ", self)
        ageline = QLineEdit(self)
        score = QLabel("Score: ", self)
        scoreline = QLineEdit(self)
        layout1 = QHBoxLayout()
        layout1.addWidget(name)
        layout1.addWidget(nameline)
        layout1.addWidget(age)
        layout1.addWidget(ageline)
        layout1.addWidget(score)
        layout1.addWidget(scoreline)

        amount = QLabel("Amount: ", self)
        amountline = QLineEdit(self)
        key = QLabel("Key: ",self)
        for i in range(len(self.combos)):
            self.keymanual.insertItem(i, self.combos[i])
        layout2 = QHBoxLayout()
        layout2.addStretch(1)
        layout2.addWidget(amount)
        layout2.addWidget(amountline)
        layout2.addWidget(key)
        layout2.addWidget(self.keymanual)
        add = QPushButton("Add",self)
        add.clicked.connect(self.addScoreDB)
        delete = QPushButton("Del",self)
        find = QPushButton("Find",self)
        inc = QPushButton("Inc",self)
        show = QPushButton("Show", self)
        show.clicked.connect(self.showScoreDB)
        layout3 = QHBoxLayout()
        layout3.addStretch(1)
        layout3.addWidget(add)
        layout3.addWidget(delete)
        layout3.addWidget(find)
        layout3.addWidget(inc)
        layout3.addWidget(show)
        result = QLabel("Result :", self)
        self.result_textedit = QTextEdit(self)
        verticalBox = QVBoxLayout()
        verticalBox.addLayout(layout1)
        verticalBox.addLayout(layout2)
        verticalBox.addLayout(layout3)
        verticalBox.addWidget(result)
        verticalBox.addWidget(self.result_textedit)
        self.setLayout(verticalBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()



    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.result_textedit.clear()
        a = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.combos[self.keymanual.currentIndex()]]):
            for msg in sorted(p):
                a += msg + "=" + str(p[msg]) + ' '
                #self.result_textedit.insertPlainText(msg + "=" + str(p[msg]) + ' ')
            a += "\n"
        self.result_textedit.setText(a)

    def addScoreDB(self):
        self.result_textedit.clear()
        record = {'Name': self.nameline.text(), 'Age': int(self.ageline.text()), 'Score': int(self.ageline.text())}
        self.scoredb += [record]
        self.showScoreDB()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())