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

import sys, os, os.path, locale, gettext, gtk.glade
from gpyfsa_shell import Shell

def get_path(default, destination):
    if not os.path.exists(destination):
        return os.path.abspath(default)+'/'
    else:
        # print(os.path.abspath(destination)+'/')
        return os.path.abspath(destination)+'/'

PATH_SRC             = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.insert(0, PATH_SRC)
os.chdir(PATH_SRC)
#print('PATH_SRC : '+os.getcwd())
APP_NAME             = 'gpyfsa'
PATH_INIT            = '/home/'
PATH_LOCAL           = get_path('/usr/share/locale','../resources/locale')
PATH_MOUNT           = '/mnt/'+APP_NAME+'/'
PATH_RES             = get_path('/usr/share/','../resources/')
PATH_IMG             = get_path('/usr/share/pixmaps/'+APP_NAME,'../resources/pixmaps/'+APP_NAME)
PATH_LOG             = '/var/log/gpyfsa.log'



locale.setlocale(locale.LC_ALL, '')
for module in (gettext,gtk.glade):
    module.bindtextdomain(APP_NAME, PATH_LOCAL)
    module.textdomain(APP_NAME)
_ = gettext.gettext

K_DEV_NAME           = K_NAME    = K_DISK   = 0
K_DEV_TYPE           = K_NOVAL   = K_DEVICE = 1 
K_DEV_LABEL          = K_SELFVAL = 2
K_DEV_SIZE           = 3
K_DEV_USIZE          = 4
K_DEV_FSIZE          = 5
K_DEV_PSIZE          = 6
K_DEV_MOUNT          = 7
K_DEV_RWRIT          = 8

####################### (K_NAME , K_NOVAL, K_SELFVAL)
SAVEOPT              = (('o'    , True    ,          ),('v',True,),('d',True,),('L',False,True),('s',False,False),('e',False,False),('c',False,False),('z',False,True),('j',False,True))
K_DEV_PIX            = 0
K_DEV_ROOT           = 1
K_DEV_UNSUP          = 2
K_DEV_SUPPORT        = 3
K_DEV_ACTIVATABLE    = 4
K_DEV_ACTIVE         = 5
K_DEV                = 6

L_COLSNAME           = ('',_('device'),_('type'),_('label'),_('size'),_('used'),_('free'),_('%used'),_('mount point'))
IMG_TV_DEVICE        = PATH_IMG+'gpyfsa_dev.png'
IMG_TV_DEVICE_LOCKED = PATH_IMG+'gpyfsa_devlocked.png'

K_TYPE               = K_FILTER_NAME    = PAGE_SAVE = 0
K_TITLE              = K_FILTER_PATTERN = PAGE_REST = 1
K_FILTER             =                    PAGE_ARCH = 2
CBDT_SAVEFS          = 'SAVE', _('Save archive') , ((_('all'),'*'),(_('fsa archive'),'*.fsa'))
CBDT_ARCHFS          = 'OPEN', _('Select archive') , ((_('all'),'*'),(_('fsa archive'),'*.fsa'))

COMPRESSION_LEVEL    = ['lzo   -3', 'gzip  -2', 'gzip  -6', 'gzip  -9', 'bzip2 -2', 'bzip2 -5', 'lzma  -1', 'lzma  -6', 'lzma  -9']

labelProgressWait    = _("pls wait ...")
labelWorkInProgress  = _("work in progress - ")
labelMountDev        = _("mount %s")
labelMountroDev      = _("mount %s read-only")
labelRemountDev      = _("remount %s read-only")
labelUmountDev       = _("unmount %s")

sh                   = Shell()

def getClDev(key)    : return K_DEV+key

def getGladeXML()    : 
    #print(PATH_RES+APP_NAME+'/glade/'+APP_NAME+'2.glade')
    return gtk.glade.XML(PATH_RES+APP_NAME+'/glade/'+APP_NAME+'.glade',APP_NAME)

def chdir(path)      : return os.chdir(path)

def getShell()       : return sh

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

# Application info
SCALABLE_ICON = PATH_IMG+'gpyfsa.png'
APPNAME = "GPyFSA"
APPVERSION = "0.33"
COPYRIGHTS = _("Copyright © 2010-2012 a-Sansara\n Copyright © 2010-2012 pluie.org")
WEBSITE = "https://sourceforge.net/projects/gpyfsa/"
AUTHORS = [
    _('Developers:'),
    'a-Sansara (http://www.a-sansara.net)',
    '',
    _('Contributors:'),
    'Francois Dupoux for fsarchiver (http://www.fsarchiver.org/)',
]

ARTISTS = [
    ''
]

TRANSLATORS = _("translator-credits")

LICENSE = file_get_contents(os.path.abspath(PATH_RES+APP_NAME+'/LICENSE'))
