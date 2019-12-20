# created by beyza at 2019-12-1 10:53.
# email : beyzakarali4743@gmail.com


from PyQt5 import QtCore, QtGui, QtWidgets
##COMBOBOXLA SAYFALARI ETKİNLEŞTİR.
##HER SAYFA ETKİNLEŞTİĞİNDE COMBOBOX DURUMUNU DEĞİŞTİRMEYİ UNUTMA
#ANA MENÜ BUTONUNU AKTİFLEŞTİR(passprevwin le ilgili sıkıntı var)



class Ui_Bill(object):
    def __init__(self, prevWin : QtWidgets.QMainWindow = None):
        self.winBill = QtWidgets.QMainWindow()
        self.setupUi(self.winBill)
        self.winBill.show()
        self.prevWin = prevWin

    def passPrevWin(self):##########################################
        self.winBill.close()
        self.prevWin.show()   

    def setupUi(self, Bill):
        Bill.setObjectName("Bill")
        Bill.resize(493, 396)
        Bill.setMinimumSize(QtCore.QSize(493, 396))
        Bill.setMaximumSize(QtCore.QSize(493, 396))
        self.centralwidget = QtWidgets.QWidget(Bill)
        self.centralwidget.setStyleSheet("background-color: rgb(46, 46, 46);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, -20, 511, 341))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 110, 201, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setText("ÖDE")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 10, 391, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setEditable(True)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(50, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(50, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 90, 231, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 0, 391, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 90, 231, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_3.addWidget(self.lineEdit_10)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(60, 0, 391, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setFrame(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(50, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(50, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_2.setToolTipDuration(1)
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 0, 391, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setOpenExternalLinks(False)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.comboBox_5 = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setFrame(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(50, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 90, 231, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_4.addWidget(self.lineEdit_11)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(50, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_2, "")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(380, 330, 101, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.commandLinkButton.setText("ANA MENÜ")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.passPrevWin)
        Bill.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Bill)
        self.statusbar.setObjectName("statusbar")
        Bill.setStatusBar(self.statusbar)

        self.retranslateUi(Bill)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Bill)
        Bill.setTabOrder(self.comboBox, self.lineEdit)
        Bill.setTabOrder(self.lineEdit, self.lineEdit_2)
        Bill.setTabOrder(self.lineEdit_2, self.pushButton)
        Bill.setTabOrder(self.pushButton, self.lineEdit_9)
        Bill.setTabOrder(self.lineEdit_9, self.pushButton_4)
        Bill.setTabOrder(self.pushButton_4, self.lineEdit_5)
        Bill.setTabOrder(self.lineEdit_5, self.pushButton_5)
        Bill.setTabOrder(self.pushButton_5, self.lineEdit_10)
        Bill.setTabOrder(self.lineEdit_10, self.pushButton_6)
        Bill.setTabOrder(self.pushButton_6, self.lineEdit_6)
        Bill.setTabOrder(self.lineEdit_6, self.pushButton_7)
        Bill.setTabOrder(self.pushButton_7, self.lineEdit_11)
        Bill.setTabOrder(self.lineEdit_11, self.pushButton_8)
        Bill.setTabOrder(self.pushButton_8, self.lineEdit_7)
        Bill.setTabOrder(self.lineEdit_7, self.pushButton_9)
        Bill.setTabOrder(self.pushButton_9, self.commandLinkButton)
        Bill.setTabOrder(self.commandLinkButton, self.comboBox_3)
        Bill.setTabOrder(self.comboBox_3, self.comboBox_4)
        Bill.setTabOrder(self.comboBox_4, self.comboBox_5)
        Bill.setTabOrder(self.comboBox_5, self.tabWidget)

    def retranslateUi(self, Bill):
        _translate = QtCore.QCoreApplication.translate
        Bill.setWindowTitle(_translate("Bill", "Fatura Ödeme"))
        self.label.setText(_translate("Bill", "Tel No"))
        self.label_3.setText(_translate("Bill", "Tutar"))
        self.label_2.setText(_translate("Bill", "Kurum Tipini Seçiniz"))
        self.comboBox.setItemText(0, _translate("Bill", "Telefon"))
        self.comboBox.setItemText(1, _translate("Bill", "Su"))
        self.comboBox.setItemText(2, _translate("Bill", "Doğalgaz"))
        self.comboBox.setItemText(3, _translate("Bill", "Elektrik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Bill", "Telefon"))
        self.label_8.setText(_translate("Bill", "Ödenecek Tutar"))
        self.label_12.setText(_translate("Bill", "TC  No"))
        self.pushButton_4.setText(_translate("Bill", "Sorgula"))
        self.pushButton_5.setText(_translate("Bill", "ÖDE"))
        self.label_7.setText(_translate("Bill", "Kurum Tipini Seçiniz"))
        self.comboBox_3.setItemText(0, _translate("Bill", "Telefon"))
        self.comboBox_3.setItemText(1, _translate("Bill", "Su"))
        self.comboBox_3.setItemText(2, _translate("Bill", "Doğalgaz"))
        self.comboBox_3.setItemText(3, _translate("Bill", "Elektrik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Bill", "Su"))
        self.pushButton_6.setText(_translate("Bill", "Sorgula"))
        self.pushButton_7.setText(_translate("Bill", "ÖDE"))
        self.label_9.setText(_translate("Bill", "Kurum Tipini Seçiniz"))
        self.comboBox_4.setItemText(0, _translate("Bill", "Telefon"))
        self.comboBox_4.setItemText(1, _translate("Bill", "Su"))
        self.comboBox_4.setItemText(2, _translate("Bill", "Doğalgaz"))
        self.comboBox_4.setItemText(3, _translate("Bill", "Elektrik"))
        self.label_13.setText(_translate("Bill", "TC  No"))
        self.label_10.setText(_translate("Bill", "Ödenecek Tutar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Bill", "Doğalgaz"))
        self.label_15.setText(_translate("Bill", "Kurum Tipini Seçiniz"))
        self.comboBox_5.setItemText(0, _translate("Bill", "Telefon"))
        self.comboBox_5.setItemText(1, _translate("Bill", "Su"))
        self.comboBox_5.setItemText(2, _translate("Bill", "Doğalgaz"))
        self.comboBox_5.setItemText(3, _translate("Bill", "Elektrik"))
        self.label_11.setText(_translate("Bill", "Ödenecek Tutar"))
        self.pushButton_8.setText(_translate("Bill", "Sorgula"))
        self.pushButton_9.setText(_translate("Bill", "ÖDE"))
        self.label_14.setText(_translate("Bill", "TC  No"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Bill", "Elektrik"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BILL = Ui_Bill()
    sys.exit(app.exec_())
