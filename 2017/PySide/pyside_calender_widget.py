#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial 

This example shows a QtGui.QCalendarWidget widget.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
update: 5 Okt 2017 by Josef
"""

import sys
import datetime
from PySide import QtGui, QtCore
#from PyQt4 import QtGui, QtCore   # to show compatiblity with PyQt4

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.lbl = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(100, 225)
        
        self.btn = QtGui.QPushButton('Today', self)
        self.btn.move(300, 220)
        self.btn.clicked.connect(self.doAction)

        self.setGeometry(300, 300, 490, 300)
        self.setWindowTitle('Calendar')
        self.show()
        
    def showDate(self, date):     
        self.lbl.setText(date.toString())
        
    def doAction(self):
        self.cal.setSelectedDate(datetime.date.today())
        self.showDate(self.cal.selectedDate())
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
