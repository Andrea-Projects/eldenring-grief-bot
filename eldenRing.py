#Every X seconds something random happens on Elden Ring
#1 - Use item (designed for Estus Flask waste) | Empty your load
#2 - Roll | Let's roll
#3 - Touch grass (minimize window) | Touch some grass, you nerd
#4 - Jump | Jump, my puppet
#5 - Resolve a captcha/minigame | Let's play a little game, just you and me
#6 - Stop being a pussy (attack) | Quit being a pussy
#7 - Stop playing | Stand still for X second/s. Loser
#98 - Bot stops itself | You're no fun to play with anymore. Farewell, puppet
#99 - ALT + F4 (ultra rare) | Go eat a dick. You really suck at this. Unworthy swine

#Import Libraries
import random
import time
import os
from pynput.keyboard import Key, Controller
import webbrowser
import pyautogui
from pydub import AudioSegment
from pydub.playback import play

#Functions --
	
#Event 1: use item
def useItem():
	print("    > Event #1: Use Item")
	play(event1)
	keyboard.press('r')
	time.sleep(0.25)
	keyboard.release('r')

#Event 2: Roll
def letsRoll():
	howMany = random.randint(1, 4)
	print("    > Event #2: Roll " + str(howMany) + " times")
	play(event2)
	for i in range(howMany):
		keyboard.press(Key.space)
		time.sleep(0.25) #if you don't give it this cooldown between press & release, it simply doesn't work <--<
		keyboard.release(Key.space)
		time.sleep(1)
	else:
		print("        Done")

#Event 3: Touch grass
def touchGrass():
	print("    > Event #3: Touch grass")
	play(event3)
	window = pyautogui.getActiveWindow()
	window.minimize()

#Event 4: Jump
def justJump():
	print("    > Event #4: Jump")
	play(event4)
	keyboard.press('f')
	time.sleep(0.25) #if you don't give it this cooldown between press & release, it simply doesn't work <--<
	keyboard.release('f')

#Event 5: Captcha
def solveCaptcha():
	print("    > Event #5: Solve this captcha")
	play(event5)
	webbrowser.open_new('https://nopecha.com/demo/recaptcha#easy')

#Event 6: Stop being a pussy
def noPussies():
	howMany = random.randint(1, 4)
	print("    > Event #6: Attack " + str(howMany) + " times")
	play(event6)
	for i in range(howMany):
		pyautogui.mouseDown()
		time.sleep(0.25) #if you don't give it this cooldown between press & release, it simply doesn't work <--<
		pyautogui.mouseUp()
		time.sleep(0.5)
	else:
		print("        Done")

#Event 7: Stop playing
def stopPlaying():
	howMany = random.randint(1, 5)
	print("    > Event #7: Stop playing for " + str(howMany) + "s")
	if howMany == 1:
		play(event7_1s)
	elif howMany == 2:
		play(event7_2s)
	elif howMany == 3:
		play(event7_3s)
	elif howMany == 4:
		play(event7_4s)
	elif howMany == 5:
		play(event7_5s)

#Event 98: Stop bot
def byYourself():
	print("    > Event #98: Goodbye Swine")
	play(event98)

#Event 99: ALT+F4
def emergencyMeeting():
	print("    > Event #99: Unlucky Bitch")
	play(event99)
	with pyautogui.hold('alt'):
		pyautogui.press('f4')
	

# Code --

#Remove pyautogui safe margins for mouse
pyautogui.FAILSAFE = False

#Audio files
event1 = AudioSegment.from_wav("media/event1.wav")
event2 = AudioSegment.from_wav("media/event2.wav")
event3 = AudioSegment.from_wav("media/event3.wav")
event4 = AudioSegment.from_wav("media/event4.wav")
event5 = AudioSegment.from_wav("media/event5.wav")
event6 = AudioSegment.from_wav("media/event6.wav")
event7_1s = AudioSegment.from_wav("media/event7_1s.wav")
event7_2s = AudioSegment.from_wav("media/event7_2s.wav")
event7_3s = AudioSegment.from_wav("media/event7_3s.wav")
event7_4s = AudioSegment.from_wav("media/event7_4s.wav")
event7_5s = AudioSegment.from_wav("media/event7_5s.wav")
event98 = AudioSegment.from_wav("media/event98.wav")
event99 = AudioSegment.from_wav("media/event99.wav")

#Clean terminal
os.system('cls' if os.name == 'nt' else 'clear')
print("---------- ELDEN RING GRIEF BOT ----------")

#Useful variables
keyboard = Controller()
eventCounter = 0
minCooldown = 5 #in seconds
maxCooldown = 20 #in seconds

while True:
	#Cooldown generator
	eventCounter += 1
	cooldown = random.randint(minCooldown, maxCooldown)
	#cooldown = 5 #Force cooldown for testing purposes
	print("Grief n." + str(eventCounter) + " | Cooldown: " + str(cooldown) + "s")
	time.sleep(cooldown)

	#Event generator
	randomEvent = random.randint(1, 7)

	specialEvent = random.randint(1, 100)
	if specialEvent <= 10: #There's a 9% chance that the bot will stop itself
		randomEvent = 98
	if specialEvent == 1: #There's a 1% chance that the bot will make me alt+f4
		randomEvent = 99

	#randomEvent = 99 #Force event for testing purposes

	#Check if Elden Ring is the Active Window, then do stuff
	window = pyautogui.getActiveWindow()
	windowTitle = str(window)
	if("ELDEN RING" in windowTitle):

		if randomEvent == 1:
			useItem()

		if randomEvent == 2:
			letsRoll()

		if randomEvent == 3:
			touchGrass()

		if randomEvent == 4:
			justJump()

		if randomEvent == 5:
			solveCaptcha()

		if randomEvent == 6:
			noPussies()

		if randomEvent == 7:
			stopPlaying()

		if randomEvent == 98:
			byYourself()
			break

		if randomEvent == 99:
			emergencyMeeting()
			break

	else:
		print("-- ACTION ABORTED: ACTIVE WINDOW IS NOT ELDEN RING --")