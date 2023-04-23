import serial
import matplotlib.pyplot as plt
import serial.tools.list_ports
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# from numpy import random
import numpy as np
import serial

from PyQt5 import QtCore, QtWidgets
global portVar 
global working 
portVar = "COM6"
working = True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main screen
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        # Voltage widget
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
        # Styling of Voltage frame
        self.Voltage_label.setStyleSheet(
            "QFrame{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 5px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "font:AlignCenter\n"
            "}"
        )
        self.Voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Voltage_label.setObjectName("Voltage_label")
        self.gridLayout.addWidget(self.Voltage_label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Voltage_frame, 0, QtCore.Qt.AlignTop)
        self.Voltage_graph = QtWidgets.QFrame(self.Voltage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Voltage_graph.sizePolicy().hasHeightForWidth()
        )
        # Defining frame for voltage area graph 
        self.Voltage_graph.setSizePolicy(sizePolicy)
        self.Voltage_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Voltage_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Voltage_graph.setObjectName("Voltage_graph")
        # create canvas
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Voltage_graph)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vgraph = plt.figure()
        self.canvas = FigureCanvas(self.vgraph)
        self.horizontalLayout_3.addWidget(self.canvas)

        self.verticalLayout_2.addWidget(self.Voltage_graph)
        self.Voltage_buttons = QtWidgets.QFrame(self.Voltage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Voltage_buttons.sizePolicy().hasHeightForWidth()
        )
        # Voltage buttons frame
        self.Voltage_buttons.setSizePolicy(sizePolicy)
        self.Voltage_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Voltage_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Voltage_buttons.setObjectName("Voltage_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Voltage_buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Start button
        self.Voltage_start_button = QtWidgets.QPushButton(self.Voltage_buttons, clicked=lambda: self.port_select(working ))
        self.Voltage_start_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 2px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(17, 25, 173);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(16, 147, 199);\n"
            "}"
        )
        self.Voltage_start_button.setObjectName("Voltage_start_button")
        self.horizontalLayout.addWidget(self.Voltage_start_button)
        self.Voltage_stop_button = QtWidgets.QPushButton(self.Voltage_buttons, clicked= lambda:self.stopping(working))   
        # styling voltage start button   
        self.Voltage_stop_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 2px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(17, 25, 173);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(16, 147, 199);\n"
            "}"
        )
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
        self.Current_label.setStyleSheet(
            "QFrame{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 5px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "font:AlignCenter\n"
            "}"
        )
        # Current
        self.Current_label.setAlignment(QtCore.Qt.AlignCenter)
        # Current label
        self.Current_label.setObjectName("Current_label")
        self.gridLayout_2.addWidget(self.Current_label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.Current_frame, 0, QtCore.Qt.AlignTop)
        self.Current_graph = QtWidgets.QFrame(self.Current)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Current_graph.sizePolicy().hasHeightForWidth()
        )
        # current graph
        self.Current_graph.setSizePolicy(sizePolicy)
        self.Current_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Current_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Current_graph.setObjectName("Current_graph")
        self.verticalLayout_3.addWidget(self.Current_graph)
        self.Current_buttons = QtWidgets.QFrame(self.Current)
        self.Current_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Current_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        # current buttons
        self.Current_buttons.setObjectName("Current_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Current_buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Current_start_button = QtWidgets.QPushButton(
            self.Current_buttons, clicked=lambda: self.port_select(working)
        )
        self.Current_start_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 2px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(17, 25, 173);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(16, 147, 199);\n"
            "}"
        )
        self.Current_start_button.setObjectName("Current_start_button")
        self.horizontalLayout_2.addWidget(self.Current_start_button)
        self.current_stop_button = QtWidgets.QPushButton(self.Current_buttons, clicked= lambda:self.stopping(working))
        self.current_stop_button.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(37, 59, 94);\n"
            'border : "2px grey solid";\n'
            "   padding: 2px;\n"
            "  border-radius: 5px;\n"
            ' font: 30 14pt "Candara";\n'
            " color: white;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(17, 25, 173);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(16, 147, 199);\n"
            "}"
        )
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
        self.Voltage_start_button.setText(_translate("MainWindow", "Start"))
        self.Voltage_stop_button.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Voltage), _translate("MainWindow", "Voltage")
        )
        self.Current_label.setText(_translate("MainWindow", "Current"))
        self.Current_start_button.setText(_translate("MainWindow", "Start"))
        self.current_stop_button.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Current), _translate("MainWindow", "Current")
        )

    # stop drawing graph function 
    def stopping(self,working):
        self.working = False

    # start drawing graph function 
    def port_select(self,working):
        serialInst = serial.Serial()
        serialInst.baudrate = 115200
        serialInst.port = portVar
        serialInst.open()
        self.working = True
        k = 100
        x = np.linspace(0, 143, k)
        y = np.zeros((k,))
        i = 0
        while self.working:
            if serialInst.in_waiting:
                data1 = serialInst.readline().decode("utf").rstrip("\n")
                data1 = data1.split()
                data = float(data1[1])
                data = (data / 1024) * 3 - 1.5
                if data1[0] != "Signal":
                    continue
                print(data)
                i = (i + 1) % 100
                y[i] = data
                if i == 99:
                    x += 143
                    y = np.zeros((100,))
                self.vgraph.clear()
                plt.plot(x, y)
                plt.ylabel("Voltage")
                plt.xlabel("Time")
                self.canvas.draw()
                self.vgraph.canvas.flush_events()

if __name__ == "__main__":
    ports=serial.tools.list_ports.comports()
    portsList = []
    for onePort in ports:
        portsList.append(str(onePort))
        print(str(onePort))
    val = input("Select Port: COM")              
    for x in range(0, len(portsList)):
        if portsList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(portVar)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())