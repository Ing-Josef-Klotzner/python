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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import gtk
import gpyfsa_conf as conf

class AboutDialog(gtk.AboutDialog):

    def __init__(self, parent=None):
        gtk.AboutDialog.__init__(self)

        # Set up the UI
        self.__initialize_dialog_widgets()

    #################### Private Methods ####################
    
    def __initialize_dialog_widgets(self):
        self.set_name(conf.APPNAME)
        self.set_version(conf.APPVERSION)
        self.set_copyright(conf.COPYRIGHTS)
        self.set_logo(gtk.gdk.pixbuf_new_from_file(conf.SCALABLE_ICON))
        self.set_translator_credits(conf.TRANSLATORS)
        self.set_license(conf.LICENSE)
        self.set_website(conf.WEBSITE)
        self.set_website_label(conf.APPNAME)
        self.set_authors(conf.AUTHORS)
        self.set_artists(conf.ARTISTS)

        # Show all widgets
        self.show_all()
