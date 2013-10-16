#!/usr/bin/python
def print_two(*args):
	arg1,arg2=args
	print "arg1: %r ,arg2:%r " % (arg1,arg2)

#ok,that *args is actually pointless , we can just do this 
def print_two_agin(arg1,arg2):
	print "arg1: %r,arg2 %r " % (arg1,arg2)

#this just takes one argument
def print_one(arg1):
	print"arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print " i got no thin'."

print_two("Zed","shaw")
print_two_agin("zed","shaw")
print_one("fiest!")
print_none()
