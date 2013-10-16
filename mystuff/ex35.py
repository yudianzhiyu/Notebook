#!/usr/bin/python

from sys import exit

def gold_room():
	print "this root is full of gold.how much do you take?"

	next=raw_input(">")
	if "0" in next or "1" in next:
		how_much=int(next)
	else:
		dead("man ,learn to type a number.")
		
	if how_much < 50:
		print "nice ,you're not greddy,you win !"
		exit(0)
	else:
		dead("you greedy bastard!")

def bear_room():
	print "there is a bear here ."
	print "the bear has a bunch of honey."
	print "the fat bear is in front of another door."
	print "how are you going to movee the bear?"
	bear_moved=false

	while True:
		next=rew_input(">")
		if next=="take honey":
			dead("the bear looks at you then slaps you face off.")
		elif next == "taunt bear" and not bear_moved:
			print "the bear has moved from the door.you can go through it now."
			bear_moved=True
		elif next == " taunt bear" and bear_moved:
			dead("the bear gets pissed off and chew you leg off.")
		elif next == " open door" and bear_moved:
			gold_room()
		else:
			print "i got no idea what that means."

def cthulhu_room():
	print "here you see the great evil cthulhu."
	print "he. if , what ever stares at you and you go insane."
	print " do you flee for you life or eat you head?"

	next=raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead ("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why ,"good job!"
	exit(0)

def start():
	print "you are in a dark room."
	print "there is a door to you right and left."
	print "which one do you take?"

	next=raw_input(">")

	if next=="left":
		bear_room()
	elif next=="right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")

start()
