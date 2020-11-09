import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel("Name:")
        age = QLabel("Age:")
        score = QLabel("Score:")
        amount = QLabel("Amount:")
        key = QLabel("Key:")
        result = QLabel("Result:")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        self.keyEdit = QComboBox()
        self.keyEdit.addItems(["Name", "Age", "Score"])

        self.resultEdit = QTextEdit()

        hbox_a = QHBoxLayout()
        hbox_a.addWidget(name)
        hbox_a.addWidget(self.nameEdit)
        hbox_a.addWidget(age)
        hbox_a.addWidget(self.ageEdit)
        hbox_a.addWidget(score)
        hbox_a.addWidget(self.scoreEdit)

        hbox_b = QHBoxLayout()
        hbox_b.addStretch(1)
        hbox_b.addWidget(amount)
        hbox_b.addWidget(self.amountEdit)
        hbox_b.addWidget(key)
        hbox_b.addWidget(self.keyEdit)

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        hbox_c = QHBoxLayout()
        hbox_c.addStretch(1)
        hbox_c.addWidget(addButton)
        hbox_c.addWidget(delButton)
        hbox_c.addWidget(findButton)
        hbox_c.addWidget(incButton)
        hbox_c.addWidget(showButton)

        hbox_d = QHBoxLayout()
        hbox_d.addWidget(result)
        hbox_d.addStretch(1)

        hbox_e = QHBoxLayout()
        hbox_e.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_a)
        vbox.addLayout(hbox_b)
        vbox.addLayout(hbox_c)
        vbox.addLayout(hbox_d)
        vbox.addLayout(hbox_e)

        showButton.clicked.connect(self.showScoreDB)
        addButton.clicked.connect(self.addScoreDB)
        delButton.clicked.connect(self.delScoreDB)
        findButton.clicked.connect(self.findScoreDB)
        incButton.clicked.connect(self.incScoreDB)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def addScoreDB(self):
        name = str(self.nameEdit.text())
        age = int(self.ageEdit.text())
        score = int(self.scoreEdit.text())
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    def delScoreDB(self):
        name = self.nameEdit.text()
        for p in self.scoredb:
            if name == p['Name']:
                self.scoredb.remove(p)
        self.showScoreDB()

    def findScoreDB(self):
        name = self.nameEdit.text()
        for p in self.scoredb:
            if name == p['Name']:
                keyname = self.keyEdit.currentText()
                for p in sorted(self.scoredb, key=lambda person: person[keyname]):
                    for attr in sorted(p):
                        print(attr + "=" + p[attr], end=' ')
                    print()
        self.showScoreDB()

    def incScoreDB(self):
        name = self.nameEdit.text()
        amount = self.amountEdit.text()
        for p in self.scoredb:
            if name == p['Name']:
                a = int(p['Score'])
                p['Score'] = str(a + int(amount))
        self.showScoreDB()


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
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
        keyname = self.keyEdit.currentText()
        message = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                message += str(attr) + "=" + str(p[attr]) + "       "
            message += '\n'
        self.resultEdit.setPlainText(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())