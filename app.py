from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QFileDialog
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont, QIcon
from amazon_footwear import scrap_footwear
from amazon_clean_data import Clean
from amazon_visualization import Visual
import pandas as pd

class Ui_Form(object):

    def __init__(self):
        self.i = 0
        self.footwear_data = {
                    'Brand': [],
                    'Category': [],
                    'Rating': [],
                    'price': [],
                    'Original_price': [],
                    'Discount': []
                     }

        self.data = pd.DataFrame(self.footwear_data)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1219, 804)
        Form.setFixedSize(1219,804)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./shoes6.png")))
        Form.setPalette(palette)
        Form.setWindowIcon(QIcon('shoes7.png'))

        #Form.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
#"\n"
#"")


        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 510, 1201, 281))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet(
                "background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                "\n"
                "")


        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(950, 140, 241, 46))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(680, 140, 250, 46))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 140, 293, 46))

        font = QtGui.QFont()
        font.setPointSize(21)
        font.setFamily("Algerian")
        self.comboBox.setObjectName("comboBox")

        items = ['shoes','Sandals','Slippers','Loafers','boots','Mules','wedges','Blockheals']

        self.comboBox.addItems(items)
        self.comboBox.setStyleSheet("QListView"
                                     "{"
                                     "background-color: white;"
                                     "}")
        self.comboBox.setFont(font)
        #self.comboBox.setEditable(True)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.export)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.scrap)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(120, 30, 1000, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(370, 460, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 310, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color:rgb(255, 255, 255)")
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(140, 310, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(420, 310, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(575, 310, 280, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 370, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clean_data)

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(880, 302, 325, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("Algerian")
        items = ['Price graph', 'Original price graph', 'Rating graph', 'Discount graph']

        self.comboBox_2.addItems(items)
        self.comboBox_2.setStyleSheet("QListView"
                                    "{"
                                    "background-color: white;"
                                    "}")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")


        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 370, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.visualization)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WEB SCRAPPING OF FOOTWEAR FROM AMAZON"))
        self.label.setText(_translate("Form", "No_of_pages"))
        self.pushButton.setText(_translate("Form", "Export"))
        self.pushButton_2.setText(_translate("Form", "Scrap"))
        self.label_2.setText(_translate("Form", "Category"))
        self.label_4.setText(_translate("Form", "WEB SCRAPPING OF FOOTWEAR FROM AMAZON"))
        self.checkBox.setText(_translate("Form", "price"))
        self.checkBox_2.setText(_translate("Form", "original price"))
        self.checkBox_4.setText(_translate("Form", "save(discount)"))
        self.checkBox_3.setText(_translate("Form", "Rating"))
        self.pushButton_3.setText(_translate("Form", "clean data"))
        self.pushButton_4.setText(_translate("Form", "visualization"))

    def scrap(self):
        scrap_data = scrap_footwear()
        self.category = self.comboBox.currentText()
        no_of_pages = self.spinBox.value()
        self.progressBar.setProperty("value", 0)
        step = 100/no_of_pages


        for page in range(1,no_of_pages+1):

                new_data = scrap_data.scrap(self.category, page)
                self.data = pd.concat([self.data,new_data],ignore_index=True)
                value = self.progressBar.value()
                self.progressBar.setProperty("value", int(value+step))

        if self.progressBar.value() != 100:
            self.progressBar.setProperty("value", 100)

        #self.visual = Visual(self.data)
        self.set_table(self.data)

    def set_table(self,data):


        self.tableWidget.setRowCount(len(data.index))
        self.tableWidget.setColumnCount(len(data.columns))
        self.tableWidget.setHorizontalHeaderLabels(list(data.columns))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        #stylesheet = "::section{Background-color:rgb(0,0,0);color:white;border-radius:8px;}"
        #self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)

        self.tableWidget.horizontalHeader().setFont(QFont("times new roman", 12))
        self.tableWidget.verticalHeader().setFont(QFont("times new roman", 12))
        for row in range(len(data.index)):
            for col in range(len(data.columns)):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data.iloc[row,col])))
                if row % 2 == 0:
                    self.tableWidget.item(row,col).setBackground(QtGui.QColor(190,190,190))
                else:
                    self.tableWidget.item(row, col).setBackground(QtGui.QColor(224, 224, 224))

    def export(self):

        filename = QFileDialog.getSaveFileName(Form,'Save as',self.category,'Excel file (*.xlsx)')
        try:
            self.data.to_excel(filename[0],index=False)

        except Exception as error:
            pass

        self.tableWidget.setRowCount(0)
        self.data = pd.DataFrame(self.footwear_data)

    def clean_data(self):
        clean = Clean()
        self.data_clean = pd.DataFrame({
                    'Brand': [],
                    'Category': []})
        self.data_clean['Brand'] = self.data['Brand']
        self.data_clean['Category'] = self.data['Category']

        if self.checkBox.isChecked():
            self.data_clean['Price'] = clean.price(self.data)
        if self.checkBox_2.isChecked():
            self.data_clean['Original price'] = clean.original_price(self.data)
        if self.checkBox_3.isChecked():
            self.data_clean['Rating'] = clean.rating(self.data)
        if self.checkBox_4.isChecked():
            self.data_clean['Discount'] = clean.save(self.data)

        self.data_clean = self.data_clean.dropna()

        self.set_table(self.data_clean)

    def visualization(self):
        visual = Visual()
        clean = Clean()
        self.data_clean = pd.DataFrame({'Brand': []})

        self.data_clean['Brand'] = self.data['Brand']

        graph = self.comboBox_2.currentText()

        if graph == 'Price graph':
            self.data_clean['Price'] = clean.price(self.data)
            visual.price_graph(self.data_clean)
        elif graph == 'Original price graph':
            self.data_clean['Original_price'] = clean.original_price(self.data)
            visual.original_price_graph(self.data_clean)
        elif graph == 'Rating graph':
            self.data_clean['Rating'] = clean.rating(self.data)
            visual.rating_graph(self.data_clean)
        elif graph == 'Discount graph':
            self.data_clean['Discount'] = clean.save(self.data)
            visual.discount_graph(self.data_clean)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
