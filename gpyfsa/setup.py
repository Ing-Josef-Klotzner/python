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
from distutils.core import setup
import glob
import os

# I18N
I18NFILES = []

for filepath in glob.glob('resources/locale/*/LC_MESSAGES/*.mo'):
    lang = filepath[len('resources/locale/'):]
    targetpath = os.path.dirname(os.path.join('share/locale',lang))
    I18NFILES.append((targetpath, [filepath]))

setup(name='gpyfsa',
      version='0.34',
      packages=['GPyFSA'],
      scripts=['gpyfsa'],
      data_files=[('/usr/share/pixmaps'       , glob.glob('resources/pixmaps/gpyfsa/gpyfsa.png')),
                  ('/usr/share/pixmaps/gpyfsa', glob.glob('resources/pixmaps/gpyfsa/*.png')),
                  ('/usr/share/applications'  , ['resources/gpyfsa.desktop']),
                  ('/usr/share/gpyfsa'        , glob.glob('resources/gpyfsa/LICENSE')),
                  ('/usr/share/gpyfsa/glade'  , glob.glob('resources/gpyfsa/glade/*.glade'))]
                   + I18NFILES
      )
