#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                     #
#   software  : GPyFSA     <http://gpyfsa.sourceforge.net/>                           #
#   version   : 0.34                                                                  #
#   date      : 2012-07-15                                                            #
#   licence   : GPLv3.0    <http://www.gnu.org/licenses/>                             #
#   author    : a-Sansara  <http://www.a-sansara.net/>                                #
#   copyright : pluie.org  <http://www.pluie.org/>                                    #
#                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   This file is part of GPyFSA.
#
#   GPyFSA is free software (free as in speech) : you can redistribute it and/or 
#   modify it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   GPyFSA is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with GPyFSA.  If not, see <http://www.gnu.org/licenses/>.

import re, os.path


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class ProbeReader():

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, conf):
        self.conf = conf
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __getListDevices(self):
        sh   = self.conf.getShell()
        ostr = sh.call([sh.CMD_FSA,"probe"]).stderr.read()
        ostr = re.sub(r'\n\n','\n',ostr)
        ostr = re.sub(r'\ ?[\[\ =]','',ostr)
        return ostr.split('\n')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getListDevices(self):
        lines, isDisk, ldev, ldisk, dic, ltmp = self.__getListDevices(), True, [], [], {}, ['','','','',False]
        for l in lines:
            l = l.split(']')
            if isDisk:
                if l[0]=="DISK"  : continue        
                if l[0]=="DEVICE": 
                    isDisk = False
                    continue
                ldisk.append(l[0])
                l = l[0:3]
                l.insert(1,'')
                l.extend(ltmp)
                ldev.append([l,[]])
            elif l:
                if not dic : dic = self.__getDicMountInfo(ldisk)
                idd = -1
                for i in range(len(ldisk)):
                    if l[0].startswith(ldisk[i]):
                        idd = i
                        break
                if idd !=-1:
                    ldevi = l[0:4]
                    if dic.has_key(l[0]): ldevi.extend(dic[l[0]])
                    else : ldevi.extend(ltmp)
                    ldev[idd][1].append(ldevi)

        return ldev

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __getDicMountInfo(self,ldisk):
        dic     = {}
        grepStr = "/\("+"\)\|\(".join(ldisk)+"\)"
        sh      = self.conf.getShell()
        ldev    = sh.getGrepPipeOut([sh.CMD_DF,"-h"],grepStr)
        i       = len("/dev/")
        for l in ldev:
            l = re.sub(r' +','$',l).split('$')
            if l[0]: dic[l[0][i:]]= l[2:]
        ldev = sh.getGrepPipeOut([sh.CMD_MOUNT],grepStr)
        for l in ldev:
            dev = l[5:l.find(' ',5)]
            if dev : dic[dev].append(not l.find('(rw')==-1)
        return dic    

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def traceDevicesList(self,dlist):
        for i in range(len(dlist)):
            print "###############################\n % s (%d)\n###############################" % (dlist[i][self.conf.K_DISK],len(dlist[i][self.conf.K_DEVICE]))
            for j in range(len(dlist[i][self.conf.K_DEVICE])):
                print "%d - %s " % (j,dlist[i][self.conf.K_DEVICE][j])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class LogReader:

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    _READSIZE, _ENDSIZE, _STARTFILE, _ENDFILE, _PERCENTPOS = 400, 400, 0, 2, 9
 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self,pathFile,textview):
        self.textview = textview
        self.path     = pathFile
        if not os.path.isfile(pathFile): 
            f = open(pathFile,'w')
            f.close()
        self.log      = open(pathFile,'r')
        self.buf      = self.textview.get_buffer()
        self.clear()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __readLastLine(self):
        if not self.stopPercent:
            size = os.path.getsize(self.path)
            if self.lastpos < size :
                if size > self._READSIZE : size = self._READSIZE
                self.log.seek(-size,self._ENDFILE)
                l = self.log.read()
                self.pos = self.log.tell()
                l = l.split('\n')
                self.entry = l[len(l)-2]
                hasPercent = self.entry[self._PERCENTPOS:self._PERCENTPOS+1] == "%"           
                if (not self.startPercent) and hasPercent : self.startPercent = hasPercent
                if hasPercent : 
                    self.percent = self.entry[self._PERCENTPOS-3:self._PERCENTPOS].strip()
                    if not self.startPercent: self.startPercent = True
                    self.lastpos = self.pos
                elif self.startPercent: self.stopPercent = True
            else : pass # waiting new entries
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def clear(self,msg=""):
        self.startPercent = self.stopPercent = self.end     = False
        self.pos          = self.bufpos      = self.lastpos = 0        
        self.entry        = self.percent     = ""    
        self.buf.set_text(msg)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def hasPercent(self):
        self.__readLastLine()
        return self.startPercent and not self.stopPercent

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def setVerbooseMode(self,verboose):
        self.verboose = verboose
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def isDone(self):
        return self.startPercent and self.stopPercent

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __readStats(self):
        size = os.path.getsize(self.path)
        self.log.seek(self.lastpos,self._STARTFILE)
        for l in self.log.readlines():
            if not l[self._PERCENTPOS:self._PERCENTPOS+1] == "%" :
                if l.startswith('==='): l = "\n"+l
                self.buf.insert(self.buf.get_end_iter(),l)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def readStats(self):
        self.__readStats()
        self.textview.scroll_to_iter(self.buf.get_end_iter(),0)                

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def read(self):
        if self.verboose and not self.end :
            if(self.pos > self.bufpos):
                self.lastbufpos = self.bufpos
                self.log.seek(self.bufpos,0)
                for l in self.log.readlines():
                    hasPercent = l[self._PERCENTPOS:self._PERCENTPOS+1] == "%"
                    if not self.stopPercent or hasPercent:
                        self.buf.insert(self.buf.get_end_iter(),l)
                        self.textview.scroll_to_iter(self.buf.get_end_iter(),0)
                self.bufpos = self.log.tell()                
        if self.isDone() and not self.end: 
            self.textview.scroll_to_iter(self.buf.get_start_iter(),0)
            self.textview.scroll_to_iter(self.buf.get_end_iter(),0)
            self.end = True

