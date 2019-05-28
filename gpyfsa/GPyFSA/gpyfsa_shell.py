#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                     #
#   software  : GPyFSA    <http://gpyfsa.sourceforge.net/>                            #
#   version   : 0.32                                                                  #
#   date      : 2010                                                                  #
#   licence   : GPLv3.0   <http://www.gnu.org/licenses/>                              #
#   author    : a-Sansara <http://www.a-sansara.net/>                                 #
#   copyright : pluie.org <http://www.pluie.org/>                                     #
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

import subprocess as subp

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class Shell:

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    PIPE, CMD_DF, CMD_GREP, CMD_FSA, CMD_MOUNT, CMD_UMOUNT    = subp.PIPE, "df", "grep", "fsarchiver", "mount", "umount"
    authCmd   = { CMD_DF:1, CMD_GREP:1, CMD_FSA:1, CMD_MOUNT:1, CMD_UMOUNT:1 }
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getGrepPipeOut(self,args,grepStr):
        return self.__getGrepPipeOut(args,grepStr)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def pipe(self,cmd1,cmd2):
        return self.__pipe(cmd1,cmd2)
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def call(self,cmd,stdoe=subp.PIPE,fdsClose=False):
        return self.__call(cmd,stdoe,fdsClose)
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __call(self,cmd,stdoe=subp.PIPE,fdsClose=False):
        p = None
        if self.authCmd.has_key(cmd[0]): 
            #print cmd[0]+' auth => '+str(cmd)
            p = subp.Popen(cmd, stdout=stdoe, stderr=stdoe, close_fds=fdsClose)
        return p
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __pipe(self,cmd1,cmd2):
        p = None     
        if self.authCmd.has_key(cmd1[0]) and self.authCmd.has_key(cmd2[0]): p = subp.Popen(cmd2, stdin=self.__call(cmd1).stdout, stdout=subp.PIPE, stderr=subp.PIPE)
        return p
       
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def __getGrepPipeOut(self,cmd,grepStr):
        try    : return self.__pipe(cmd, [self.CMD_GREP, grepStr]).stdout.read().split("\n")
        except : return ""
