# read file testfile.txt
# content Testfile
# ***   end   ***
#import pickle
f=open('C:/Python24/Scripts/josy/testfile.txt','r')
#x = pickle.load(f)
print 'ausgabe mit for line in'
for line in f:
	print line,
print
#f.close()
#f=open('C:/Python24/Scripts/josy/testfile.txt','r')
print 'ausgabe mit read'
#print 'Dies sollte die Datei noch einmal ausgeben - tut es aber nicht!'
#print f.tell()
f.seek(0)
#print f.tell()
print f.read()
print 'ausgabe mit readline'
#print 'Dies sollte die Datei auch noch einmal ausgeben - tut es aber auch nicht!'
f.seek(0)
print f.readline(),
print f.readline()
#for line in f:
#	print line,
#print 'ausgabe x aus pickle.load(f)'
#print x