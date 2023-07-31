import random
import os

lines = ["I totally agree", "Good, how are you?", "Whales are pretty big", "Jurassic park released in 1993, that's a long time ago", "Hi", "You should try minecraft", "Minecraft is getting camels (or is it cammels?)", "Egypt is a country in Africa", "Counting sheep...", "No", "Yes", "I actually don't know what you are saying", "Firefox has a cool logo", "I want to thank our sponsor, Raid: Shadow Legends", "Subnautica good game", "Fun fact: this isn't a fun fact", "FEED THE PENGUINS", "Deinosuchus was pretty big", "I have no friends", "Programming is fun", "Yeah, your way of doing it is better"]

os.system("clear")

while True:
	input(">")
	print(random.choice(lines))
