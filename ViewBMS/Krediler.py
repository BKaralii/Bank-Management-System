

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Credit(object):
    def __init__(self, prevWin : QtWidgets.QMainWindow = None):
        self.winCredit = QtWidgets.QMainWindow()
        self.setupUi(self.winCredit)
        self.winCredit.show()
        self.prevWin = prevWin

    def passPrevWin(self):
        self.winCredit.close()
        self.prevWin.show()

    def setupUi(self, Credit):
        Credit.setObjectName("Credit")
        Credit.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(Credit)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 35, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(240, 31, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 95, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 170, 141, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 240, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(370, 330, 131, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.passPrevWin)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(260, 90, 101, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(230, 30, 131, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 105, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setGeometry(QtCore.QRect(230, 100, 131, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 170, 101, 51))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 250, 61, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(370, 330, 121, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.passPrevWin)
        self.tabWidget.addTab(self.widget, "")
        Credit.setCentralWidget(self.centralwidget)

        self.retranslateUi(Credit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Credit)
        Credit.setTabOrder(self.tabWidget, self.comboBox)
        Credit.setTabOrder(self.comboBox, self.comboBox_3)
        Credit.setTabOrder(self.comboBox_3, self.pushButton_3)
        Credit.setTabOrder(self.pushButton_3, self.commandLinkButton_2)
        Credit.setTabOrder(self.commandLinkButton_2, self.comboBox_4)
        Credit.setTabOrder(self.comboBox_4, self.comboBox_5)
        Credit.setTabOrder(self.comboBox_5, self.pushButton_4)
        Credit.setTabOrder(self.pushButton_4, self.commandLinkButton)

    def retranslateUi(self, Credit):
        _translate = QtCore.QCoreApplication.translate
        Credit.setWindowTitle(_translate("Credit", "KREDİ İŞLEMLERİ"))
        self.label.setText(_translate("Credit", "Kredi Türü :"))
        self.comboBox.setItemText(0, _translate("Credit", "Seçiniz"))
        self.comboBox.setItemText(1, _translate("Credit", "Teminata Göre"))
        self.comboBox.setItemText(2, _translate("Credit", "Vadesine Göre"))
        self.comboBox.setItemText(3, _translate("Credit", "Kurumsal Krediler"))
        self.label_2.setText(_translate("Credit", "Tutar :"))
        self.label_3.setText(_translate("Credit", "Taksit Seçenekleri :"))
        self.pushButton_3.setText(_translate("Credit", "ÇEK"))
        self.commandLinkButton_2.setText(_translate("Credit", "ANAMENÜ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Credit", "KREDİ ÇEKME"))
        self.label_4.setText(_translate("Credit", "Kredilerim :"))
        self.label_5.setText(_translate("Credit", "Taksit Tarihi :"))
        self.comboBox_5.setItemText(0, _translate("Credit", "Ocak"))
        self.comboBox_5.setItemText(1, _translate("Credit", "Şubat"))
        self.comboBox_5.setItemText(2, _translate("Credit", "Mart"))
        self.comboBox_5.setItemText(3, _translate("Credit", "Nisan"))
        self.comboBox_5.setItemText(4, _translate("Credit", "Mayıs"))
        self.comboBox_5.setItemText(5, _translate("Credit", "Haziran"))
        self.comboBox_5.setItemText(6, _translate("Credit", "Temmuz"))
        self.comboBox_5.setItemText(7, _translate("Credit", "Ağustos"))
        self.comboBox_5.setItemText(8, _translate("Credit", "Eylül"))
        self.comboBox_5.setItemText(9, _translate("Credit", "Ekim"))
        self.comboBox_5.setItemText(10, _translate("Credit", "Kasım"))
        self.comboBox_5.setItemText(11, _translate("Credit", "Aralık"))
        self.label_6.setText(_translate("Credit", "Tutar :"))
        self.pushButton_4.setText(_translate("Credit", "ÖDE"))
        self.commandLinkButton.setText(_translate("Credit", "ANAMENÜ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Credit", "KREDİ ÖDEME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CREDİT = Ui_Credit()
    sys.exit(app.exec_())
