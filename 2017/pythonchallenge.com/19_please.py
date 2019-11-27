#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import base64, subprocess,wave   #, pygame
"""
19 please
"""
site = "http://www.pythonchallenge.com/pc/hex/"
opt = "bin.html"

"""
From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!

--===============1295515792==
Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64
"""

#test = "UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YdizAQBABkAMQAtAAEADQAJA"
#print(base64.decodestring(test))

with open("19_indian_base64_wav") as wav_b64:
    wav_b64_c = wav_b64.read()

#base64.decode("19_indian_base64_wav", "19_indian_base64.wav")
decoded = base64.decodestring(wav_b64_c)

with open('19_indian.wav', 'w') as wav:
    wav.write(decoded)

print("converted '19_indian_base64_wav' string to wav file '19_indian.wav' and play it")

subprocess.call(["totem", "./19_indian.wav"])

print("this does not sound like a solution yet - 'sorry' :) .... need some conversion -- indian")


w = wave.open('19_indian.wav', 'rb')

h = wave.open("19_result.wav", "wb")

print(w.getnchannels())
print(w.getsampwidth())
print(w.getframerate())
h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())
wave.big_indian = 1
h.writeframes(frames)

h.close()
w.close()

subprocess.call(["totem", "./19_result.wav"])
print("not nice! ... you are an idiot ... ts ts ts")
answer_to_find = "in audio"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
##webbrowser.open(site + answer_to_find)


