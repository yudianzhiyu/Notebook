#!/usr/bin/python 
from sys import argv

script,user_name=argv
prompt='>'

print "HI %s ,I'm the %s script ." %(user_name ,script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes=raw_input(prompt)

print "where do you live %s ?" % user_name
lives=raw_input(prompt)

print "what kine of computer do you have?"
computer=raw_input(prompt)

print """
Alright,so you said %r about liking me .
you live in %r.NOt sure where that is .
And you have a %r computer.Nice.
""" % (likes,lives,computer)
