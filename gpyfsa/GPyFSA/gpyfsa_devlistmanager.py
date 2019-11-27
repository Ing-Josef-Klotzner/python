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

import gtk, os, os.path, pprint
from gpyfsa_fsa import ProbeReader
from gpyfsa_ui  import getNewWidget, insertWidget
from operator   import itemgetter

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
class DevListManager():

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
    dicseldev             = {}
    bseldev               = False
    dcount                = 1

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def evt_refreshDevicesList(self,widget=None):
        self.gpyfsa.doBeforeManageDevices()
        self.gpyfsa['w_treedev'].set_model(self.getTreeStoreDevices(self.gpyfsa['w_treedev'].get_model()))
        self.gpyfsa['w_treedev'].expand_all()
        self.gpyfsa.doAfterManageDevices()
                
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_mountDevice(self, w, name, type, label, prevmountp, mountOpt):
        if mountOpt==None: cmd = ["umount","/dev/"+name]
        else: 
            if type=="ntfs": type = "ntfs-3g"
            if prevmountp == "":
                prevmountp = self.conf.PATH_MOUNT+name
                if not os.path.exists(prevmountp):os.makedirs(prevmountp,0755)
            cmd = ["mount","-o",mountOpt,"-t",type,"/dev/"+name, prevmountp]
        self.conf.getShell().call(cmd,self.gpyfsa.logFile,True)
        self.evt_refreshDevicesList()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_selectDevice(self, widget):
        if not self.bseldev:
            (model, miter) = self.gpyfsa['w_treedev'].get_selection().get_selected()
            path = model.get_path(miter)
            bunsup = model.get_value(miter, self.conf.K_DEV_UNSUP)
            # disk expand
            if len(path)==1 :
                if self.gpyfsa['w_treedev'].row_expanded(path): self.gpyfsa['w_treedev'].collapse_row(path)            
                else : self.gpyfsa['w_treedev'].expand_row(path,True)
            # device selection                
            elif miter != None and not model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_RWRIT)) and not bunsup:
                toggled = model.get_value(miter, self.conf.K_DEV_ACTIVE)
                model.set_value(miter, self.conf.K_DEV_ACTIVE, not toggled)
                self.setDevicesSelection(model.get_value(miter, self.conf.K_DEV),not toggled)
        self.bseldev = False

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def evt_treeviewPressedButton(self, treeview, event):
        bcontinue = False
        if event.button == 3:
            x = int(event.x)
            y = int(event.y)
            time = event.time
            pathinfo = treeview.get_path_at_pos(x, y)
            if pathinfo is not None:
                path, col, cellx, celly = pathinfo
                self.bseldev = True
                #treeview.grab_focus()
                treeview.set_cursor( path, col, 0)
                if(len(path)>1):self.buildDeviceContextMenu(event,path,treeview.get_model())
            bcontinue = True
        return bcontinue

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def buildDeviceContextMenu(self, event, path, model):
        miter  = model.get_iter(path)
        self.gpyfsa.doBeforeManageDevices()
        if miter != None :            
            mountp   = model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_MOUNT))
            dev      = model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_NAME))
            devlabel = model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_LABEL))
            devtype  = model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_TYPE))
            mrw      = model.get_value(miter, self.conf.getClDev(self.conf.K_DEV_RWRIT))
            notSwap  = devtype!="swap"
            entries = [ (self.conf.labelMountDev   % devlabel, bool(notSwap and mountp=="")                , self.evt_mountDevice, "rw" ),
                        (self.conf.labelMountroDev % devlabel, bool(notSwap and mountp=="")                , self.evt_mountDevice, "ro,acl,user_xattr" ),
                        (self.conf.labelRemountDev % devlabel, bool(notSwap and mountp!="/" and mrw)       , self.evt_mountDevice, "remount,ro,acl,user_xattr" ),
                        (self.conf.labelUmountDev  % devlabel, bool(notSwap and mountp!="/" and mountp!=""), self.evt_mountDevice, None )
            ]
            menu = gtk.Menu()
            for label,sensitivity,callback,mountOpt in entries:
                item = gtk.ImageMenuItem(label)
                if callback: item.connect("activate",callback,dev,devtype,devlabel,mountp,mountOpt)
                item.set_sensitive(sensitivity)
                item.show()
                menu.append(item)
            menu.popup(None,None,None,event.button,event.time)     
        self.gpyfsa.doAfterManageDevices()      

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getDeviceOrder(self):
        self.dcount += 1
        return self.dcount

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def setDevicesSelection(self,dev,add):
        if(add):self.dicseldev[dev] = self.getDeviceOrder()
        else: del self.dicseldev[dev]
        self.gpyfsa.doAfterDeviceSelection()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getSortedSelDevList(self):        
        ldev = self.dicseldev.items()
        ldev.sort(key=itemgetter(1),reverse=False)
        return ["/dev/%s" % k for k,v in ldev]
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    def preformatStoreData(self,ldata,activatable,isRoot,imgFileName,active=False,unsupport=False):
        #print(str((active,activatable,unsupport)))
        ldata.insert(0,bool(active and not unsupport))
        ldata.insert(0,bool(activatable and not unsupport))
        ldata.insert(0,not unsupport and not isRoot)
        ldata.insert(0,unsupport)
        ldata.insert(0,isRoot)        
        ldata.insert(0,gtk.gdk.pixbuf_new_from_file(imgFileName))
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    def getTreeStoreDevices(self,oldModel=None):
        #                     ICO             ROOT        UNSUPPORT   SUPPORT     ACTIVATABLE ACTIVE     _K_DEV_                                  NO READ-WRITE      UNSUPPORT
        store = gtk.TreeStore(gtk.gdk.Pixbuf, 'gboolean', 'gboolean', 'gboolean','gboolean','gboolean', str, str, str, str, str, str, str, str, 'gboolean')        
        ldev  = ProbeReader(self.conf).getListDevices()

        for i,l in enumerate(ldev):
            hasntLockedDev = True
            self.preformatStoreData(l[self.conf.K_DISK],False,True,self.conf.IMG_TV_DEVICE)      
            diter = store.append(None,l[self.conf.K_DISK])
            for j,dev in enumerate(l[self.conf.K_DEVICE]):
                imgn = self.conf.IMG_TV_DEVICE
                if dev[self.conf.K_DEV_RWRIT]:                 
                    imgn = self.conf.IMG_TV_DEVICE_LOCKED
                    if hasntLockedDev: store.set_value(diter, self.conf.K_DEV_PIX, gtk.gdk.pixbuf_new_from_file(imgn))
                    hasntLockedDev = False
                active = False
                if(oldModel != None):
                    try:
                        oiter = oldModel.get_iter((i,j))
                        if oiter != None: active = oldModel.get_value(oiter,self.conf.K_DEV_ACTIVE)
                    except :
                        pass
                bunsup = bool(dev[self.conf.K_DEV_TYPE]=="vfat")
                self.preformatStoreData(dev,not dev[self.conf.K_DEV_RWRIT],False,imgn,active,bunsup)
                # inspect later possible wrong length
                
                if bunsup : 
                    #print('dev[14] : '+str(dev[14]))
                    dev[14] = True

                #print(str(dev[:15]))
                store.append(diter,dev[:15])
        return store
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    def buildTreeDevices(self):
        self.gpyfsa['w_treedev'].set_model(self.getTreeStoreDevices())
        crtog = getNewWidget(gtk.CellRendererToggle(),(('activatable',True  ),('active',False)))
        crtxt = getNewWidget(gtk.CellRendererText()  ,(('scale',1.0),('foreground','#6C6C6C'),('background','#D4C8C8')))        
        for i,col in enumerate(self.conf.L_COLSNAME):
            if i == 0:             
                tvcol = gtk.TreeViewColumn(col, gtk.CellRendererPixbuf(), pixbuf=0)
                tvcol.pack_start(gtk.CellRendererPixbuf(),True)
                tvcol.pack_start(crtog,True)
                tvcol.set_attributes(crtog, active=self.conf.K_DEV_ACTIVE, sensitive=self.conf.K_DEV_ACTIVATABLE, visible=self.conf.K_DEV_SUPPORT) 
                tvcol.set_clickable(True)
                insertWidget(self.gpyfsa['w_refresh_devices'],tvcol)
            else :
                tvcol = gtk.TreeViewColumn(col)
                tvcol.pack_start(crtxt,True)
                tvcol.set_attributes(crtxt, text=i+5, background_set=self.conf.K_DEV_UNSUP,foreground_set=self.conf.getClDev(self.conf.K_DEV_RWRIT))  
            self.gpyfsa['w_treedev'].append_column(tvcol)
            
        self.gpyfsa['w_treedev'].set_rules_hint(True)
        self.gpyfsa['w_treedev'].set_enable_search(False)
        self.gpyfsa['w_treedev'].expand_all()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def bindEvents(self):
        self.gpyfsa['w_refresh_devices']._gpyfsa_parent.connect('clicked', self.evt_refreshDevicesList)
        self.gpyfsa['w_treedev'].connect('cursor-changed', self.evt_selectDevice)
        self.gpyfsa['w_treedev'].connect('button-press-event', self.evt_treeviewPressedButton)
               
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, gpyfsa, conf):
        self.gpyfsa = gpyfsa
        self.conf   = conf
        self.buildTreeDevices()
        self.bindEvents()
