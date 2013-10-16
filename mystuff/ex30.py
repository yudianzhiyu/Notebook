#!/usr/bin/python
people = 30
cars = 40
buses = 15

if cars > people:
	print "we should take the cars."
elif cars < people:
	print " we shoule not take the cars."
else:
	print " we can't decide."

if buses> cars:
	print "that's too many buses."
elif buses<cars:
	print "may be we could take buses."
else:
	print "we still can't decice."

if people > buses:
	print "alright,let's just  take the buses."
else:
	print "file ,let's stay home then."

