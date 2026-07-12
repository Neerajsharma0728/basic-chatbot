import datetime
import time
name= input("enter your name: ")
presenthour= datetime.datetime.now().hour
if 5<= presenthour<=12:
    print("god morning ",name)
elif 12<= presenthour<=18:
    print("afternoon", name)
else: print("good evening",name)


print("HELLO! welcome to hero")
print("you can ask me basic questions, type 'bye' to exit from the bot")
#chatbot mm creation.
responce ={
    "hello" : " hi,welcome how can i help you",
    "how are you" : "im fine thank you",
    "who are you" : "im you personal assitant (hero)",
    "motivate me" : "keep going. you gonna win as soon as possible",
    "happy" : "great to hear that",
    "need help" : "im here to help you, tell me "
}
#funtion for user reponse 
def getresponse(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responce:
        if eachkey in userquestion:
            return responce[eachkey]
    return "im not able to answer this yet"

#user input
while True:

    userinput =input("enter what you want : ")
    reply= getresponse(userinput)
    print(reply)
    if "bye" in userinput.lower():
        break