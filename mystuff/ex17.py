#!/usr/bin/python

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print"copying from %s to %s" % (from_file,to_file)

#we could do these two on one line too.how?
in_file=open(from_file)
indata=in_file.read()

print "the input file is %d bytes long" % len (indata)

print "does the output file exist  %r " % exists(to_file)
print "Ready ,hit RETURN to continue ,CTRL-C to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright ,all donw."

out_file.close()
in_file.close()
