import speech_recognition  #pip install speechrecognition and pyaudio
import pyttsx3  #pip install pyttsx3
from datetime import date, datetime

robotEar = speech_recognition.Recognizer()
robotBrain = ""
robotMouth = pyttsx3.init()

while True:
#listen:
	
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening ...")
		audio = robotEar.listen(mic)
	try:	
		you = robotEar.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)

	#understand:
	if you == "":
		robotBrain = "I can't hear you, try again !"
	elif "hello" in you:
		robotBrain = "Hello Nhu !"
	elif "today" in you:
		robotBrain = date.today().strftime("%B %d %Y")
	elif "time" in you:
		robotBrain = datetime.now().strftime("%H hours %M minutes %S seconds")
	elif "goodbye" in you:
		robotBrain = "Bye Nhu, see you again !"
		print("Robot: " + robotBrain)
		robotMouth.say(robotBrain)
		robotMouth.runAndWait()
		break
	else:
		robotBrain = "Sorry, i don't understand"
	print("Robot: " + robotBrain)

	#speak:
	robotMouth.say(robotBrain)
	robotMouth.runAndWait()
