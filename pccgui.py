import sys
import time
import serial
import numpy as np

from state import State_Initialization
from policy import policy

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import *

from PyQt6.QtCore import QTimer
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTextEdit
)

class sensor(QWidget):
     def __init__(self, name, color):
        super().__init__()
        self.main=QHBoxLayout()
        self.setLayout(self.main)
        self.sensorLabel = QLabel(name)
        self.sensorLabel.setStyleSheet('QLabel {background-color:'+color+';color:black;}')
        self.sensorData = QLineEdit()
        self.sensorData.setReadOnly(True)
        self.main.addWidget(self.sensorLabel)
        self.main.addWidget(self.sensorData)

     def setData(self, sensorData):
        self.sensorData.setText(str(sensorData))



class postureCorrectionChair(QWidget):
    index = []
    ser = serial.Serial('/dev/cu.usbmodem14301')
    s0 = [[] for i in range(6)]
    colorList = ["r","g","b","w","y","m"]
    colorNameList = ["red","green","blue","white","yellow","magenta"]
    
    def readserial(self):
        ser_bytes = self.ser.readline()
        ser_bytes = ser_bytes.decode("utf-8")
        ser_bytes = ser_bytes.rstrip()
        self.index = ser_bytes.split(',')
        print(self.index)

        sumBottom = float(self.index[0]) + float(self.index[1]) + float(self.index[2]) + float(self.index[3])
        sumBack = float(self.index[4]) + float(self.index[5])
        
        for i, s in enumerate(self.sensorList):
            s.setData(str(self.index[i]))

            if i < 4:
                stemp = (float(self.index[i])/float(sumBottom))*100
                s.setData(str(round(stemp, 2))+"%")
                self.s0[i].append(float(stemp))
                l=[0.1*(j+1) for j in range(len(self.s0[i]))]
                pen = pg.mkPen(color=self.colorList[i])
                self.graphWidget.plot(l, self.s0[i],name=f"sensor {i+1}", pen=pen)
            else:
                stemp = (float(self.index[i])/float(sumBack))*100
                s.setData(str(round(stemp, 2))+"%")
                self.s0[i].append(float(stemp))
                l=[0.1*(j+1) for j in range(len(self.s0[i]))]
                pen = pg.mkPen(color=self.colorList[i])
                self.graphWidget.plot(l, self.s0[i],name=f"sensor {i+1}", pen=pen)

            # self.s0[i].append(float(self.index[i]))
            # l=[0.1*(j+1) for j in range(len(self.s0[i]))]
            # pen = pg.mkPen(color=self.colorList[i])
            # self.graphWidget.plot(l, self.s0[i],name=f"sensor {i+1}", pen=pen)
        
        qualityValues = self.checkValues(self.index)
        if qualityValues == True:
            self.actionValue.setText("No one is sitting")
            self.poseValue.setText(" ")
        else:
            sensorDataList = list(map(float, self.index))
            xpos,ypos = State_Initialization(
                sensorDataList[0],
                sensorDataList[1],
                sensorDataList[2],
                sensorDataList[3],
                sensorDataList[4],
                sensorDataList[5]
            )
            if xpos == 1 and ypos == 1:
                self.poseValue.setText("Good Pose")
            else:
                self.poseValue.setText("Bad Pose")

            state = np.zeros([3,3])
            state[xpos][ypos] = 1
            trainedPolicy = np.load("policy.npy")
            sactions="\n".join([action for action in policy(state, trainedPolicy)])
            # for action in policy(state, trainedPolicy):
            #     print(action)
            print(sactions)
            if len(sactions) == 0:
                self.actionValue.setText("Ideal Position")
            else:
                self.actionValue.setText(sactions)
    
    def checkValues(self, sensorVals):
        count = 0
        for ele in sensorVals:
            if ele <= "2" and ele >= "0":
                count = count + 1
        if count == len(sensorVals):
            return True
        else:
            return False
        
    def createGraph(self):
        self.graphWidget.hide()
        del self.graphWidget
        self.graphWidget = pg.PlotWidget()
        self.HorizontalLayout2.addWidget(self.graphWidget)
        self.s0 = [[] for i in range(6)]

    def startReading(self):
        self.timer.start(500)
    
    def Weight_calibration(self, sensorData):
        sensorValues = list(map(float, sensorData))
        S_ideal=sensorValues[0]+sensorValues[1]+sensorValues[2]+sensorValues[3]
        S_backrest=sensorValues[4]+sensorValues[5]
        Calibrate=np.array([S_ideal,S_backrest])
        np.save('Calibrate',Calibrate)

    def startCalibrate(self):

        # while qualityValues == True:
        #     ser_bytes_pre_calib = self.ser.readline()
        #     ser_bytes_pre_calib = ser_bytes_pre_calib.decode("utf-8")
        #     ser_bytes_pre_calib = ser_bytes_pre_calib.rstrip()
        #     print(ser_bytes_pre_calib)
        #     self.index_pre_calib = ser_bytes_pre_calib.split(',')
        #     self.actionValue.setText("please sit in ideal position")
        #     self.poseValue.setText(" ")
        #     qualityValues = self.checkValues(self.index_pre_calib)

        print("start calibration")
        self.actionValue.setText("CALIBRATION IN PROGRESS")
        itr = 0
        while (itr < 11):
            QtCore.QCoreApplication.processEvents()
            ser_bytes = self.ser.readline()
            print(ser_bytes)
            itr = itr + 1
        
        ser_bytes = ser_bytes.decode("utf-8")
        ser_bytes = ser_bytes.rstrip()
        print(ser_bytes)
        self.index = ser_bytes.split(',')
        sumBottom = float(self.index[0]) + float(self.index[1]) + float(self.index[2]) + float(self.index[3])
        sumBack = float(self.index[4]) + float(self.index[5])
        for i, s in enumerate(self.sensorList):
            s.setData(str(self.index[i]))
            if i < 4:
                stemp = (float(self.index[i])/float(sumBottom))*100
                s.setData(str(round(stemp, 2))+"%")  
            else:
                stemp = (float(self.index[i])/float(sumBack))*100
                s.setData(str(round(stemp, 2))+"%")

        print("10th value")
        print(self.index)
        self.Weight_calibration(self.index)
        self.ser.close()
        self.ser.open()
        self.actionValue.setText("DONE CALIBRATION")
        print("end calibration")

    def stopReading(self):
        for i, s in enumerate(self.sensorList):
            s.setData(str(0.0))
        self.actionValue.setText(" ")
        self.poseValue.setText(" ")
        self.timer.stop()
        self.ser.close()
        self.ser.open()
        self.createGraph()
    
    def getActionValue(self):
        if self.flagValue == 1:
            return "START CALIBRATION"
        if self.flagValue == 2:
            return "DONE CALIBRATION"

    def __init__(self):
        super().__init__()
        self.timer=QTimer()
        self.timer.timeout.connect(self.readserial)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.HorizontalLayout1 = QHBoxLayout()
        self.HorizontalLayout2 = QHBoxLayout()
        self.mainLayout.addLayout(self.HorizontalLayout1)
        self.mainLayout.addLayout(self.HorizontalLayout2)

        self.sensorsLayout = QVBoxLayout()
        self.HorizontalLayout1.addLayout(self.sensorsLayout)
        self.sensorList = []
        for i in range(6):
            s=sensor(f"Sensor {i+1}:", self.colorNameList[i])
            self.sensorsLayout.addWidget(s)
            self.sensorList.append(s)
        print(self.index)
        # self.startReading()

        self.buttonLayout = QVBoxLayout()
        self.HorizontalLayout2.addLayout(self.buttonLayout)

        self.buttonCalib = QPushButton("Calibration")
        self.buttonCalib.setStyleSheet(
            'QPushButton {background-color: Aquamarine; color: black;height:30px;width:50px; float:left;}'
            )
        self.buttonCalib.setFixedWidth(100)
        self.buttonCalib.clicked.connect(self.startCalibrate)
        self.buttonLayout.addWidget(self.buttonCalib)

        self.buttonStart = QPushButton("Start")
        self.buttonStart.setStyleSheet(
            'QPushButton {background-color: DarkSeaGreen; color: black;height:30px;width:50px;float:left;}'
            )
        self.buttonStart.setFixedWidth(100)
        self.buttonStart.clicked.connect(self.startReading)
        self.buttonLayout.addWidget(self.buttonStart)

        self.buttonStop = QPushButton("Stop")
        self.buttonStop.setStyleSheet(
            'QPushButton {background-color: FireBrick; color: black;height:30px;width:50px;float:left;}'
            )
        self.buttonStop.setFixedWidth(100)
        self.buttonStop.clicked.connect(self.stopReading)
        self.buttonLayout.addWidget(self.buttonStop)

        self.feedbackLayout = QVBoxLayout()
        self.HorizontalLayout1.addLayout(self.feedbackLayout)

        self.actionLabel = QLabel("Action:")
        self.actionLabel.setFixedHeight(50)
        self.feedbackLayout.addWidget(self.actionLabel)
        self.actionValue = QTextEdit()
        self.actionValue.setFixedHeight(100)
        self.actionValue.setReadOnly(True)
        self.feedbackLayout.addWidget(self.actionValue)
        # self.actionValue.setText(str("Right"))

        self.poseLabel = QLabel("Pose:")
        self.poseLabel.setFixedHeight(50)
        self.feedbackLayout.addWidget(self.poseLabel)
        self.poseValue = QLineEdit()
        self.poseValue.setFixedHeight(50)
        self.poseValue.setReadOnly(True)
        self.feedbackLayout.addWidget(self.poseValue)
        # self.poseValue.setText(str("Good/Bad"))
        
        self.graphWidget = pg.PlotWidget()
        self.HorizontalLayout2.addWidget(self.graphWidget)

        self.ImageLayout = QVBoxLayout()
        pixmap = QPixmap('chair.png')
        pixmapResize = pixmap.scaled(300, 300)
        labelImg = QLabel("")
        labelImg.setPixmap(pixmapResize)
        self.HorizontalLayout1.addLayout(self.ImageLayout)
        self.ImageLayout.addWidget(labelImg)



app = QApplication([])
window = postureCorrectionChair()
window.setFixedWidth(800)
window.setFixedHeight(700)
window.show()
sys.exit(app.exec())

