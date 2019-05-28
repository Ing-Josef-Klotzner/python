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

import sys

try:
    import pygtk
    pygtk.require("2.0")
except:
    print("You need to install pyGTK 2.0 or set your PYTHONPATH correctly")
    sys.exit(1)
  
import gtk, pango, re #, thread, threading
from time import sleep
from gpyfsa_devlistmanager import DevListManager
from gpyfsa_about import AboutDialog
import gpyfsa_conf as conf
import gpyfsa_ui   as ui
import gpyfsa_fsa  as fsa


#gtk.gdk.threads_init()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
class GPyFSA(gtk.Window):
     
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    def bugFix_GladeComboBoxEntry(self):
        # save tab
        self.w_saveArchiveHistory,combo,browse = gtk.combo_box_entry_new_text(),self.xml.get_widget('w_saveArchiveHistory'),self['w_saveArchiveBrowse']
        self['w_saveArchiveHistory'].set_model(gtk.ListStore(str))
        box = browse.get_parent()
        box.remove(combo)
        box.remove(browse)
        box.pack_start(self['w_saveArchiveHistory'],True,True,0)
        box.pack_start(browse,False,False,0)
        # archive tab
        self.w_infoArchiveHistory,combo1,browse1 = gtk.combo_box_entry_new_text(),self.xml.get_widget('w_infoArchiveHistory'),self['w_infoArchiveBrowse']
        self['w_infoArchiveHistory'].set_model(gtk.ListStore(str))
        box1 = browse1.get_parent()
        box1.remove(combo1)
        box1.remove(browse1)
        box1.pack_start(self['w_infoArchiveHistory'],True,True,0)
        box1.pack_start(browse1,False,False,0)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def cleaningSaveFS(self):
        self.switchControlSaveFS(False)
        ui.clearTimeout(self.timer)
        self.logReader.setVerbooseMode(True)
        self.logReader.readStats()
        self.timer = 0
        if self.pfsa.poll()==0: self['w_nb_savefs'].set_current_page(0)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_aboutDialogActivate(self, widget):
        about = AboutDialog()
        ret = about.run()
        about.destroy()
        return ret

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def checkCleaningSaveFS(self):
        self.endTime+=100
        return self.endTime > self.endSaveFSTime
           
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def terminateSaveFS(self):
        ui.clearTimeout(self.timer)
        self.endTime = 0
        self.endSaveFSTime = 500
        self.timer = ui.setTimeout(100, ui.endSaveFS, self.cleaningSaveFS, self.checkCleaningSaveFS, self['w_progress_savefs'])

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def terminateArchInfos(self):
        ui.clearTimeout(self.timer)
        self.endTime = 0
        buff = self['w_info_log'].get_buffer();
        content = conf.file_get_contents(conf.PATH_LOG)
        buff.set_text(content)


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         
    def switchControlSaveFS(self,active):
        self['w_nb_savefs'].set_show_tabs(True)
        ui.setSensitivity(not active,(self['w_treedev'],self['w_saveArchiveHistory'],self['w_saveArchiveBrowse'],self['w_fsaOpt_c'],self['w_fsaOptValue_c'],self['w_fsaOptValueConfirm_c'],self['w_fsaOpt_c_showpass'],self['l_password'],self['l_confirmPassword'],self['w_fsaOpt_c_noconfirm']))
        self['w_treedev'].set_sensitive(not active)
        self['w_saveArchiveHistory'].set_sensitive(not active)        
        self['w_saveArchiveBrowse'].set_sensitive(not active)       
        sl,hl = l1,l2 = ('w_progress_savefs','w_cancel_savefs'),('w_savefs',)
        if not active: l1,l2 = hl,sl       
        for n in l2: self[n].hide()
        for n in l1: self[n].show()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_cancelSaveFS(self,widget,data=None):
        self.pfsa.terminate()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def evt_browseFile(self,widget,data,callback):
        return ui.browseFile(data[conf.K_TYPE],data[conf.K_TITLE],data[conf.K_FILTER],callback)
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_setArchivePath(self,path):
        self.archivePath = path.rpartition('/')
        if(self.archivePath[2]!=""):conf.chdir(self.archivePath[0])  
        if(self['w_notebook'].get_current_page() == self['w_notebook'].page_num(self['frame_save'])):             
            self['w_saveArchiveHistory'].insert_text(0, path)
            self['w_saveArchiveHistory'].set_active(0)
        elif(self['w_notebook'].get_current_page() == self['w_notebook'].page_num(self['frame_archive'])):
            self['w_infoArchiveHistory'].insert_text(0, path)
            self['w_infoArchiveHistory'].set_active(0)
            self.switchStateArchInfos()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_editComboBoxEntry(self,txt):
        self['w_savefs'].set_sensitive(bool(self.dlm.dicseldev and txt and self.checkPassword(None,None,False)))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_archInfos(self,widget):        
        buff = self['w_info_log'].get_buffer();
        path = self['w_infoArchiveHistory'].get_model().get_value(self['w_infoArchiveHistory'].get_active_iter(),0)
        self.archivePath = path.rpartition('/')
        cmd = ['fsarchiver','archinfo',path]
        if self['w_infopass'].get_active():
            cmd.append('-c'+self['w_infopass_value'].get_text())
        self.logFile.close()
        self.logFile = open(conf.PATH_LOG, 'w')
        self.pfsa = conf.getShell().call(cmd,self.logFile,False)
        self.timer = ui.setTimeout(100, ui.waitTimeout, self.terminateArchInfos, self.checkProgressAborting, (self.logReader,))
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_saveFS(self,widget):
        cmd  = ui.buildFsaOptions(self,conf)
        path = self['w_saveArchiveHistory'].get_model().get_value(self['w_saveArchiveHistory'].get_active_iter(),0)
        self.archivePath = path.rpartition('/')
        filen = path
        if(not path.endswith(".fsa") and self['w_force_ext'].get_active()): 
            if self.archivePath[2]!="":filen = self.archivePath[2]
            filen = re.sub(r'\.[^.]+$',"",filen)+".fsa"
            if self.archivePath[2]!="":path = "".join(self.archivePath[0:1])+"/"+filen     
        self['w_saveArchiveHistory'].get_model().set_value(self['w_saveArchiveHistory'].get_active_iter(), 0, path)
        cmd.append(path)
        cmd.extend(self.dlm.getSortedSelDevList())
        pcmd = list(cmd)
        if self.tmp!=0: 
            pcmd[self.tmp] = "-c"+re.sub(r".","*",pcmd[self.tmp][2:])
        del self.tmp
        self.logReader.clear("\n"+" ".join(pcmd)+"\n\n")
        self.logReader.setVerbooseMode(self['w_fsaOpt_v'].get_active())
        self.timer = ui.setTimeout(100, ui.progressTimeout, self.terminateSaveFS, self.checkProgressAborting, (self.logReader, self['w_progress_savefs'], conf.labelProgressWait, conf.labelWorkInProgress ))
        self.switchControlSaveFS(True)
        self['w_nb_savefs'].set_current_page(1)
        self.logFile.close()
        self.logFile = open(conf.PATH_LOG, 'w')
        self.pfsa = conf.getShell().call(cmd,self.logFile,True)
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def setDefaultArchivePath(self):
        if(hasattr(self,"archivePath") and self.archivePath[2]!=""):conf.chdir(self.archivePath[0])
        else:conf.chdir(conf.PATH_INIT)
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def checkProgressAborting(self): 
        poll   = self.pfsa.poll()
        return poll==0 or poll==1

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def doBeforeManageDevices(self): conf.chdir(conf.PATH_SRC)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def doAfterManageDevices(self): self.setDefaultArchivePath()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def doAfterDeviceSelection(self): self.switchStateSaveFS()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def switchStateSaveFS(self,password=None):
        if password is None : password = self.checkPassword(None,None,False)
        aiter = self['w_saveArchiveHistory'].get_active_iter()
        if(aiter != None): self['w_savefs'].set_sensitive(bool(self.dlm.dicseldev and self['w_saveArchiveHistory'].get_model().get_value(aiter,0) and password))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def switchStateArchInfos(self, data=None):
        password = True
        if self['w_infopass'].get_active():
            pass1 = self['w_infopass_value'].get_text()
            password = bool(len(pass1)>5 and len(pass1)<65)        
        aiter = self['w_infoArchiveHistory'].get_active_iter()
        if(aiter != None): self['w_archinfo'].set_sensitive(bool(self['w_infoArchiveHistory'].get_model().get_value(aiter,0) and password))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    def setCompressionStore(self):
        liststore = gtk.ListStore(int, str)
        for i,name in enumerate (conf.COMPRESSION_LEVEL):liststore.append([i+1,str(i+1)+': '+name])        
        crt = gtk.CellRendererText()
        crt.set_property('family','Liberation mono')
        self['w_fsaOpt_z'].set_model(liststore)
        self['w_fsaOpt_z'].pack_start(crt, True)
        self['w_fsaOpt_z'].add_attribute(crt, 'text', 1)
        self['w_fsaOpt_z'].set_active(2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
    def manageStyle(self):
        self['w_log'].modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse('#2E3436'))
        self['w_log'].modify_text(gtk.STATE_NORMAL,gtk.gdk.color_parse('#FFF7BA'))
        self['w_log'].modify_font(pango.FontDescription("Liberation mono normal 10"))
        self['w_info_log'].modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse('#2E3436'))
        self['w_info_log'].modify_text(gtk.STATE_NORMAL,gtk.gdk.color_parse('#FFF7BA'))
        self['w_info_log'].modify_font(pango.FontDescription("Liberation mono normal 10"))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def checkPassword(self,widget=None,data=None,testRefresh=True):
        bvalid, stockid, pass1, pass2 = not self['w_fsaOpt_c'].get_active(), gtk.STOCK_NO, self['w_fsaOptValue_c'].get_text(), self['w_fsaOptValueConfirm_c'].get_text()
        self['w_validPassword'].set_sensitive(not bvalid)
        if not bvalid and len(pass1)>5 and len(pass1)<65 and (self['w_fsaOpt_c_noconfirm'].get_active() or pass1==pass2):
            stockid = gtk.STOCK_YES 
            bvalid = True
        self['w_validPassword'].set_from_stock(stockid, gtk.ICON_SIZE_BUTTON)
        if(testRefresh): self.switchStateSaveFS(bvalid)
        return bvalid

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def bindEvents(self): 
        for opt in conf.SAVEOPT :
            if opt[conf.K_NAME] == 'e' or opt[conf.K_NAME] == 's' :
                self['w_fsaOpt_'+opt[conf.K_NAME]].connect("toggled", ui.setSensitivity, self['w_fsaOptValue_'+opt[conf.K_NAME]])
            if opt[conf.K_NAME] == 'c' :
                self['w_fsaOpt_c'].connect("toggled", ui.setSensitivity, (self['w_fsaOptValue_c'],self['w_fsaOptValueConfirm_c'],self['w_fsaOpt_c_showpass'],self['l_password'],self['l_confirmPassword'],self['w_fsaOpt_c_noconfirm']))                                                                                           
                self['w_fsaOpt_c_showpass' ].connect("toggled", ui.setInvisibleChar, (self['w_fsaOptValue_c'],self['w_fsaOptValueConfirm_c']) )
                self['w_fsaOpt_c_showpass' ].connect("toggled", lambda w : self['w_fsaOpt_c_noconfirm'].set_active(w.get_active()) )                                   
                self['w_fsaOpt_c_noconfirm'].connect("toggled", ui.setInvisibility  , (self['w_fsaOptValueConfirm_c'],self['l_confirmPassword']) )
                self['w_fsaOpt_c'].connect("toggled", self.checkPassword)
                self['w_fsaOpt_c_showpass' ].connect("toggled", self.checkPassword)
                self['w_fsaOpt_c_noconfirm'].connect("toggled", self.checkPassword)
                self['w_fsaOptValue_c'].connect("changed", self.checkPassword)                
                self['w_fsaOptValueConfirm_c'].connect("changed", self.checkPassword)
        self['w_saveArchiveHistory'].child.connect('changed', ui.onEditComboBoxEntry, self.evt_editComboBoxEntry)
        self['w_saveArchiveBrowse'].connect("clicked", self.evt_browseFile, conf.CBDT_SAVEFS, self.evt_setArchivePath)
        self['w_savefs'].connect('clicked', self.evt_saveFS)
        self['w_cancel_savefs'].connect('clicked', self.evt_cancelSaveFS)        
        self['gpyfsa'].connect("delete_event", gtk.main_quit)
        dic = {"on_aboutDialog_activate" : self.evt_aboutDialogActivate }
        self.xml.signal_autoconnect(dic)
        self['w_infoArchiveBrowse'].connect("clicked", self.evt_browseFile, conf.CBDT_ARCHFS, self.evt_setArchivePath)
        self['w_infopass'].connect("toggled", ui.setSensitivity  , (self['w_infopass_value']))
        self['w_infopass'].connect("toggled", self.switchStateArchInfos )
        self['w_archinfo'].connect('clicked', self.evt_archInfos)
        self['w_infopass_value'].connect("changed", self.switchStateArchInfos)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __getitem__(self, key):
        # # # # > BUG FIX ! see bugFix_GladeComboBoxEntry() # # # #
        if key == 'w_saveArchiveHistory' : return self.w_saveArchiveHistory
        if key == 'w_infoArchiveHistory': return self.w_infoArchiveHistory
        # # # # < BUG FIX # # # # # # # # # # # # # # # # # # # # #
        return self.xml.get_widget(key)
                
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self): 
        self.xml = conf.getGladeXML()
        self.dlm = DevListManager(self,conf)
        self.bugFix_GladeComboBoxEntry()        
        self.setCompressionStore()        
        self.manageStyle()
        self.bindEvents()
        self.logReader = fsa.LogReader(conf.PATH_LOG,self['w_log'])
        self.logFile   = open(conf.PATH_LOG, 'w')
        self[conf.APP_NAME].show_all()
        conf.chdir(conf.PATH_INIT)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def main():
    GPyFSA()
    gtk.window_set_default_icon_list(gtk.gdk.pixbuf_new_from_file(conf.SCALABLE_ICON))
    gtk.main()
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    main()

# xgettext --language=Python --keyword=_ --keyword=N_ --output=gpyfsa.pot  res/gpyfsa.glade.h src/*.py
# msginit -i gpyfsa.pot -o locale/fr/LC_MESSAGES/gpyfsa.po
# msgfmt gpyfsa.po -o gpyfsa.mo
# intltool-extract --type=gettext/glade res/*.glade
# msgmerge -U locale/fr/LC_MESSAGES/gpyfsa.po gpyfsa.pot
