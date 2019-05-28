#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
#Estimating Pi using Buffon's Needle # www.101compiting.net/estimating-pi-using-buffons-needle

import random
from math import sin, cos
import sys
from PySide import QtGui, QtCore
#from PyQt4 import QtGui, QtCore

def check_line_crossing(y, y_end, angle, needleLength, lines_y, omega):
    for line_y in lines_y:
        if y == y_end:
            if y == line_y:
                return True
        if y > y_end:
            if y >= line_y and line_y >= y_end:
                return True
        elif y_end >= line_y and line_y >= y:
                return True
    return False

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):      

        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle('Buffons Pi - PySide (QT) application')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        boardWidth = 40
        needleLength = 30
        numberOfNeedles = 1000

        omega = 2 * 3.141593
        lines_y = range(20, 381, 40)
        Crossing_needles = 0

        #Draw floor boards
        for y in lines_y:
            qp.drawLine(10, y, 490, y)

        #Draw Needles
        for needle in range(numberOfNeedles):
            x=random.randint(60,440)
            y=random.randint(10,390)
            angle=random.randint(0,360)
            # calculate xe and ye with angle
            ye = int(sin(omega * angle / 360) * needleLength + y)
            xe = int(cos(omega * angle / 360) * needleLength + x)
            if check_line_crossing(y, ye, angle,needleLength, lines_y, omega):
                pen = QtGui.QPen(QtCore.Qt.green, 1, QtCore.Qt.SolidLine)
                qp.setPen(pen)
                Crossing_needles += 1
            else:
                pen = QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine)
                qp.setPen(pen)
            qp.drawLine(x, y, xe, ye)

        print("L = " + str(needleLength))
        print("N = " + str(numberOfNeedles))
        print("W = " + str(boardWidth))
        print("C = " + str(Crossing_needles))
        print("Pi = " + str(2.1*needleLength*numberOfNeedles/(Crossing_needles*boardWidth)))

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
