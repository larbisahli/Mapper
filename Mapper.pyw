# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.13.2

"""
            ####################################
            #                                  #
            #       Author: Larbi Sahli        #
            #                                  #
            #  https://github.com/larbisahli  #
            #                                  #
            ####################################
"""
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbManagement import *
import img_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 546)
        Form.setFixedSize(310, 546)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/icons8-mind-map-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("*{background-color: rgb(81, 81, 81);}\n"
                           "\n"
                           "\n"
                           "QScrollBar:vertical {              \n"
                           "  border: none;\n"
                           "  background:rgb(0, 0, 0);\n"
                           "  width:8px;\n"
                           "  margin: 0px 0px 0px 0px;\n"
                           "        }\n"
                           "QScrollBar::handle:vertical {\n"
                           "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.820896 rgba(200, "
                           "117, 17, 255), stop:1 rgba(255, 255, 255, 255));\n "
                           "            min-height: 0px;\n"
                           "        }\n"
                           "QScrollBar::add-line:vertical {\n"
                           "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                           "stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n "
                           "\n"
                           "            height: 0px;\n"
                           "            subcontrol-position: bottom;\n"
                           "            subcontrol-origin: margin;\n"
                           "        }\n"
                           "QScrollBar::sub-line:vertical {\n"
                           "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                           "stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n "
                           "            height: 0 px;\n"
                           "            subcontrol-position: top;\n"
                           "            subcontrol-origin: margin;\n"
                           "        }\n"
                           "\n"
                           "QScrollBar::down-arrow:vertical {\n"
                           "                        /*image:url(:/images/Images/open-label.png);*/\n"
                           "                        height: 40px; \n"
                           "                        width: 40px                              \n"
                           "                      }\n"
                           "")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 100, 251, 271))
        self.listWidget.setStyleSheet("QListView {\n"
                                      "    show-decoration-selected: 1;\n"
                                      "    selection-color: white;\n"
                                      "    selection-background-color: rgb(132,88, 0);\n"
                                      "    font: 12pt \"Sitka Small\";\n"
                                      "    \n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "    background: rgb(194, 194, 194);\n"
                                      "  border-radius: 15px\n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:selected:active:hover{\n"
                                      "    background-color:rgb(255, 170, 0); \n"
                                      "    color: rgb(4, 4, 4);\n"
                                      "border-radius: 15px\n"
                                      "}\n"
                                      "QListView::item:selected:active:!hover{\n"
                                      "    background-color:rgb(255, 170, 0); \n"
                                      "    color: rgb(4, 4, 4);\n"
                                      "border-radius: 15px\n"
                                      "\n"
                                      "}\n"
                                      "QListView::item:selected:!active{\n"
                                      "    background-color:rgb(255, 170, 0); \n"
                                      "    color: rgb(4, 4, 4);\n"
                                      "border-radius: 15px\n"
                                      "  \n"
                                      "}\n"
                                      "QListView::item:!selected:hover{\n"
                                      "   \n"
                                      "    background-color: rgb(170, 85, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "border-radius: 15px\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical {              \n"
                                      "  border: none;\n"
                                      "  background:rgb(0, 0, 0);\n"
                                      "  width:8px;\n"
                                      "  margin: 0px 0px 0px 0px;\n"
                                      "border-radius: 15px\n"
                                      "        }\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                      "stop:0.820896 rgba(200, 117, 17, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "            min-height: 0px;\n"
                                      "border-radius: 15px\n"
                                      "        }\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                      "            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  "
                                      "stop:1 rgb(32, 47, 130));\n"
                                      "\n"
                                      "            height: 0px;\n"
                                      "            subcontrol-position: bottom;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "border-radius: 15px\n"
                                      "        }\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                      "            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  "
                                      "stop:1 rgb(32, 47, 130));\n"
                                      "            height: 0 px;\n"
                                      "            subcontrol-position: top;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "border-radius: 15px\n"
                                      "        }\n"
                                      "\n"
                                      "QScrollBar::down-arrow:vertical {\n"
                                      "                        /*image:url(:/images/Images/open-label.png);*/\n"
                                      "                        height: 40px; \n"
                                      "                        width: 40px                              \n"
                                      "                      }")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget.itemActivated.connect(self.active)
        self.listWidget.setObjectName("listWidget")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 251, 51))
        self.label.setStyleSheet("font: 75 14pt \"Sitka Small\";\n"
                                 "\n"
                                 "background-color: rgb(255, 170, 0);\n"
                                 "border-radius: 15px;\n"
                                 "color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(160, 490, 121, 31))
        self.add_btn.setStyleSheet("*{\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "color: rgb(255, 255, 255);\n"
                                   ";\n"
                                   "    \n"
                                   "    background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton{\n"
                                   "border: 1px solid  #333;\n"
                                   "background:  rgb(55, 55, 55);\n"
                                   "border-radius:15px ;\n"
                                   "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "color: rgb(0, 255, 0);\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "border-radius:15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed \n"
                                   "{\n"
                                   " border: 2px inset  rgb(0, 255, 0);\n"
                                   "background-color: #333;\n"
                                   "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/images/icons8-pencil-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_btn.setIcon(icon1)
        self.add_btn.setFlat(True)
        self.add_btn.clicked.connect(self.add)
        self.add_btn.setObjectName("add_btn")
        self.input = QtWidgets.QLineEdit(Form)
        self.input.setGeometry(QtCore.QRect(30, 450, 251, 25))
        self.input.setStyleSheet("\n"
                                 "\n"
                                 "*{\n"
                                 "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius:5px;\n"
                                 "background-color: rgb(230, 230, 230);\n"
                                 "}\n"
                                 "")
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setObjectName("input")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(27, 410, 251, 2))
        self.line.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setGeometry(QtCore.QRect(30, 490, 121, 31))
        self.del_btn.setStyleSheet("*{\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "color: rgb(255, 255, 255);\n"
                                   ";\n"
                                   "    \n"
                                   "    background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton{\n"
                                   "border: 1px solid  #333;\n"
                                   "background:  rgb(55, 55, 55);\n"
                                   "border-radius:15px ;\n"
                                   "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "color: rgb(225, 150, 0);\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "border-radius:15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed \n"
                                   "{\n"
                                   " border: 2px inset   rgb(225, 150, 0);\n"
                                   "background-color: #333;\n"
                                   "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/icons8-waste-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/img/images/icons8-plus-26 _orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.del_btn.setIcon(icon2)
        self.del_btn.setFlat(True)
        self.del_btn.clicked.connect(self.delete)
        self.del_btn.setObjectName("del_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Table("Metadata").create()
        self.list_init()

    def active(self, selected_item):

        try:
            _translate = QtCore.QCoreApplication.translate
            item = selected_item.text()
            Metadata(_id="current_project").insert(data=str(item))
            Metadata(_id="current_project").update(data=str(item))
            from MainWindow import Ui_Form
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()
            time.sleep(2)
            Form.close()
        except Exception:
            pass

    def list_init(self):

        _translate = QtCore.QCoreApplication.translate
        try:
            projects = eval(Extract(table_name="Metadata").get_by_name(column="id", name="projects")[1])
        except TypeError:
            projects = []
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.clear()

        k = 0
        for i in projects:
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.addItem(item)
            item = self.listWidget.item(k)
            item.setText(_translate("Form", f"{i}"))
            k += 1

        self.listWidget.setSortingEnabled(__sortingEnabled)

    def delete(self):
        _translate = QtCore.QCoreApplication.translate
        text = str(self.input.text())
        if len(text) > 0:
            try:
                projects = eval(Extract(table_name="Metadata").get_by_name(column="id", name="projects")[1])
            except TypeError:
                projects = []
            try:
                projects.remove(text)
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle("Mapper")
                box.setWindowIcon(QtGui.QIcon('Images\\icons8-mind-map-26.png'))
                box.setInformativeText(
                    f"\nRemoving the project {text}.\n\n" +
                    "Are you sure?\n\n")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                box.setDefaultButton(QMessageBox.No)
                buttonYes = box.button(QMessageBox.Yes)
                box.exec_()

                if box.clickedButton() == buttonYes:
                    Metadata(_id="projects").update(data=str(projects))
                    self.listWidget.setSortingEnabled(True)
                    __sortingEnabled = self.listWidget.isSortingEnabled()
                    self.listWidget.setSortingEnabled(False)
                    self.listWidget.clear()

                    k = 0
                    for i in projects:
                        item = QtWidgets.QListWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.listWidget.addItem(item)
                        item = self.listWidget.item(k)
                        item.setText(_translate("Form", f"{i}"))
                        k += 1

                    self.listWidget.setSortingEnabled(__sortingEnabled)
                    self.input.setText(_translate("Form", ""))
                else:
                    pass

            except ValueError:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon('Images\\icons8-mind-map-26.png'))
                msg.setIcon(QMessageBox.Warning)
                msg.setText("input-Error")
                msg.setInformativeText(
                    f"\nthere is no such a project called {text}.\n\n")
                msg.setWindowTitle("input-Error")
                msg.exec_()

    def add(self):
        _translate = QtCore.QCoreApplication.translate
        text = str(self.input.text())
        if len(text) > 0:
            
            try:
                projects = eval(Extract(table_name="Metadata").get_by_name(column="id", name="projects")[1])
            except TypeError:
                projects = []
            
            projects.append(text)
            Metadata(_id="projects").insert(data=str(projects))
            Metadata(_id="projects").update(data=str(projects))

            self.listWidget.setSortingEnabled(True)
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            self.listWidget.clear()

            k = 0
            for i in projects:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.listWidget.addItem(item)
                item = self.listWidget.item(k)
                item.setText(_translate("Form", f"{i}"))
                k += 1

            self.listWidget.setSortingEnabled(__sortingEnabled)
            self.input.setText(_translate("Form", ""))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mapper"))

        self.label.setText(_translate("Form", "Projects"))
        self.add_btn.setText(_translate("Form", "add Project"))
        self.input.setPlaceholderText(_translate("Form", "Project name"))
        self.del_btn.setText(_translate("Form", "del Project"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
