#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
#Solar System 3D Animation using python-visual

from visual import *

Ome = 2*3.14159
mag = 300   # magnifier for visibility of planets

sun = sphere(color = vector(1,1,0), pos=vector(0,0,0), radius=.5*mag/20, shininess=10)
mercury = sphere(color = vector(0.5,0.5,1), pos=vector(41,0,0), radius=.00175*mag, shininess=10, make_trail=True, retain=50)
venus = sphere(color = vector(1,1,0.5), pos=vector(77,0,0), radius=.0043*mag, shininess=10, make_trail=True, retain=50)
earth = sphere(color = vector(0,0,1), pos=vector(107,0,0), radius=.0045*mag, shininess=10, make_trail=True, retain=50)
moon = sphere(color = vector(0.5,0.5,0.5), pos=vector(107+.275*mag/10,0,0), radius=.00125*mag, shininess=10, make_trail=True, retain=50)
#mars = sphere(color = vector(0.8,0.2,0.2), pos=vector(163,0,0), radius=.00245*mag, shininess=10, make_trail=True, retain=50)
#jupiter = sphere(color = vector(0.5,0.5,0), pos=vector(556,0,0), radius=.051*mag/5, shininess=10, make_trail=True, retain=50)
#saturn = sphere(color = vector(0.5,0.5,0.5), pos=vector(1019,0,0), radius=.043*mag/5, shininess=10, make_trail=True, retain=50)
#uranus = sphere(color = vector(0.5,0.5,0.5), pos=vector(2051,0,0), radius=.018*mag/5, shininess=10, make_trail=True, retain=50)
#neptune = sphere(color = vector(0.5,0.5,0.5), pos=vector(3213,0,0), radius=.017*mag/5, shininess=10, make_trail=True, retain=50)

earth.make_trail = True
moon.make_trail = False

framerate = 25
MercuryOmega = Ome/88
VenusOmega = Ome/225
EarthOmega = Ome/365
MoonOmega=Ome/28
MarsOmega = Ome/687
JupiterOmega = Ome/4333
SaturnOmega = Ome/10756
UranusOmega = Ome/30687
NeptuneOmega = Ome/60190

moonAngle = 0
#scene.mouse.getclick()

while True:
    rate(framerate)
    mercury.rotate(angle=MercuryOmega, axis=vector(1,8,0), origin=vector(0,0,0))
    venus.rotate(angle=VenusOmega, axis=vector(1,17,0), origin=vector(0,0,0))
    earth.rotate(angle=EarthOmega, axis=vector(0,1,0), origin=vector(0,0,0))
    moonAngle+=MoonOmega
    moon.pos=earth.pos + vector(.275*mag/10,0,0)
    moon.rotate(angle=moonAngle, axis=vector(0,1,0), origin=earth.pos)
#    mars.rotate(angle=MarsOmega, axis=vector(0,1,0), origin=vector(0,0,0))
#    jupiter.rotate(angle=JupiterOmega, axis=vector(0,1,0), origin=vector(0,0,0))
#    saturn.rotate(angle=SaturnOmega, axis=vector(0,1,0), origin=vector(0,0,0))
#    uranus.rotate(angle=UranusOmega, axis=vector(0,1,0), origin=vector(0,0,0))
#    neptune.rotate(angle=NeptuneOmega, axis=vector(0,1,0), origin=vector(0,0,0))

    


"""
                Name	Inclination
                        to ecliptic	
                                Inclination
                                to Sun's equator	
                                        Inclination
                                        to invariable plane
Terrestrials	Mercury	7.01°	3.38°	6.34°
                Venus	3.39°	3.86°	2.19°
                Earth	0	    7.155°	1.57°
                Mars	1.85°	5.65°	1.67°
Gas giants	    Jupiter	1.31°	6.09°	0.32°
                Saturn	2.49°	5.51°	0.93°
                Uranus	0.77°	6.48°	1.02°
                Neptune	1.77°	6.43°	0.72°

Mercury: 88 days
Venus : 225 days
Earth: 365 days
Mars: 687 days
Jupiter: 4333 days
Saturn: 10756 days
Uranus: 30687 days
Neptune: 60190 days

Ein Modell im Maßstab 1 : 1,4 Milliarden findet man mit Sonne und allen Planeten auf vielen Planetenwegen. Ein Fußgänger käme hier mit etwa der sechsfachen Lichtgeschwindigkeit voran, die hier nur 21,4 cm/s entspricht.

Alle folgenden Größen sind gerundet; für alle in Wirklichkeit mehr oder weniger schwankenden Abstände wurden mittlere Werte verwendet.

Der Durchmesser der Sonne beträgt in diesem Modell 1 m.
Der Planet Merkur befindet sich im Abstand von 41 m zur Sonne und hat einen Durchmesser von 3,5 mm.
Der Planet Venus befindet sich im Abstand von 77 m zur Sonne und hat einen Durchmesser von 8,6 mm.
Die Erde befindet sich im Abstand von 107 m zur Sonne und hat einen Durchmesser von 9,1 mm.
Der Erdmond befindet sich im Abstand von 27,5 cm zur Erde (nur etwas weniger als die Höhe eines Din-A4-Blatts mit 29,7 cm) und hat einen Durchmesser von 2,5 mm.
Der Planet Mars befindet sich im Abstand von 163 m zur Sonne und hat einen Durchmesser von 4,9 mm.
Der Planet Jupiter befindet sich im Abstand von 556 m zur Sonne und hat einen Durchmesser von 102 mm.
Der Planet Saturn befindet sich im Abstand von 1019 m zur Sonne und hat einen Durchmesser von 86 mm.
Die Saturnringe: Der A-Ring hat einen äußeren Durchmesser von 193 mm und der B-Ring von 168 mm. Der äußerste Ring, der E-Ring, hat einen äußeren Durchmesser von knapp 700 mm.
Der Planet Uranus befindet sich im Abstand von 2051 m zur Sonne und hat einen Durchmesser von 37 mm.
Der Planet Neptun befindet sich im Abstand von 3213 m zur Sonne und hat einen Durchmesser von 35 mm.
"""
