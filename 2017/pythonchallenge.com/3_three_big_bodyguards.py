#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from string import ascii_lowercase, ascii_uppercase, translate, letters, count

import urllib, re, collections

"""
three big bodyguards
"""
# test string "mess" is shorter than on page pythonchallenge
# string is still from challenge 2 !!!
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

try:
    html_string = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
    #html_lines = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').readlines()
except IOError:
    print("")
    print("the server pythonchallenge can not be reached. Please try later or check internet connection")
    
result = ""
found = (re.findall(r'[a-z\d\s][A-Z]{3}[a-z][A-Z]{3}[a-z\d\s]', html_string))
for c in found:
    result += "".join(c[4])
print(result)
print("re version 2:")
print("".join(re.findall(r'[a-z\d\s][A-Z]{3}([a-z])[A-Z]{3}[a-z\d\s]', html_string)))
print("re version 3:")
print("".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', html_string)))
# An alternate regex using lookahead and lookbehind
print("re version 4:")
print("".join(re.findall("(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])",html_string)))

"""
[A-Z]{3} means exactly 3 capital letters. The brackets () are used to define groups. For each matching pattern, only the group is returned. Putting "".join() around it changes it from a list of letters to a continuous string, just for clarity.
"""
