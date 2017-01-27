# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 762)
        self.mainLayout = QtGui.QWidget(MainWindow)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainLayout)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.traceLayout = QtGui.QVBoxLayout()
        self.traceLayout.setSpacing(1)
        self.traceLayout.setObjectName(_fromUtf8("traceLayout"))
        self.timeWidget = TimeWidget(self.mainLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeWidget.sizePolicy().hasHeightForWidth())
        self.timeWidget.setSizePolicy(sizePolicy)
        self.timeWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.timeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.timeWidget.setObjectName(_fromUtf8("timeWidget"))
        self.traceLayout.addWidget(self.timeWidget)
        self.verticalLayout_2.addLayout(self.traceLayout)
        MainWindow.setCentralWidget(self.mainLayout)
        self.textOutDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutDock.sizePolicy().hasHeightForWidth())
        self.textOutDock.setSizePolicy(sizePolicy)
        self.textOutDock.setMinimumSize(QtCore.QSize(290, 147))
        self.textOutDock.setMaximumSize(QtCore.QSize(524287, 52487))
        self.textOutDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.textOutDock.setObjectName(_fromUtf8("textOutDock"))
        self.textOutLayout = QtGui.QWidget()
        self.textOutLayout.setObjectName(_fromUtf8("textOutLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.textOutLayout)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textOutBrowser = QtGui.QTextBrowser(self.textOutLayout)
        self.textOutBrowser.setObjectName(_fromUtf8("textOutBrowser"))
        self.verticalLayout_4.addWidget(self.textOutBrowser)
        self.strollingLabel = QtGui.QLabel(self.textOutLayout)
        self.strollingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.strollingLabel.setObjectName(_fromUtf8("strollingLabel"))
        self.verticalLayout_4.addWidget(self.strollingLabel)
        self.strollComboBox = QtGui.QComboBox(self.textOutLayout)
        self.strollComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.strollComboBox.setObjectName(_fromUtf8("strollComboBox"))
        self.verticalLayout_4.addWidget(self.strollComboBox)
        self.textOutDock.setWidget(self.textOutLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.textOutDock)
        self.archiveDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveDock.sizePolicy().hasHeightForWidth())
        self.archiveDock.setSizePolicy(sizePolicy)
        self.archiveDock.setMinimumSize(QtCore.QSize(383, 150))
        self.archiveDock.setMaximumSize(QtCore.QSize(524287, 150))
        self.archiveDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.archiveDock.setObjectName(_fromUtf8("archiveDock"))
        self.archiveLayout = QtGui.QWidget()
        self.archiveLayout.setObjectName(_fromUtf8("archiveLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.archiveLayout)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.archiveLeftLayout = QtGui.QVBoxLayout()
        self.archiveLeftLayout.setObjectName(_fromUtf8("archiveLeftLayout"))
        self.archiveList = ArchiveListWidget(self.archiveLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveList.sizePolicy().hasHeightForWidth())
        self.archiveList.setSizePolicy(sizePolicy)
        self.archiveList.setMinimumSize(QtCore.QSize(290, 0))
        self.archiveList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.archiveList.setObjectName(_fromUtf8("archiveList"))
        self.archiveLeftLayout.addWidget(self.archiveList)
        self.horizontalLayout.addLayout(self.archiveLeftLayout)
        self.archiveRightLayout = QtGui.QVBoxLayout()
        self.archiveRightLayout.setSpacing(1)
        self.archiveRightLayout.setObjectName(_fromUtf8("archiveRightLayout"))
        self.archiveSpan = ArchiveSpanWidget(self.archiveLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpan.sizePolicy().hasHeightForWidth())
        self.archiveSpan.setSizePolicy(sizePolicy)
        self.archiveSpan.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveSpan.setMaximumSize(QtCore.QSize(16777215, 200))
        self.archiveSpan.setObjectName(_fromUtf8("archiveSpan"))
        self.archiveRightLayout.addWidget(self.archiveSpan)
        self.archiveEvent = ArchiveEventWidget(self.archiveLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveEvent.sizePolicy().hasHeightForWidth())
        self.archiveEvent.setSizePolicy(sizePolicy)
        self.archiveEvent.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveEvent.setMaximumSize(QtCore.QSize(16777215, 200))
        self.archiveEvent.setObjectName(_fromUtf8("archiveEvent"))
        self.archiveRightLayout.addWidget(self.archiveEvent)
        self.archiveTextLayout = QtGui.QHBoxLayout()
        self.archiveTextLayout.setSpacing(0)
        self.archiveTextLayout.setObjectName(_fromUtf8("archiveTextLayout"))
        self.archiveSpanT0Label = DblClickLabelWidget(self.archiveLayout)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT0Label.setFont(font)
        self.archiveSpanT0Label.setText(_fromUtf8(""))
        self.archiveSpanT0Label.setObjectName(_fromUtf8("archiveSpanT0Label"))
        self.archiveTextLayout.addWidget(self.archiveSpanT0Label)
        self.archiveSpanT1Label = DblClickLabelWidget(self.archiveLayout)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT1Label.setFont(font)
        self.archiveSpanT1Label.setText(_fromUtf8(""))
        self.archiveSpanT1Label.setObjectName(_fromUtf8("archiveSpanT1Label"))
        self.archiveTextLayout.addWidget(self.archiveSpanT1Label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.archiveTextLayout.addItem(spacerItem)
        self.archiveRightLayout.addLayout(self.archiveTextLayout)
        self.archiveRightLayout.setStretch(0, 5)
        self.archiveRightLayout.setStretch(1, 3)
        self.horizontalLayout.addLayout(self.archiveRightLayout)
        self.archiveDock.setWidget(self.archiveLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.archiveDock)
        self.mapDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapDock.sizePolicy().hasHeightForWidth())
        self.mapDock.setSizePolicy(sizePolicy)
        self.mapDock.setMinimumSize(QtCore.QSize(290, 125))
        self.mapDock.setMaximumSize(QtCore.QSize(524287, 52487))
        self.mapDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.mapDock.setObjectName(_fromUtf8("mapDock"))
        self.mayLayout = QtGui.QWidget()
        self.mayLayout.setObjectName(_fromUtf8("mayLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.mayLayout)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.mapWidget = QtGui.QGraphicsView(self.mayLayout)
        self.mapWidget.setObjectName(_fromUtf8("mapWidget"))
        self.verticalLayout_6.addWidget(self.mapWidget)
        self.mapDock.setWidget(self.mayLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mapDock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lazylyst", None))
        self.textOutDock.setWindowTitle(_translate("MainWindow", "Standard Out", None))
        self.strollingLabel.setText(_translate("MainWindow", "Strolling Actions (0)", None))
        self.archiveDock.setWindowTitle(_translate("MainWindow", "Archive", None))
        self.mapDock.setWindowTitle(_translate("MainWindow", "Map View", None))

from CustomWidgets import ArchiveEventWidget, ArchiveListWidget, ArchiveSpanWidget, DblClickLabelWidget, TimeWidget
