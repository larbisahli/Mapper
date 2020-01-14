# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HTML_class.ui'
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
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbManagement import *
import img_rc

project = Extract(table_name='Metadata').get_by_name(column='id', name='current_project')[1]
Table(str(project)).create()
var = 0

default = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><meta name="qrichtext" content="1" /><style type="text/css">
        p, li { white-space: pre-wrap; }
        </style></head><body style=" font-family:'Sitka Small'; font-size:12pt; font-weight:400; font-style:normal;">
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; 
        text-indent:0px;"><span style=" font-family:'Courier New'; font-size:10pt; color:#ffff00;">      
        Copy your css here and save</span></p></body></html>"""



def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    try:

        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return f"{round(num)} {x}"
            num /= 1024.0
    except Exception:
        pass


def file_size(file_path):
    """
    this function will return the database file size
    """
    try:
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            return convert_bytes(file_info.st_size)
    except Exception:
        pass


def css_styler(text):
    global head_, body_1, footer

    if len(text) > 0:
        str_ = "".join(text.split())
        pairs = list()
        obj = dict()
        while str_:
            a = str_.index("{")
            head = str_[:a]
            body = str_[a:str_.index("}") + 1]
            str_ = str_.replace(head + body, "")
            result = body.replace("{", "").replace("}", "").split(";")
            for i in result:
                if len(i) > 0:
                    k, v = i.split(":")
                    obj.__setitem__(k, v)
            pairs.append([head, obj])
            obj = dict()

        para = ""

        for pair in pairs:
            p1 = '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; ' \
                 '-qt-block-indent:0; text-indent:0px;"><span style=" font-weight:750; ' \
                 f'color:#ffaa00;">{pair[0]}</span>' \
                 '<span style="font-family:MS Shell Dlg 2;' \
                 ' font-style:italic;  color:#515151;"></span> <span style=" ' \
                 'color:#ffff00; font-weight:550;">{<br></span></p>'

            p2 = ""
            p3 = ""
            for k, v in pair[1].items():
                p = '<p style=" margin-top:0px;  margin-bottom:0px;  margin-left:0px; margin-right:0px; ' \
                    '-qt-block-indent:0; text-indent:0px;"><span style="font-family:MS Shell Dlg 2;' \
                    'font-style:italic;">   </span><span style="font-family:MS Shell Dlg 2; ' \
                    f' font-weight:500; color:#00aaff;"> {k}:</span><span style=" ' \
                    f'font-family:MS Shell Dlg 2; color: rgb(233, 233, 233);">   {v};</span></p>'
                p2 += p

                p3 = '<p style=" margin-top:0px;  margin-bottom:0px;  ' \
                     'margin-left:0px; font-weight:550;   margin-right:0px;  -qt-block-indent:0; ' \
                     'text-indent:0px;"><span style=" color:#ffff00;">}<br></span></p>'

            para += p1 + p2 + p3

        return head_ + body_1 + para + footer

    else:
        return default


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1689, 870)
        Form.setFixedSize(1689, 870)
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
                           "            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),"
                           "  stop:1 rgb(32, 47, 130));\n"
                           "\n"
                           "            height: 0px;\n"
                           "            subcontrol-position: bottom;\n"
                           "            subcontrol-origin: margin;\n"
                           "        }\n"
                           "QScrollBar::sub-line:vertical {\n"
                           "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                           "            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),"
                           "  stop:1 rgb(32, 47, 130));\n"
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
                           "\n"
                           "")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(910, 270, 351, 111))
        self.frame_2.setStyleSheet("background-color: rgb(51, 51, 51);\n"
                                   "border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.create_element_input = QtWidgets.QLineEdit(self.frame_2)
        self.create_element_input.setGeometry(QtCore.QRect(80, 20, 141, 25))
        self.create_element_input.setStyleSheet("\n"
                                                "\n"
                                                "*{\n"
                                                "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                                "color: rgb(0, 0, 0);\n"
                                                "border-radius:5px;\n"
                                                "background-color: rgb(230, 230, 230);\n"
                                                "}\n"
                                                "")
        self.create_element_input.setAlignment(QtCore.Qt.AlignCenter)
        self.create_element_input.setObjectName("create_element_input")
        self.create_name_input = QtWidgets.QLineEdit(self.frame_2)
        self.create_name_input.setGeometry(QtCore.QRect(80, 70, 251, 25))
        self.create_name_input.setStyleSheet("\n"
                                             "\n"
                                             "*{\n"
                                             "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                             "color: rgb(0, 0, 0);\n"
                                             "border-radius:5px;\n"
                                             "background-color: rgb(230, 230, 230);\n"
                                             "}\n"
                                             "")
        self.create_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.create_name_input.setObjectName("create_name_input")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 55, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.comboBox_class_id = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_class_id.setGeometry(QtCore.QRect(230, 20, 101, 25))
        self.comboBox_class_id.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.373134 rgba(255, 255, 255, 255));\n"
            "\n"
            "selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.097, "
            "stop:0.771144 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(81, 81, 81);\n"
            "font: 12pt \"Bahnschrift\";\n"
            "border-radius:10px;")
        self.comboBox_class_id.setFrame(False)
        self.comboBox_class_id.setObjectName("comboBox_class_id")
        self.comboBox_class_id.addItem("")
        self.comboBox_class_id.addItem("")
        self.css_text_edit = QtWidgets.QTextEdit(Form)
        self.css_text_edit.setGeometry(QtCore.QRect(1300, 40, 381, 801))
        self.css_text_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(81, 81, 81);\n"
                                         "font: 12pt \"Sitka Small\";\n"
                                         "")
        self.css_text_edit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.css_text_edit.setObjectName("css_text_edit")
        self.description_text = QtWidgets.QPlainTextEdit(Form)
        self.description_text.setGeometry(QtCore.QRect(890, 480, 391, 361))
        self.description_text.setStyleSheet("color: rgb(233, 233, 233);\n"
                                            "background-color: rgb(81, 81, 81);\n"
                                            "font: 13pt \"Sitka Text\";")
        self.description_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description_text.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.description_text.setDocumentTitle("")
        self.description_text.setBackgroundVisible(False)
        self.description_text.setCenterOnScroll(False)
        self.description_text.setObjectName("description_text")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(1290, 0, 401, 41))
        self.frame_3.setStyleSheet("background-color: rgb(35,35,35);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(40, 4, 301, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Sitka Display\";\n"
                                   "\n"
                                   "")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.save_btn_2 = QtWidgets.QPushButton(self.frame_3)
        self.save_btn_2.setGeometry(QtCore.QRect(350, 6, 31, 31))
        self.save_btn_2.clicked.connect(self.save_css)
        self.save_btn_2.setStyleSheet("\n"
                                      "\n"
                                      "*{\n"
                                      "color: rgb(0, 208, 0);\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 170, 0);\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{ \n"
                                      "border: 1px solid  rgb(35,35,35);\n"
                                      "background-color: rgb(35,35,35);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background:  rgb(55,55,55);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed \n"
                                      "{\n"
                                      " border: 2px inset    rgb(0, 255, 0);\n"
                                      "background-color: #333;\n"
                                      "}")
        self.save_btn_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/images/icons8-save-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.save_btn_2.setIcon(icon1)
        self.save_btn_2.setObjectName("save_btn_2")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(880, 430, 411, 41))
        self.frame_4.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(40, 3, 321, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 14pt \"Sitka Display\";\n"
                                   "\n"
                                   "")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.save_btn_1 = QtWidgets.QPushButton(self.frame_4)
        self.save_btn_1.setGeometry(QtCore.QRect(370, 6, 31, 31))
        self.save_btn_1.setStyleSheet("\n"
                                      "\n"
                                      "*{\n"
                                      "color: rgb(0, 208, 0);\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 170, 0);\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{ \n"
                                      "border: 1px solid  rgb(35,35,35);\n"
                                      "background-color: rgb(35,35,35);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background:  rgb(55,55,55);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed \n"
                                      "{\n"
                                      " border: 2px inset   rgb(0, 255, 0);\n"
                                      "background-color: #333;\n"
                                      "}")
        self.save_btn_1.setText("")
        self.save_btn_1.setIcon(icon1)
        self.save_btn_1.clicked.connect(self.save_description)
        self.save_btn_1.setObjectName("save_btn_1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(1290, 40, 3, 801))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_222 = QtWidgets.QFrame(Form)
        self.line_222.setGeometry(QtCore.QRect(880, 41, 3, 804))
        self.line_222.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_222.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_222.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_222.setObjectName("line_222")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(0, 841, 1691, 30))
        self.frame_5.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_db_size = QtWidgets.QLabel(self.frame_5)
        self.label_db_size.setGeometry(QtCore.QRect(10, 5, 81, 21))
        self.label_db_size.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_db_size.setAlignment(QtCore.Qt.AlignCenter)
        self.label_db_size.setObjectName("label_db_size")
        self.label_tree_tracker = QtWidgets.QLabel(self.frame_5)
        self.label_tree_tracker.setGeometry(QtCore.QRect(110, 6, 1401, 21))
        self.label_tree_tracker.setStyleSheet("color: rgb(255, 170, 0);\n"
                                              "font: 9pt \"NSimSun\";")
        self.label_tree_tracker.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_tree_tracker.setObjectName("label_tree_tracker")
        self.label_total_attr = QtWidgets.QLabel(self.frame_5)
        self.label_total_attr.setGeometry(QtCore.QRect(1520, 2, 161, 25))
        self.label_total_attr.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_total_attr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_attr.setObjectName("label_total_attr")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(910, 50, 351, 71))
        self.frame_6.setStyleSheet("background-color: rgb(51, 51, 51);\n"
                                   "border-radius:15px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 101, 21))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.edit_btn = QtWidgets.QPushButton(self.frame_6)
        self.edit_btn.setGeometry(QtCore.QRect(310, 16, 31, 31))
        self.edit_btn.setStyleSheet("*{\n"
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
                                    "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "\n"
                                    "color: rgb(225, 150, 0);\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "border-radius:15px;\n"
                                    "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed \n"
                                    "{\n"
                                    " border: 2px inset  rgb(0, 255, 0);\n"
                                    "background-color: #333;\n"
                                    "}")
        self.edit_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/icons8-pencil-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edit_btn.setIcon(icon2)
        self.edit_btn.setFlat(True)
        self.edit_btn.clicked.connect(self.change_name)
        self.edit_btn.setObjectName("edit_btn")

        self.change_name_input = QtWidgets.QLineEdit(self.frame_6)
        self.change_name_input.setGeometry(QtCore.QRect(113, 20, 191, 25))
        self.change_name_input.setStyleSheet("\n"
                                             "\n"
                                             "*{\n"
                                             "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                             "color: rgb(0, 0, 0);\n"
                                             "border-radius:5px;\n"
                                             "background-color: rgb(230, 230, 230);\n"
                                             "}\n"
                                             "")
        self.change_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.change_name_input.setObjectName("change_name_input")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(880, 0, 411, 41))
        self.frame_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(35, 35, 35);\n"
                                   "font: 75 14pt \"Sitka Display\";")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.del_btn = QtWidgets.QPushButton(self.frame_7)
        self.del_btn.setGeometry(QtCore.QRect(370, 6, 31, 31))
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
                                   "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "color: rgb(225, 150, 0);\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "border-radius:15px;\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed \n"
                                   "{\n"
                                   " border: 2px inset   rgb(225, 150, 0);\n"
                                   "background-color: #333;\n"
                                   "}")
        self.del_btn.clicked.connect(self.delete)
        self.del_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/images/icons8-waste-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/img/images/icons8-plus-26 _orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.del_btn.setIcon(icon3)
        self.del_btn.setFlat(True)
        self.del_btn.setObjectName("del_btn")
        self.class_display = QtWidgets.QLabel(self.frame_7)
        self.class_display.setGeometry(QtCore.QRect(50, 2, 311, 31))
        self.class_display.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 75 14pt \"Sitka Display\";\n"
                                         "\n"
                                         "")
        self.class_display.setAlignment(QtCore.Qt.AlignCenter)
        self.class_display.setObjectName("class_display")
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 881, 41))
        self.frame_8.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.search_input = QtWidgets.QLineEdit(self.frame_8)
        self.search_input.setGeometry(QtCore.QRect(640, 8, 231, 25))
        self.search_input.setStyleSheet("\n"
                                        "\n"
                                        "*{\n"
                                        "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-radius:5px;\n"
                                        "background-color: rgb(230, 230, 230);\n"
                                        "}\n"
                                        "")
        self.search_input.setAlignment(QtCore.Qt.AlignCenter)
        self.search_input.textEdited.connect(self.search_event)
        self.search_input.setObjectName("search_input")
        self.comboBox_show_me = QtWidgets.QComboBox(self.frame_8)
        self.comboBox_show_me.setGeometry(QtCore.QRect(100, 8, 161, 27))
        self.comboBox_show_me.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.373134 rgba(255, 255, 255, 255));\n"
            "\n"
            "selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, "
            "y2:0.097, stop:0.771144 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(55, 55,55);\n"
            "font: 12pt \"Bahnschrift\";\n"
            "border-radius:10px;")
        self.comboBox_show_me.setFrame(False)
        self.comboBox_show_me.setObjectName("comboBox_show_me")
        self.comboBox_show_me.currentIndexChanged.connect(self.show_me)
        self.comboBox_show_me.addItem("")
        self.comboBox_show_me.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 9pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_8)
        self.label_13.setGeometry(QtCore.QRect(280, 0, 341, 41))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Sitka Display\";\n"
                                    "\n"
                                    "")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tree_display = QtWidgets.QTextEdit(Form)
        self.tree_display.setEnabled(False)
        self.tree_display.setGeometry(QtCore.QRect(10, 50, 611, 791))
        self.tree_display.setStyleSheet("font: 12pt \"Sitka Small\";")
        self.tree_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tree_display.setObjectName("tree_display")
        self.frame_9 = QtWidgets.QFrame(Form)
        self.frame_9.setGeometry(QtCore.QRect(910, 190, 351, 71))
        self.frame_9.setStyleSheet("background-color: rgb(51, 51, 51);\n"
                                   "border-radius:15px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 331, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_display_parent = QtWidgets.QLabel(self.frame_9)
        self.label_display_parent.setGeometry(QtCore.QRect(10, 30, 331, 31))
        self.label_display_parent.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                "font: 75 11pt \"Sitka Display\";\n"
                                                "\n"
                                                "")
        self.label_display_parent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_parent.setObjectName("label_display_parent")
        self.line_1 = QtWidgets.QFrame(Form)
        self.line_1.setGeometry(QtCore.QRect(14, 67, 1, 773))
        self.line_1.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(635, 41, 241, 791))
        self.listWidget.setStyleSheet("QListView {\n"
                                      "    show-decoration-selected: 1;\n"
                                      "    selection-color: white;\n"
                                      "    selection-background-color: rgb(132,88, 0);\n"
                                      "    font: 12pt \"Sitka Small\";\n"
                                      "    color: rgb(226, 151, 0);\n"
                                      "    background: rgb(81, 81, 81);\n"
                                      "  \n"
                                      "}\n"
                                      "\n"
                                      "QListView::item:selected:active:hover{\n"
                                      "    background-color:rgb(211, 211, 211); \n"
                                      "    color: rgb(4, 4, 4);\n"
                                      "border-radius: 15px;"
                                      "}\n"
                                      "QListView::item:selected:active:!hover{\n"
                                      "     background-color: rgb(211, 211, 211); \n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "border-radius: 15px;"
                                      "\n"
                                      "}\n"
                                      "QListView::item:selected:!active{\n"
                                      "    background-color:rgb(224, 219, 219);\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "border-radius: 15px;"
                                      "  \n"
                                      "}\n"
                                      "QListView::item:!selected:hover{\n"
                                      "   background-color:rgb(0, 0, 0); \n"
                                      "   background: qlineargradient(spread:pad, x1:0.423, y1:0.625, x2:0.99005, "
                                      "y2:0.188, stop:0 rgba(124, 119, 119, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "border-radius: 15px;"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical {              \n"
                                      "  border: none;\n"
                                      "  background:rgb(0, 0, 0);\n"
                                      "  width:8px;\n"
                                      "  margin: 0px 0px 0px 0px;\n"
                                      "border-radius: 15px;"
                                      "        }\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                      "stop:0.820896 rgba(200, 117, 17, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "            min-height: 0px;\n"
                                      "border-radius: 15px;"
                                      "        }\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                      "            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  "
                                      "stop:1 rgb(32, 47, 130));\n"
                                      "border-radius: 15px;"
                                      "\n"
                                      "            height: 0px;\n"
                                      "            subcontrol-position: bottom;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "        }\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
                                      "            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  "
                                      "stop:1 rgb(32, 47, 130));\n"
                                      "            height: 0 px;\n"
                                      "            subcontrol-position: top;\n"
                                      "            subcontrol-origin: margin;\n"
                                      "border-radius: 15px;"
                                      "        }\n"
                                      "\n"
                                      "QScrollBar::down-arrow:vertical {\n"
                                      "                        /*image:url(:/images/Images/open-label.png);*/\n"
                                      "                        height: 40px; \n"
                                      "                        width: 40px    "
                                      "                          \n"
                                      "border-radius: 15px;"
                                      "                      }")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget.itemActivated.connect(self.select_name)
        self.listWidget.setObjectName("listWidget")
        self.line_223 = QtWidgets.QFrame(Form)
        self.line_223.setGeometry(QtCore.QRect(630, 40, 3, 804))
        self.line_223.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_223.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_223.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_223.setObjectName("line_223")
        self.frame_10 = QtWidgets.QFrame(Form)
        self.frame_10.setGeometry(QtCore.QRect(880, 140, 411, 41))
        self.frame_10.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(35, 35, 35);\n"
                                    "font: 75 14pt \"Sitka Display\";")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 391, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(970, 390, 231, 31))
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
                                   "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "color: rgb(225, 150, 0);\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "border-radius:15px;\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed \n"
                                   "{\n"
                                   " border: 2px inset   rgb(225, 150, 0);\n"
                                   "background-color: #333;\n"
                                   "}")
        self.add_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/images/icons8-plus-26 _orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_btn.setIcon(icon4)
        self.add_btn.setFlat(True)
        self.add_btn.clicked.connect(self.create_new_attr)
        self.add_btn.setObjectName("add_btn")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # ----------------
        self.list_init()
        Projects(table_name=f"{project}").insert(name="Body", element="null", attr="null", parent="null",
                                                 children="", css="", description="")
        self.last_seen()

    def current_name(self):
        try:
            name = self.class_display.text().split("&quot")[1].split(";")[1]
            if name != "Body (Ancestor)":
                name = name
            else:
                name = name.split(' ')[0]
            return name
        except Exception:
            pass

    def save_last_seen(self):

        name = self.current_name()
        Metadata(_id="last_seen").insert(data=str(name))
        Metadata(_id="last_seen").update(data=str(name))

    def change_name(self):

        update = str(self.change_name_input.text())
        name = self.current_name()
        if len(name) > 0:
            Projects(table_name=f"{project}").update_one(update="name", name=name, data=update)
            self.list_init()
            self.attr_state(name=update)
            self.save_last_seen()

    def delete(self):

        name = self.current_name()
        if len(name) > 0 and name != "Body":
            try:
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle("Mapper")
                box.setWindowIcon(QtGui.QIcon('Images\\icons8-mind-map-26.png'))
                box.setInformativeText(
                    f"\nRemoving {name}.\n\n" +
                    "Are you sure?\n\n")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                box.setDefaultButton(QMessageBox.No)
                buttonYes = box.button(QMessageBox.Yes)
                box.exec_()

                if box.clickedButton() == buttonYes:
                    data = Extract(table_name=f"{project}").get_by_name(column="name", name=name)
                    parent = data[3]
                    data = Extract(table_name=f"{project}").get_by_name(column="name", name=parent)
                    list_ = data[4]
                    if len(list_) > 0:
                        li = eval(list_)
                        if name in li:
                            li.remove(name)
                            Projects(table_name=f"{project}").update_one(update="children", name=parent, data=str(li))

                    all = Extract(table_name=f"{project}").fetchall()

                    delete = [name]

                    for i in all:
                        if i[3] == name:
                            delete.append(i[0])

                    for x in delete:
                        Extract(table_name=f"{project}").delete(name=x)

                    self.list_init()
                    self.attr_state(name="Body")
                    self.save_last_seen()

            except ValueError:
                pass

    def create_new_attr(self):

        element = str(self.create_element_input.text())
        name = str(self.create_name_input.text())
        attr = self.comboBox_class_id.currentText()
        parent = self.current_name()

        if len(name) > 0:
            try:
                Projects(table_name=f"{project}").insert(name=name, element=element, attr=attr, parent=parent,
                                                         children="", css="", description="")
                data = Extract(table_name=f"{project}").get_by_name(column="name", name=parent)
                children = data[4]

                if len(children) == 0:
                    children = list()
                    children.append(name)
                else:
                    children = eval(children)
                    children.append(name)

                Projects(table_name=f"{project}").update_one(update="children", name=parent, data=str(children))

                self.list_init()
                self.attr_state(name=name)

            except Exception:
                pass

    def list_init(self):

        _translate = QtCore.QCoreApplication.translate
        attr = Extract(table_name=f"{project}").select_column(column="name")
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.clear()

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense1Pattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Body (Ancestor)"))

        k = 1
        for i in attr:
            if i != "Body":
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.listWidget.addItem(item)
                item = self.listWidget.item(k)
                item.setText(_translate("Form", f"{i}"))
                k += 1

        self.listWidget.setSortingEnabled(__sortingEnabled)

    def select_name(self, selected_item):

        name = selected_item.text()
        name = name if name != "Body (Ancestor)" else "Body"
        self.attr_state(name=name)
        self.save_last_seen()

    def attr_state(self, *, name):

        data = Extract(table_name=f"{project}").get_by_name(column="name", name=name)
        name, element, attr, parent, children, css, description = data

        _translate = QtCore.QCoreApplication.translate
        if name != "Body":

            self.class_display.setText(_translate("Form",
                                                  "<html><head/><body><p><span style=\" "
                                                  f"font-weight:600; color:#55aaff;\">{attr}=</span>"
                                                  "<span style=\" "
                                                  f"font-weight:400; color:#ffaa00;\">&quot;{name}&quot;</span>"
                                                  "</p></body></html>"))

            self.label_display_parent.setText(_translate("Form",
                                                         "<html><head/><body><p><span style=\" font-weight:600; "
                                                         f"color:#55aaff;\">{attr}=</span><span style=\" "
                                                         "font-weight:400; "
                                                         f"color:#ffaa00;\">&quot;{name}&quot;</span>"
                                                         "</p></body></html>"))

        else:
            self.class_display.setText(_translate("Form",
                                                  '<html><head/><body><p><span style=" font-weight:600; '
                                                  'color:#55aaff;">&quot;Body (Ancestor)&quot;</span>'
                                                  '</p></body></html>'))

            self.label_display_parent.setText(_translate("Form",
                                                         '<html><head/><body><p><span style=" font-weight:600; '
                                                         'color:#55aaff;">Body (Ancestor)</span></p></body></html>'))

        self.description_text.setPlainText(_translate("Form", f"{description}"))

        self.css_text_edit.setHtml(_translate("Form", f"{css_styler(text=css)}"))

        self.label_tree_tracker.setText(_translate("Form", self.tracker(name=name, parent=parent)))

        self.tree_display.setHtml(_translate("Form", self.class_tree(name=name,
                                                                     select= str(self.comboBox_show_me.currentText()),
                                                                     children=children, element=element, attr=attr)))

    def tracker(self, *, name, parent):

        p_list = list()
        if parent != "null":
            while parent != "null":
                if parent != "null":
                    p_list.insert(0, parent)
                data = Extract(table_name=f"{project}").get_by_name(column="name", name=parent)
                parent = data[3]
        head = "<html><head /><body><p>"
        body = ""
        for i in p_list:
            body_ = f'{i} <span style=" font-weight:600; color:#55aaff;">&gt; </span>'
            body += body_
        last_ = f'{name}'
        foot = "</p></body></html>"
        return head + body + last_ + foot

    def search_event(self):

        text = self.search_input.text()
        try:
            if len(text.split()) > 0:
                list_ = Extract(table_name=f"{project}").select_column(column="name")

                _translate = QtCore.QCoreApplication.translate
                self.listWidget.setSortingEnabled(True)
                __sortingEnabled = self.listWidget.isSortingEnabled()
                self.listWidget.setSortingEnabled(False)
                self.listWidget.clear()
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.Dense1Pattern)
                item.setBackground(brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setForeground(brush)
                self.listWidget.addItem(item)
                item = self.listWidget.item(0)
                item.setText(_translate("Form", "Body (Ancestor)"))
                k = 1
                for i in list_:
                    if text in i:
                        if i.rindex(text) == 0:
                            item = QtWidgets.QListWidgetItem()
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.listWidget.addItem(item)
                            item = self.listWidget.item(k)
                            item.setText(_translate("Form", f"{i}"))
                            k += 1
                self.listWidget.setSortingEnabled(__sortingEnabled)
            else:
                self.list_init()
        except Exception:
            pass

    def last_seen(self):

        try:
            name = Extract(table_name="Metadata").get_by_name(column="id", name="last_seen")[1]
        except Exception:
            name = "Body"
        try:
            self.attr_state(name=name)
        except Exception:
            pass

    def save_description(self):
        name = self.current_name()
        text = str(self.description_text.toPlainText())
        Projects(table_name=f"{project}").update_one(update="description", name=name, data=str(text))

    def save_css(self):

        _translate = QtCore.QCoreApplication.translate
        name = self.current_name()
        text = str(self.css_text_edit.toPlainText())
        try:
            self.css_text_edit.setHtml(_translate("Form", f"{css_styler(text=text)}"))
            self.css_text_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(81, 81, 81);\n"
                                             "font: 12pt \"Sitka Small\";\n"
                                             "")
            Projects(table_name=f"{project}").update_one(update="css", name=name, data=str(text))

        except Exception:
            self.css_text_edit.setStyleSheet("color: rgb(255, 0, 0);\n"
                                             "background-color: rgb(55,55, 55);\n"
                                             "font: 12pt \"Sitka Small\";\n"
                                             "")

    def para(self, name, element, attr, space=""):
        return '<p style=" margin-top:6px; margin-bottom: 5px; margin-left:0px; margin-right:0px; ' \
               '-qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\';' \
               f' color:#ffff00;">{space}</span><span style=" font-family:\'MS Shell Dlg 2\'; ' \
               f'color:#55aaff;">&lt;{element if name != "Body" else ""}</span><span style=" ' \
               f'font-family:\'MS Shell Dlg 2\'; ' \
               'color:#00aaff;"> </span><span style=" font-family:\'MS Shell Dlg 2\'; ' \
               f'color:#0099ff;">{attr + "=" if name != "Body" else ""}</span><span style=" ' \
               f'font-family:\'MS Shell Dlg 2\'; ' \
               'color:#55aaff;">&quot;</span><span style=" font-family:\'MS Shell Dlg 2\'; ' \
               f'color:#ffaa00;">{name}</span><span style=" font-family:\'MS Shell Dlg 2\'; ' \
               'color:#55aaff;">&quot;&gt;</span></p>'

    def show_me(self):

        _translate = QtCore.QCoreApplication.translate
        name = self.current_name()
        text = str(self.comboBox_show_me.currentText())
        if len(text) > 0:
            data = Extract(table_name=f"{project}").get_by_name(column="name", name=name)
            self.tree_display.setHtml(_translate("Form", self.class_tree(name=data[0],
                                                                         select=text,
                                                                         children=data[4],
                                                                         element=data[1],
                                                                         attr=data[2])))

    def class_tree(self, name, select, children, element, attr):

        if children != "":
            children = eval(children)
        else:
            children = list()

        class_1 = self.para(name=name, element=element, attr=attr)
        class_2 = ""
        if select == "  Children":

            for child in children:
                data = Extract(table_name=f"{project}").get_by_name(column="name", name=child)
                class_2 += self.para(name=data[0], element=data[1], attr=data[2], space="__")
        elif select == "  Siblings":
            for child in children:
                data = Extract(table_name=f"{project}").get_by_name(column="name", name=child)
                class_2 += self.para(name=data[0], element=data[1], attr=data[2], space="__")

                if len(data[4]) > 0:
                    siblings = eval(data[4])
                    for sibling in siblings:
                        data_ = Extract(table_name=f"{project}").get_by_name(column="name", name=sibling)
                        class_2 += self.para(name=data_[0], element=data_[1], attr=data_[2], space="____")

        return t_head + class_1 + class_2 + t_footer

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(
            _translate("Form", f"{project}"))
        self.label_2.setText(_translate("Form", "Element:"))
        self.label.setText(_translate("Form", "Name:"))
        self.comboBox_class_id.setItemText(0, _translate("Form", "  Class"))
        self.comboBox_class_id.setItemText(1, _translate("Form", "  id"))
        self.label_3.setText(_translate("Form", "CSS"))
        self.label_5.setText(_translate("Form", "description"))
        self.label_db_size.setText(_translate("Form", f"db : {file_size('database.db')}"))
        self.label_tree_tracker.setText(_translate("Form", ""))
        self.label_total_attr.setText(_translate("Form", "Total Attributes :"
                                                         f"  {len(Extract(table_name=f'{project}'))}"))
        self.label_7.setText(_translate("Form", "Change name:"))
        self.search_input.setPlaceholderText(_translate("Form", "Search"))
        self.comboBox_show_me.setItemText(0, _translate("Form", "  Children"))
        self.comboBox_show_me.setItemText(1, _translate("Form", "  Siblings"))
        self.label_12.setText(_translate("Form", "Show me: "))
        self.label_13.setText(_translate("Form", "Class-Tree"))
        self.tree_display.setHtml(_translate("Form", ""))
        self.label_9.setText(_translate("Form", "Select the parent class:"))
        self.label_11.setText(_translate("Form", "Create a new class"))


head_ = """ <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
          <html><head><meta name="qrichtext" content="1" /><style type="text/css">
          p,li {white-space: pre-wrap;}</style></head> """

body_1 = """ <body style=" font-family:'NSimSun'; font-size:11pt; font-weight:400; 
             font-style:normal;"><p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; 
             margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>"""

footer = """ </body></html>"""

# ====================

t_head = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0//EN" 
            "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" 
             content="1" /><style type="text/css">p,li {white-space: pre-wrap;}</style></head>
             <bodystyle=" font-family:'Courier New'; font-size:12pt; font-weight:400; font-style:normal;">
"""

t_footer = """</body></html>"""

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
