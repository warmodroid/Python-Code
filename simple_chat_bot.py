import random

greetings = ['hola','hello','hi','Hi','hey!','hey']
random_greetings = random.choice(greetings)

question = ['how are you?','how are you doing?']
response = ['okay','fine']
random_response = random.choice(response)

while True:
	userInput = raw_input(">>>")
	if userInput in greetings:
		g = random_greetings
		print(g)
	elif userInput in question:
		print(random_response)
	else:
		print("I didnt understand what you said")
