from pynput.keyboard import Key, Listener as key_listener
from pynput.mouse import Listener as mouse_listener
import os
from threading import Thread
import time

def play_sound(filename):
	print("Playing " + filename)
	thread = Thread(target=os.system, args=("aplay " + filename, ))
	thread.start()
	#os.system("aplay " + filename)

keyboards = [
	['a', 'b', 'c', 'd', 'e'],
	['1', '2', '3', '4', '5'],
	['do', 're', 'mi', 'fa', 'so'],
]

current_keyboard = 0

def on_release(key):
	current_outputs = keyboards[current_keyboard]
	if key == Key.esc:
		player.terminate()  
		return False

	if key == Key.left:
		output = current_outputs[0]
	elif key == Key.right:
		output = current_outputs[1]
	elif key == Key.up:
		output = current_outputs[2]
	elif key == Key.down:
		output = current_outputs[3]
	elif key == Key.space:
		output = current_outputs[4]

	play_sound('sounds/{}.wav'.format(output))

def on_click(x, y, button, pressed):
	global current_keyboard
	if pressed:
		current_keyboard = (current_keyboard + 1) % 3
		print("Switched to Keyboard #{}".format(current_keyboard+1))


play_sound('sounds/do.wav')
time.sleep(0.2)
play_sound('sounds/re.wav')
time.sleep(0.2)
play_sound('sounds/mi.wav')


with key_listener(on_release=on_release) as keyboard, mouse_listener(on_click=on_click) as mouse:
	mouse.join()
	keyboard.join()

