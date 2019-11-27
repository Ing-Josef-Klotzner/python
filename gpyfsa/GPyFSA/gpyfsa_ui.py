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

import gtk, gobject, re

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def setSensitivity(checkBoxOrBool,target):
    if type(checkBoxOrBool)==bool:active = checkBoxOrBool
    else : active = checkBoxOrBool.get_active()
    if(type(target) != tuple): target = (target,)
    for w in target : w.set_sensitive(active)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
def setVisibility(widget,hide=False):
    if hide: widget.hide_all()
    else: widget.show_all()    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
def setInvisibility(widget,target):
    active = widget.get_active()
    if(type(target) != tuple): target = (target,)
    for w in target : setVisibility(w,active)
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
def setInvisibleChar(widget,target):
    active = widget.get_active()
    if(type(target) != tuple): target = (target,)
    for w in target : w.set_visibility(active)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def onEditComboBoxEntry(entry, callback=None):
    combo = entry.get_parent()
    index = combo.get_active()
    if(index > -1):
        combo._activeIndex = index
        combo._activeIter  = combo.get_active_iter()
    elif not hasattr(combo,"_activeIter"):
        combo._activeIndex = 0                    
        combo._activeIter  = (combo.get_model()).insert_after(None,None)        
    (combo.get_model()).set_value(combo._activeIter, 0, entry.get_text())
    combo.set_active(combo._activeIndex)
    if(callback != None):callback(entry.get_text())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def browseFile(typeBrowse,title="",filterList=None,callback=None):
    dialog = gtk.FileChooserDialog(title   = title,
                                   action  = eval('gtk.FILE_CHOOSER_ACTION_'+typeBrowse),
                                   buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, eval('gtk.STOCK_'+typeBrowse), gtk.RESPONSE_OK))
    if(filterList!=None):
        _K_FILTER_NAME,_K_FILTER_PATTERN = 0,1
        for elmt in filterList:
            f = gtk.FileFilter()
            f.set_name(elmt[_K_FILTER_NAME])
            f.add_pattern(elmt[_K_FILTER_PATTERN])
            dialog.add_filter(f)
    if dialog.run() == gtk.RESPONSE_OK and callback!=None: callback(dialog.get_filename())
    dialog.destroy()
    return

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def getNewWidget(widget,propList):
    for i,prop in enumerate(propList):widget.set_property(prop[0],prop[1])
    return widget

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
def insertWidget(widget,wp=None,add=False):
    w = widget
    widget.get_parent().remove(widget)
    w.unparent()
    if wp!=None:
        if not add: wp.set_widget(w)
        else: wp.add(w)
        w._gpyfsa_parent = wp
    return

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def buildFsaOptions(gpyfsa,conf):
    cmd = ['fsarchiver', 'savefs']
    gpyfsa.tmp = 0
    for opt in conf.SAVEOPT :
        noAdd  = False
        v, wname, applyMethod  = '','w_fsaOpt_'+opt[conf.K_NAME], None
        if isinstance(gpyfsa[wname], gtk.CheckButton): noAdd = not gpyfsa[wname].get_active()
        if opt[conf.K_NAME]=="v": noAdd = False       
        if not noAdd and not opt[conf.K_NOVAL]:
            if not opt[conf.K_SELFVAL]: wname = 'w_fsaOptValue_'+opt[conf.K_NAME]
            v = getWidgetValue(gpyfsa[wname],applyMethod)
            if opt[conf.K_NAME]=="c": gpyfsa.tmp = len(cmd)            
            if not noAdd : noAdd = v.strip() == ''               
        if not noAdd : cmd.append('-'+opt[conf.K_NAME]+v)
    print(str(cmd))
    return cmd

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def getWidgetValue(widget,applyMethod):
    value = ''
    if   isinstance(widget, gtk.Entry)     : value = widget.get_text()  
    elif isinstance(widget, gtk.SpinButton): value = str(int(widget.get_value()))
    elif isinstance(widget, gtk.ComboBox)  : value = str(widget.get_model().get_value(widget.get_active_iter(),0))          
    if applyMethod is not None: value = applyMethod(value)
    return value

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def formatDoubleQuote(value):
    #value = re.sub(r"'","\\'",value)
    if(value.rfind('"')!=-1): value = re.sub(r'"','\\"',value)
    return '"'+value+'"'
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def progressTimeout(callBack, clearCallback, fsaLogReader, progressbar, msgWait="", msgInProgress=""):
    progress, txt, pulse, fraction = not clearCallback(), msgWait, True, 0.0
    if fsaLogReader.hasPercent() : txt, pulse, fraction = msgInProgress+fsaLogReader.percent+"%", False, float(fsaLogReader.percent)/100.0
    fsaLogReader.read()
    progressbar.set_text(txt)    
    if pulse        : progressbar.pulse()
    else            : progressbar.set_fraction(fraction)
    if not progress : callBack()    
    return progress

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def waitTimeout(callBack, clearCallback, fsaLogReader):
    progress = not clearCallback()
    if not progress : callBack()    
    return progress

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def endArchInfos(callBack,clearCallback):
    bnotclear = not clearCallback()     
    if(bnotclear):callBack()
    return bnotclear

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def endSaveFS(callBack,clearCallback,progressbar):
    progressbar.pulse()
    bnotclear = not clearCallback()     
    if(bnotclear):callBack()
    return bnotclear

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def clearTimeout(timer):
    gobject.source_remove(timer)
    timer = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def setTimeout(ms, bind, callback, clearCallback, data=None):
    params = ""
    if data is not None :
        if(type(data) != tuple): data = (data,)
        for i in range(len(data)): params += ", data["+str(i)+"]"
    return eval("gobject.timeout_add(ms, bind, callback, clearCallback "+params+")")
