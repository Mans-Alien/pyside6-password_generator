# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 212)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #205BD4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_password = QLineEdit(self.centralwidget)
        self.line_password.setObjectName(u"line_password")

        self.horizontalLayout.addWidget(self.line_password)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        icon = QIcon()
        icon.addFile(u":/icon/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copy.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_length)

        self.spin_length = QSpinBox(self.centralwidget)
        self.spin_length.setObjectName(u"spin_length")
        self.spin_length.setAlignment(Qt.AlignCenter)
        self.spin_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_length.setMaximum(100)
        self.spin_length.setSingleStep(0)
        self.spin_length.setValue(12)

        self.horizontalLayout_2.addWidget(self.spin_length)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_digits)

        self.btn_simbols = QPushButton(self.centralwidget)
        self.btn_simbols.setObjectName(u"btn_simbols")
        self.btn_simbols.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_simbols)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_simbols.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

