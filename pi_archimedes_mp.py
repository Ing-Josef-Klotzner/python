#!/usr/bin/python
# -*- coding: utf-8 -*-
# Berechnung Pi nach Methode Archimedes optimiert - deutlich weniger Vielecke für höhere Präzision
# Die Differenz des Umfangs des Um Kreis Vielecks zu Pi verhält sich zur Differenz zwischen Pi und dem Umfang des In Kreis Vielecks wie 2 : 1
# Daher kann man ausgehend von einem jeweiligen n in je einem In Kreis n-Eck (Vieleck) und einem Um Kreis n-Eck auf Pi viel genauer schließen
# Referenz Pi = (Zeilenumbruch im Editor auf 'nach jedem Wort' einstellen)
pr='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'
#.....1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#..............1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3.........4.........5.........6.........7.........8.........9.........0
#........................................................................................................1...................................................................................................2...................................................................................................3...................................................................................................4...................................................................................................5...................................................................................................6...................................................................................................7...................................................................................................8...................................................................................................9...................................................................................................0
#............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................1
from decimal import *
from sys import argv

CEND      = '\33[0m'
#CBLUE   = '\33[34m'
#CCYAN  = '\33[36m'
#CYELLOW = '\33[33m'
#CSELECTED = '\33[7m'
CBLUE2   = '\33[94m'

def prRed(prt): print("\033[91m{}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m{}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m{}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m{}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m{}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m{}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m{}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m{}\033[00m" .format(prt))

# Benutzereingaben bei Programmaufruf prüfen
if len(argv) == 1:
	print ("usage: "+argv[0]+" 'Anzahl der gewünschten Nachkommastellen'")
	print ("Es wird per default Pi auf 8 Stellen berechnet")
	argv.append(8)
f_prec=int(argv[1])
if f_prec<1:
    f_prec=0
count, ecken, last_avr, prec = 0, 6, Decimal('0'), f_prec+4  # prec ... Präzision mit der gerechnet wird (3 Stellen mehr)
getcontext().prec=prec
a, b = Decimal('2')*Decimal('3').sqrt(), Decimal('3')  # fma (function multiply and add decimal)
pi=Decimal(pr)
avr = (a+b)/2

# Berechne Umfang des Inkreis-n-Ecks (n=count) und des Umkreis-n-Ecks, bilde daraus gewichteten Mittelwert und vergleiche bis das Ergebnis gleich dem vorigen Ergebnis bei angegebener zu berechnender Anzahl von Stellen ist 
while (avr.quantize(Decimal((0,(1,),-(f_prec))),rounding=ROUND_DOWN) != last_avr.quantize(Decimal((0,(1,),-(f_prec))),rounding=ROUND_DOWN)):
    if f_prec<10:
        print ("{:>30} Ecken  ".format(ecken)+"Pi aus gewichtetem Mittelwert a,b: "+str(avr))
    last_avr, last_a, last_b = avr, a, b
    count += 1
    a=Decimal('2')*a*b/(a+b)
    b=Decimal(a*b).sqrt()
    avr=b+(a-b)/Decimal('3')  # (a-pi)/(pi-b)=2 -> daher gewichteter Mittelwert!
    ecken*=2 	# ecken = 3 * 2 hoch (count+1)

# Ermittlung wie viele Stellen Genauigkeit für Pi tatsächlich berechnet wurden und korrigieren der Anzahl an Stellen für die ungerundete Formattierung (f_prec)
f_prec=prec-1
prGreen ("optimiertes Archimedes Pi':" + str(last_avr))
while (last_avr.quantize(Decimal((0,(1,),-(f_prec))),rounding=ROUND_DOWN) != avr.quantize(Decimal((0,(1,),-(f_prec))),rounding=ROUND_DOWN)):
    f_prec-=1
print ("Durchläufe: {:>3} (6 Ecken ist Ausgangswert.)".format(count-1)+" Dabei werden tatsächlich "+str(f_prec)+" Nachkommastellen von Pi bestimmt.")
prYellow ("Dies entspricht Angleichung an Vieleck mit Ecken: {}".format(ecken/2)+" = 3 * 2^{}".format(count-1))
prGreen ("optimiertes Archimedes Pi: " + str(last_avr.quantize(Decimal((0,(1,),-(f_prec))),rounding=ROUND_DOWN)))
print ("Reference  Pi:             "+str(pi.quantize(Decimal((0,(1,),-(prec-1))),rounding=ROUND_DOWN)))

# Feststellen bis zu welcher Stelle das Ergebnis des Archimedes genau ist (a=b) und das Ergebnis in genauen Teil und ungenauen Teil zerlegen, um hervorheben zu können, bis zu welcher Stelle ursprüngliche Archimedes Methode genau ist
A_prec=f_prec
while (last_a.quantize(Decimal((0,(1,),-(A_prec))),rounding=ROUND_DOWN) != last_b.quantize(Decimal((0,(1,),-(A_prec))),rounding=ROUND_DOWN)):
    A_prec-=1
print (" Um Kreis n-Eck a:         "+str(last_a)[:A_prec+2]+CBLUE2+str(last_a)[A_prec+2:])+CEND
print (" In Kreis n-eck b:         "+str(last_b)[:A_prec+2]+CBLUE2+str(last_b)[A_prec+2:])+CEND
print ("Nach ursprünglicher Archimedes Methode ist Pi bei Berechnung mit "+str(ecken/2)+"-Eck nur auf "+str(A_prec)+" Nachkommastellen bestimmt, ");
print ("da Archimedes nur mit Bestimmtheit wusste, dass 'Umfang des Umkreis n-Ecks (a)' > Pi > 'Umfang des Inkreis n-Eck (b)'");
print ("Durch Optimierung mittels gewichtetem Mittelwert des Delta zwischen Umkreis und Inkreis je zu Pi ")
if A_prec>0 :
    print ("werden gegenüber ursprünglicher Archimedes Methode {:1.2f} mal so viele Nachkommastellen bestimmt".format
(float(f_prec)/A_prec))
else :
    print ("werden gegenüber ursprünglicher Archimedes Methode {:1.2f} gegenüber keine Nachkommastellen bestimmt".format(float(f_prec)))
print ("(a-pi)/(pi-b)=2/1 -> daher ist Pi mittels gewichtetem Mittelwert deutlich genauer berechenbar!")


CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CCYAN  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CCYANBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CCYAN2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CCYANBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

formatters = {             
    'RED': '\033[91m',     
    'GREEN': '\033[92m',   
    'END': '\033[0m',      
}

print 'Master is currently {RED}red{END}!'.format(**formatters)
print 'Help make master {GREEN}green{END} again!'.format(**formatters)
