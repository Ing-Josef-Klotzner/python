#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import ascii_lowercase, ascii_uppercase, translate, letters, count

import urllib, re, collections

"""
find rare characters in mess
"""
# test string "mess" is shorter than on page pythonchallenge
mess = ("""\
</body>
</html>

<!--
find rare characters in the mess below:
-->

<!--

%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++
())&#@*[#}+#^}#%!![#&*}^{^(({+#*[!{!}){(!*@!+@[_(*^+*]$]+@+*_##)&)^(@$^]e@][#&)(
^*&_^%+{^{$+$[^_*)*++%^++#%#%*^$*@+${!+%@!}^q(%!({@]%@]]@&#^$[&![(**${)]*^))[$}#
!{&++#^({{@$$@#)&*%[!]$&{^!%$+)}]_@+{*_]@)]{*]@+^]$}}]&)]#!_)}]@$@_[&_*)+(_}%#u(
%&!#a}#+#^#{_&)({%!_]!_][}^_%*+}$)&!@[)#@{@[%*!*#_[$$(_[+!^[[[[+*{[*+{!#&*^@&+%)
)+#&{${%+(*_$$^]}&#+^%())^_^@(_]*^]{))]+_)$@_%*([}{${^(]{[[#(#]&}+l}%#@}{{)%@{+}
_^&!&(%{_%*[($])}%[{@{{^_[$}@&&_)^()({%![#][(}+&^(]&}!*@#{)]{i]%_]%^(&]^{+_([)$%
_]}]!^_[!)&&&]_(#]+_!_}&&)#$*+^###[**@{}{%^[&#+&__@@@[+t]+&)^{*((@$!$)%]$[{}$}&$
!^$!@y{$][%@+^##](_*(##^_{#)$+$*&}[#%&_!+)*@{][_($#_$*{(}_[{+)$[)+{#)+($_]{}!]+#
+_+}%@#{_}^#*)%*(*}*![}[%_[[^@$&%)([*{_${)$^^_!+}{)!)@_[*$_}*}$#[+}{]*+!^])}&{+#
+!@!^*@}!}&{]*#^@}_[)}#@%!_*#!$}!)[(${+^&!{[&&&*[{}+*+(#+_[}{$$)#([*!)%@^%_]#%$$
(++^+&)}*_&%@#[^^+^&@_%]+$%$#$*)@!(]*+@]}%$$}$(#$&^(%[*([&]*^&}(!#{&_}^(*{(+$#}}

-->
""")
html_string = mess
html = mess.split()

#html_string = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
#html = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').readlines()

interest = False
trslt_txt = ""
re_txt = ""
output = ""
html_meas_string = ""
str_is_alpha_txt = ""
flt_txt = ""
block_of_interest = False

print()
print("Do you see the readable letters in the mess?")
print()
print(mess)
   
for item in html:
    if "<!--" in item:
        interest = True
    if interest and block_of_interest:
        html_meas_string += item
        # using filter
        flt_txt += filter(lambda x: x in letters, item)
        # using string.is_alpha
        str_is_alpha_txt += "".join([char for char in item if char.isalpha()])
        # using re
        re_txt += "".join(chr for chr in re.findall(r'[a-z]', item))
        # using translate: 
        txt = (item.translate(None, '%#+!)(}{&*$@[]_^<->'+chr(10)))
        if txt != "":
            trslt_txt += txt
    if "-->" in item:
        block_of_interest = True
        interest = False

counts = {}
print("solution measuring rare characters using string.count:")
for c in html_meas_string:
  if counts.has_key(c):
    continue
  counts[c] = html_meas_string.count(c)
  if counts[c] < 2 and c not in "<>-!":  # guess that rare characters will occur less than 2 times
    output += c
print(counts)
print (output)

print("")
print("solution using re.findall:")
print (re_txt)
print("")
print("solution measuring rare characters:")        
data = ''.join([line.rstrip() for line in html_meas_string])    
OCCURRENCES = collections.OrderedDict()
for c in data: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = 2   # len(data) // len(OCCURRENCES)
print(OCCURRENCES)
print (''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC and c not in "<>-!"]))
print("")
print("solution using list comprehension and string.isalpha:")
print(str_is_alpha_txt)
print("")
print("solution with filter:")        
print(flt_txt)
print("")
print("solution with translate:")        
print(trslt_txt)

