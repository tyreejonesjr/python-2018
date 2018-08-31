import random
responses = ["yes","no","maybe"]
print(responses[0])
name = input("What is your name?")
while True:
    answer = input("Hello " + name + " what do you want to ask?")
    if answer =="stop":
        break
    else:
        choice = random.choice(responses)
        print(answer + ": " + choice)
print( "Thanks for using the 8ball")
