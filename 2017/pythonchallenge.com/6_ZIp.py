#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import zipfile, string, re, urllib
from StringIO import StringIO


"""
zip - now there are pairs
readme.txt: welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
"""
site = "http://www.pythonchallenge.com/pc/def/"
opt = "channel.jpg"
answer_to_find = ""
coll_comments = ""
nothing = "90052"
#zobj = StringIO()

# zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# zipfile.ZipInfo([filename[, date_time]])

#zobj.write(urllib.urlopen(site + "channel.zip").read())

#with zipfile.ZipFile(zobj) as channel_zip:
with zipfile.ZipFile('channel.zip','r') as channel_zip:
    # objs_list = channel_zip.infolist()
    name_list = channel_zip.namelist()
    # print(name_list, end = " ")
    # channel_zip.printdir()
    for _file in name_list:
        content = channel_zip.read(_file)
        # only in answer there's no ' is '
        if content.find(" is ") == -1:
            # print(_file + " " + content, end = "  ")
            answer_to_find = content
            found_in_file = _file

    # second part - collect the comments
    info_obj_list = channel_zip.infolist()
    # verification that info_list and name_list are in same order  --> zip them to relate them
    print("")
    verified = True
    print(str(len(info_obj_list)) + " Files in zip File")
    for c in range(len(info_obj_list)):
#        print(channel_zip.infolist()[c].filename + " " + channel_zip.namelist()[c], end = "  ")
        if info_obj_list[c].filename != name_list[c]:
            verified = False
    if verified:
        print("it is verified by comparing file names, that infolist and namelist are in same order" +\
              "   --> zip them to relate them")
    else:
        print("infolist and namelist are in no related order ... puh!")

    name_info_list = zip(name_list, info_obj_list)
    
#    filename = ZipInfo_obj.filename
#    comment = ZipInfo_obj.comment
#        collect the comments
#    find filename in second tuple of name_info_list, 
#    get comment of related first tuple, get content of file for next
    for _ in range(len(name_info_list)):   # there are 910
#           without using zipped name_info_list:
#        coll_comments += channel_zip.getinfo(nothing + ".txt").comment
        for tup in name_info_list:
            if nothing + ".txt" == tup[0]:
                coll_comments += tup[1].comment
        # get next nothing
        inspected_file = nothing + ".txt"
        file_content = channel_zip.read(inspected_file)
#        nothing = "".join(re.findall('nothing is ([0-9]*)', file_content))
        nothing = file_content.split()[-1]
        if not nothing.isdigit():
            print("unexptected content in inspected file " + inspected_file)
            break

# answer_to_find = "in progress"
print("")
print("First answer to find is: " + answer_to_find + " found in file '" + found_in_file + "'")
print("Second answer to find is collected comment of each file comment in zip file: \n" + coll_comments)
#webbrowser.open(site + answer_to_find)
