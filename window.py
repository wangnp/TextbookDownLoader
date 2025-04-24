# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(688, 504)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(8)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.action_mianze = QAction(MainWindow)
        self.action_mianze.setObjectName(u"action_mianze")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.actionYouTube = QAction(MainWindow)
        self.actionYouTube.setObjectName(u"actionYouTube")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background-color: #2780e3;\n"
"	border-radius: 2px;\n"
"	color: white;\n"
"	padding: 8px 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2a8cf4;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	padding: 3px 0px;\n"
"	border: 1px solid #ced4da;\n"
"}\n"
"QLineEdit:hover {\n"
"   /* \u9f20\u6807\u60ac\u505c\u6837\u5f0f */\n"
"   border: 1px solid #2780e3;\n"
"}\n"
"QLineEdit:focus {\n"
"   /* \u83b7\u53d6\u7126\u70b9(\u70b9\u51fb)\u65f6\u7684\u6837\u5f0f */\n"
"   border: 1px solid #2780e3;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.text_book_url = QLineEdit(self.centralwidget)
        self.text_book_url.setObjectName(u"text_book_url")

        self.verticalLayout.addWidget(self.text_book_url)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.text_download_dir = QLineEdit(self.centralwidget)
        self.text_download_dir.setObjectName(u"text_download_dir")

        self.verticalLayout_2.addWidget(self.text_download_dir)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.btn_select_dir = QPushButton(self.centralwidget)
        self.btn_select_dir.setObjectName(u"btn_select_dir")

        self.horizontalLayout.addWidget(self.btn_select_dir)

        self.btn_download = QPushButton(self.centralwidget)
        self.btn_download.setObjectName(u"btn_download")

        self.horizontalLayout.addWidget(self.btn_download)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.label_progress = QLabel(self.centralwidget)
        self.label_progress.setObjectName(u"label_progress")

        self.verticalLayout_4.addWidget(self.label_progress)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.text_log = QTextBrowser(self.groupBox)
        self.text_log.setObjectName(u"text_log")
        self.text_log.setOpenLinks(False)

        self.verticalLayout_3.addWidget(self.text_log)


        self.verticalLayout_4.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 688, 20))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_mianze)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u6559\u6750\u52a9\u624b V1.0", None))
        self.action_mianze.setText(QCoreApplication.translate("MainWindow", u"\u514d\u8d23\u58f0\u660e", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u6211\u4eec", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u4e2d\u5fc3", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u5fae\u4fe1\u516c\u4f17\u53f7\u6587\u7ae0\u6279\u91cf\u4e0b\u8f7d", None))
        self.actionYouTube.setText(QCoreApplication.translate("MainWindow", u"YouTube\u81ea\u52a8\u8bc4\u8bba\u5f15\u6d41\u673a\u5668\u4eba", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6559\u6750\u94fe\u63a5\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u4e0b\u8f7d\u76ee\u5f55\uff1a", None))
        self.btn_select_dir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"  \u4e0b\u8f7d  ", None))
        self.label_progress.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u4e0b\u8f7d", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

