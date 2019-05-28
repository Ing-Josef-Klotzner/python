#! /usr/bin/env python2
# savegebuehr.py  --  created by Ing. Josef Klotzner
print "Bitte geben sie den Savebetrag ein: "
betrag = int(raw_input())
print betrag
# (betrag + savegebuehr) * 0.02 = savegebuehr    <<  mathematisch
# betrag*0.02 + savegebuehr*0.02 = savegebuehr
# betrag * 0.02 = savegebuehr*0.98
# savegebuehr = (betrag *0.02)/0.98
betrag_save=betrag+(betrag *0.02)/0.98
betrag_save_n=betrag-(betrag *0.02)
print int(round(betrag_save+.5)), " ist der Betrag samt Savegebuehren, wenn Aufschlag vorher"
print int(round(betrag_save_n)), " ist der Betrag samt Savegebuehren, wenn Abzug nachher"

betrag_save=betrag+(betrag *0.01)/0.99
betrag_save_n=betrag-(betrag *0.01)
print
print int(round(betrag_save+.5)), " ist der Betrag samt Savegebuehren (1%), wenn Aufschlag vorher"
print int(round(betrag_save_n)), " ist der Betrag samt Savegebuehren (1%), wenn Abzug nachher"

print "enter um zu beenden"
end = raw_input()
