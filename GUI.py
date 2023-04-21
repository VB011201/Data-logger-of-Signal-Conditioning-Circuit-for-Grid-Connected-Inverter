from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Voltage = QtWidgets.QWidget()
        self.Voltage.setObjectName("Voltage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Voltage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Voltage_frame = QtWidgets.QFrame(self.Voltage)
        self.Voltage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Voltage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Voltage_frame.setObjectName("Voltage_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.Voltage_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Voltage_label = QtWidgets.QLabel(self.Voltage_frame)
        self.Voltage_label.setStyleSheet("QFrame{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 5px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"font:AlignCenter\n"
"}")
        self.Voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Voltage_label.setObjectName("Voltage_label")
        self.gridLayout.addWidget(self.Voltage_label, 0, 0, 1, 1)
        self.Port_selection = QtWidgets.QLabel(self.Voltage_frame)
        self.Port_selection.setStyleSheet("QFrame{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 5px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"font:AlignCenter\n"
"}")
        self.Port_selection.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_selection.setObjectName("Port_selection")
        self.gridLayout.addWidget(self.Port_selection, 0, 1, 1, 1)
        self.DropDownBox = QtWidgets.QComboBox(self.Voltage_frame)
        self.DropDownBox.setObjectName("DropDownBox")
        self.gridLayout.addWidget(self.DropDownBox, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.Voltage_frame, 0, QtCore.Qt.AlignTop)
        self.Voltage_graph = QtWidgets.QFrame(self.Voltage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Voltage_graph.sizePolicy().hasHeightForWidth())
        self.Voltage_graph.setSizePolicy(sizePolicy)
        self.Voltage_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Voltage_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Voltage_graph.setObjectName("Voltage_graph")
        self.verticalLayout_2.addWidget(self.Voltage_graph)
        self.Voltage_buttons = QtWidgets.QFrame(self.Voltage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Voltage_buttons.sizePolicy().hasHeightForWidth())
        self.Voltage_buttons.setSizePolicy(sizePolicy)
        self.Voltage_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Voltage_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Voltage_buttons.setObjectName("Voltage_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Voltage_buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Voltage_start_button = QtWidgets.QPushButton(self.Voltage_buttons)
        self.Voltage_start_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 2px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(17, 25, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(16, 147, 199);\n"
"}")
        self.Voltage_start_button.setObjectName("Voltage_start_button")
        self.horizontalLayout.addWidget(self.Voltage_start_button)
        self.Voltage_stop_button = QtWidgets.QPushButton(self.Voltage_buttons)
        self.Voltage_stop_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 2px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(17, 25, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(16, 147, 199);\n"
"}")
        self.Voltage_stop_button.setObjectName("Voltage_stop_button")
        self.horizontalLayout.addWidget(self.Voltage_stop_button)
        self.verticalLayout_2.addWidget(self.Voltage_buttons, 0, QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.Voltage, "")
        self.Current = QtWidgets.QWidget()
        self.Current.setObjectName("Current")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Current)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Current_frame = QtWidgets.QFrame(self.Current)
        self.Current_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Current_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Current_frame.setObjectName("Current_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Current_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Current_label = QtWidgets.QLabel(self.Current_frame)
        self.Current_label.setStyleSheet("QFrame{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 5px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"font:AlignCenter\n"
"}")
        self.Current_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Current_label.setObjectName("Current_label")
        self.gridLayout_2.addWidget(self.Current_label, 0, 0, 1, 1)
        self.Port_selection_2 = QtWidgets.QLabel(self.Current_frame)
        self.Port_selection_2.setStyleSheet("QFrame{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 5px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"font:AlignCenter\n"
"}")
        self.Port_selection_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_selection_2.setObjectName("Port_selection_2")
        self.gridLayout_2.addWidget(self.Port_selection_2, 0, 1, 1, 1)
        self.DropDownBox_2 = QtWidgets.QComboBox(self.Current_frame)
        self.DropDownBox_2.setObjectName("DropDownBox_2")
        self.gridLayout_2.addWidget(self.DropDownBox_2, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.Current_frame, 0, QtCore.Qt.AlignTop)
        self.Current_graph = QtWidgets.QFrame(self.Current)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Current_graph.sizePolicy().hasHeightForWidth())
        self.Current_graph.setSizePolicy(sizePolicy)
        self.Current_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Current_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Current_graph.setObjectName("Current_graph")
        self.verticalLayout_3.addWidget(self.Current_graph)
        self.Current_buttons = QtWidgets.QFrame(self.Current)
        self.Current_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Current_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Current_buttons.setObjectName("Current_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Current_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Current_start_button = QtWidgets.QPushButton(self.Current_buttons)
        self.Current_start_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 2px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(17, 25, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(16, 147, 199);\n"
"}")
        self.Current_start_button.setObjectName("Current_start_button")
        self.horizontalLayout_2.addWidget(self.Current_start_button)
        self.current_stop_button = QtWidgets.QPushButton(self.Current_buttons)
        self.current_stop_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(37, 59, 94);\n"
"border : \"2px grey solid\";\n"
"   padding: 2px;\n"
"  border-radius: 5px;\n"
" font: 30 14pt \"Candara\";\n"
" color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(17, 25, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(16, 147, 199);\n"
"}")
        self.current_stop_button.setObjectName("current_stop_button")
        self.horizontalLayout_2.addWidget(self.current_stop_button)
        self.verticalLayout_3.addWidget(self.Current_buttons, 0, QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.Current, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Voltage_label.setText(_translate("MainWindow", "Voltage"))
        self.Port_selection.setText(_translate("MainWindow", "Port Selection"))
        self.Voltage_start_button.setText(_translate("MainWindow", "Start"))
        self.Voltage_stop_button.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Voltage), _translate("MainWindow", "Voltage"))
        self.Current_label.setText(_translate("MainWindow", "Current"))
        self.Port_selection_2.setText(_translate("MainWindow", "Port Selection"))
        self.Current_start_button.setText(_translate("MainWindow", "Start"))
        self.current_stop_button.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Current), _translate("MainWindow", "Current"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
