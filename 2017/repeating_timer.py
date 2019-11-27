#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Fri Aug 18 15:57:34 2017

@author: josef
"""
from time import time
from threading import Timer

def tic_callback():
    print("tic callback ausgelöst")
    #print(".", end="\n")
def callback():
    print("final callback ausgelöst")

def timer_ticking(tic_seconds, seconds, _tic_callback, _callback, startmomenttime=time()):
    """ ein precision timer mit 'Sekundentick' 
    tic_callback Funktion jeden tic (z.B. Sekunde) und andere callback Funktion am Ende """
    def repeating_timer(rem_reps, next_call):
        next_call += tic_seconds   # (next_call - time) for time correction
        rem_reps -= 1
        reps = int(seconds / tic_seconds)
        if reps > 1 and (rem_reps == reps - 2):
            next_call -= tic_seconds + time() - next_call   # Versatzkorrektur
        if rem_reps != reps - 1 and rem_reps != 0:
            _tic_callback()
        if rem_reps >= 0:
            Timer(next_call - time(), repeating_timer, [rem_reps, next_call]).start()
        else:
            _callback()
            print(str(reps)+" timer_ticking zu "+str(tic_seconds)+
                " Sekunden beendet nach: "+str(time() - startmomenttime)+" Sekunden")
    next_call = time()
    repeating_timer(int(seconds/tic_seconds), next_call)   # seconds//tic_seconds = repetitions

def rep_timer(seconds, repetitions, startmomenttime=time()):
    """ ein sich um 'repetitions' wiederholender timer """
    def repeating_timer(rem_reps):
        rem_reps -= 1
        if rem_reps >= 0:
            Timer(seconds, repeating_timer, [rem_reps]).start()
        else:
            print(str(repetitions)+" rep_timer zu "+str(seconds)+
                " Sekunden beendet nach: "+str(time() - startmomenttime)+" Sekunden")
    repeating_timer(repetitions)

# from time import ctime,time   from threading import Timer
def rep_timer_prec(seconds, repetitions, startmomenttime=time()):
    """ ein sich um 'repetitions' wiederholender precision timer """
    def repeating_timer(rem_reps, next_call):
        next_call += seconds   # (next_call - time) for time correction
        rem_reps -= 1
#        if repetitions > 1 and (rem_reps == repetitions - 2 or rem_reps == repetitions - 3  or rem_reps == 1):
#            print()
#            cur_time = time()
#            print(cur_time-startmomenttime)
#            print("Korrekturzeit: ", str(seconds+cur_time-next_call))
#            print(next_call-cur_time)
#            print(startmomenttime)
#            print(next_call)
        if repetitions > 1 and (rem_reps == repetitions - 2):
#            next_call_old = next_call
#            cur_time = time()
            next_call -= seconds + time() - next_call   # Versatzkorrektur
#            vkz = next_call - next_call_old
#            print("Versatzkorrekturzeit: ", str(vkz))
#            print(next_call-cur_time)
        if rem_reps >= 0:
#            print(rem_reps)
            Timer(next_call - time(), (lambda: repeating_timer(rem_reps, next_call))).start()
        else:
            print(str(repetitions)+" rep_timer_prec zu "+str(seconds)+
                " Sekunden beendet nach: "+str(time() - startmomenttime)+" Sekunden")
    next_call = time()
    repeating_timer(repetitions, next_call)

def rep_timer_prec_v2(seconds, repetitions, startmomenttime=time()):
    """ ein sich um 'repetitions' wiederholender precision timer """
    def repeating_timer(rem_reps, next_call):
        next_call += seconds   # (next_call - time) for time correction
        rem_reps -= 1
        if repetitions > 1 and (rem_reps == repetitions - 2):
            next_call -= seconds + time() - next_call   # Versatzkorrektur
        if rem_reps >= 0:
            Timer(next_call - time(), repeating_timer, [rem_reps, next_call]).start()
        else:
            print(str(repetitions)+" rep_timer_prec_v2 zu "+str(seconds)+
                " Sekunden beendet nach: "+str(time() - startmomenttime)+" Sekunden")
    next_call = time()
    repeating_timer(repetitions, next_call)

timer_ticking(.1, 1, tic_callback, callback)
rep_timer(0.001,1000)
rep_timer_prec(.001, 1000)
rep_timer_prec_v2(0.01, 100)
