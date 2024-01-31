# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Title)

        self.Subtitle = QLabel(self.centralwidget)
        self.Subtitle.setObjectName(u"Subtitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Subtitle.sizePolicy().hasHeightForWidth())
        self.Subtitle.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.Subtitle.setFont(font1)
        self.Subtitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Subtitle)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.link1_title = QLabel(self.centralwidget)
        self.link1_title.setObjectName(u"link1_title")
        sizePolicy.setHeightForWidth(self.link1_title.sizePolicy().hasHeightForWidth())
        self.link1_title.setSizePolicy(sizePolicy)
        self.link1_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.link1_title)

        self.l1a = QSlider(self.centralwidget)
        self.l1a.setObjectName(u"l1a")
        self.l1a.setOrientation(Qt.Horizontal)
        self.l1a.setInvertedAppearance(False)
        self.l1a.setInvertedControls(False)
        self.l1a.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l1a)

        self.l1b = QSlider(self.centralwidget)
        self.l1b.setObjectName(u"l1b")
        self.l1b.setOrientation(Qt.Horizontal)
        self.l1b.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l1b)

        self.l1c = QSlider(self.centralwidget)
        self.l1c.setObjectName(u"l1c")
        self.l1c.setOrientation(Qt.Horizontal)
        self.l1c.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l1c)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.link2_title = QLabel(self.centralwidget)
        self.link2_title.setObjectName(u"link2_title")
        sizePolicy.setHeightForWidth(self.link2_title.sizePolicy().hasHeightForWidth())
        self.link2_title.setSizePolicy(sizePolicy)
        self.link2_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.link2_title)

        self.l2a = QSlider(self.centralwidget)
        self.l2a.setObjectName(u"l2a")
        self.l2a.setOrientation(Qt.Horizontal)
        self.l2a.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l2a)

        self.l2b = QSlider(self.centralwidget)
        self.l2b.setObjectName(u"l2b")
        self.l2b.setOrientation(Qt.Horizontal)
        self.l2b.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l2b)

        self.l2c = QSlider(self.centralwidget)
        self.l2c.setObjectName(u"l2c")
        self.l2c.setOrientation(Qt.Horizontal)
        self.l2c.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_3.addWidget(self.l2c)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Soft Robot Simulation", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Soft Robot Simulation", None))
        self.Subtitle.setText(QCoreApplication.translate("MainWindow", u"Kousheek Chakraborty", None))
        self.link1_title.setText(QCoreApplication.translate("MainWindow", u"Link 1", None))
        self.link2_title.setText(QCoreApplication.translate("MainWindow", u"Link 2", None))
    # retranslateUi

