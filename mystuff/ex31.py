#!/usr/bin/env python

print " You enter a dark root with two doors. Do you go through door #! or door #1?"
door = raw_input(">")

if door == "1":
	print "there 's a giant bear here eating a cheese cake. what do you do ?"
	print "1.take the cake."
	print "2.Scream at the bear."
	
	bear=raw_input(">")

	if bear=="1":
		print "the bear eats you face off .Good job!"
	elif bear == "2":
		print "the bear eats you legs off .good job!"
	else:
		print " well,doing %s is probably better. Bear runs away." % bear
elif door == "2":
	print " you star into the endless abyss at cthulhu's retina"
	print "1. blueberries."
	print "2.yellow jacket clothespins."
	print "3.understanding revolvers yelling melodies."

	insanity=rew_input(">")

	if insanity =="1" or insanity =="2":
		print "you body survives powered by a mind of jello. good job!"
	else:
		print "the insanity rots you eyes in to a pool of muck  . good job!"

else:
	print "you stumble around and fall on a knife and die .good job!"



