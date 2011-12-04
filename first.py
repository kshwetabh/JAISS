import speech
import datetime
import speakWebPage
import os
import Weather
import ReadMail


def getCurrentTime():
    """
        Returns the properly formatted current time
    """
    now = datetime.datetime.now();
    hr = now.hour
    greeting = ""
    ampm = ""
    if (hr < 12): #morning
        hr = hr
        greeting = "morning"
        ampm = "am"
    elif(hr>=12 and hr <1): #afternoon
        hr = hr-12
        greeting = "afternoon"
        ampm = "noon"
    elif(hr>12 and hr <19): #evening
        hr = hr-12
        greeting = "evening"
        ampm = "pm"
    else:
        hr = hr -12
        greeting = "night"
        ampm = "pm"
    return [str(hr) + 'O' + str(now.minute), ampm, ' in the ', greeting]


def morning_greetings():
    speech.say ("Good Morning.")
    speech.say(" It is "+''.join(getCurrentTime()))
    speech.say(Weather.getCurrentWather())
    check_mails()

def check_mails():
    speech.say("Checking mails. Please wait ...")
    count = ReadMail.getUnreadMailCount()
    if (count <= 0):
        speech.say("You have NO unread mails")
    else:
        speech.say("You have "+ str(count) + " unread mails")

def handleCallback(phrase, listner):
    #speech.say('You said %s' % phrase)
    
    if phrase == "jarvis" or phrase == "jaiss":
        print (phrase)
        speech.say("Yes Boss")
        
    elif phrase == "are you up":
        speech.say("definitely. at your service sir!")
        
    elif phrase == "what is the current time":
        speech.say(getCurrentTime())
    
    elif phrase == "turn off":
        print (phrase)
        speech.say("Turning Off")
        listner.stoplistening()
        
    elif phrase == "how are you":
        print (phrase)
        speech.say("I am good. Thank you. How are you.")
        
    elif phrase == "read news":
        print (phrase)
        feeds = speakWebPage.readFeeds()
        speech.say(feeds)
    
    elif phrase == "show my feeds":
        print (phrase)
        speech.say("Launching Google Reader")
        os.system("C:\Users\kshwetabh\AppData\Local\Google\Chrome\Application\chrome.exe reader.google.com")
        
    elif phrase == "how is the weather outside":
        speech.say("Getting current weather. Please wait...!")
        print (phrase)
        speech.say(Weather.getCurrentWather())
    
    elif phrase == "get me the weather forecast":
        speech.say("Getting weather forecast. Please wait...!")
        print (phrase)
        speech.say("This week's weather forecast:")
        for item in Weather.getWeatherForecast():
            speech.say(item)
    
    elif phrase == "any new mails":
        check_mails()
        print (phrase)
                        
    elif phrase == "morning greetings":
        morning_greetings()
    
    else:
        print (phrase)
        speech.say("Could not understand, please repeat")


listner = speech.listenfor(['jarvis', 'jaiss', 'turn off',
                            'how are you', 'read news', 
                            'stop' , 'show my feeds', 
                            'what is the current time', 
                            'are you up', 'how is the weather outside', 
                            'get me the weather forecast', 
                            'any new mails', '*', 'morning greetings'], handleCallback)

import time

while listner.islistening():
    time.sleep(1)
    #print "Waiting for Command"