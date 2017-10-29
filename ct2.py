# Import all libraries 
# step 0
# step 1
# step 2
# step 3
# step 4
import os
import pdb
import datetime
import SystemTime
import Relays
import RPi.GPIO as GPIO
import time
# Pin definitions 
rel1 = 18 # Relay 1 Q_PP001 pump water 
rel2 = 19 # Relay 2 Q_PP002 pump dosifier
rel3 = 20 # Relay 3 Q_PP003 pump irrigation
rel4 = 21 # Relay 4 Q_XV001 irrigation zone A 
rel5 = 22 # Relay 5 Q_XV002 irrigation zone B
rel6 = 23 # Relay 6 Q_XV003 irrigation zone C
rel7 = 24 # Relay 7 Q_XV004 irrigation zone D
rel8 = 25 # Relay 8 Q_XV005 irrigation injector A
rel9 = 26 # Relay 9 Q_XV006 irrigation injector B
rel10 = 27 # Relay 10 Q_XV007 irrigation injector C / Acid
# GPIO definition
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rel1,GPIO.OUT)
GPIO.setup(rel2,GPIO.OUT)
GPIO.setup(rel3,GPIO.OUT)
GPIO.setup(rel4,GPIO.OUT)
GPIO.setup(rel5,GPIO.OUT)
GPIO.setup(rel6,GPIO.OUT)
GPIO.setup(rel7,GPIO.OUT)
GPIO.setup(rel8,GPIO.OUT)
GPIO.setup(rel9,GPIO.OUT)
GPIO.setup(rel10,GPIO.OUT)
#~ rel1_on = GPIO.output(rel1, GPIO.LOW)
#~ rel1_off = GPIO.output(rel1, GPIO.LOW)
#~ rel2_on = GPIO.output(rel1, GPIO.LOW)
#~ rel2_off = GPIO.output(rel1, GPIO.LOW)
#~ rel3_on = GPIO.output(rel1, GPIO.LOW)
#~ rel3_off = GPIO.output(rel1, GPIO.LOW)
#~ rel4_on = GPIO.output(rel1, GPIO.LOW)
#~ rel4_off = GPIO.output(rel1, GPIO.LOW)
#~ rel5_on = GPIO.output(rel1, GPIO.LOW)
#~ rel5_off = GPIO.output(rel1, GPIO.LOW)
#~ rel6_on = GPIO.output(rel1, GPIO.LOW)
#~ rel6_off = GPIO.output(rel1, GPIO.LOW)
# RTC definition 
# Relay class definition 
# Relays.DisplayRelayStates(1)





# Read characters to active relays, off = kill all relays 
# each charactter actives a relay, just one relay is activated at a time 
list1 = [rel1,rel2,rel3,rel4,rel5,rel6,rel7,rel8,rel9,rel10]

while 1 :


        var= raw_input('Enter relay # or kill entering off: ')
        if var == ' ' :
                GPIO.output(rel1, GPIO.LOW)
                GPIO.output(rel2, GPIO.LOW)
                GPIO.output(rel3, GPIO.LOW)
                GPIO.output(rel4, GPIO.LOW)
                GPIO.output(rel5, GPIO.LOW)
                print('OFF')
                
	
	if var == '1' :
                GPIO.output(rel1, GPIO.HIGH)
                print('relay 1 = ON')
        else:
                GPIO.output(rel1, GPIO.LOW)
                print('relay 1 = OFF')	
	if var == '2' :
                GPIO.output(rel2, GPIO.HIGH)
                print('relay 2 = ON') 	     
        else:
                GPIO.output(rel2, GPIO.LOW)
                print('relay 2 = OFF')	     	
	if var == '3' :
                GPIO.output(rel3, GPIO.HIGH)
                print('relay 3 = ON') 	     
        else:
                GPIO.output(rel3, GPIO.LOW)
                print('relay 3 = OFF')		
	if var == '4' :
                GPIO.output(rel4, GPIO.HIGH)
                print('relay 4 = ON') 	     
        else:
                GPIO.output(rel4, GPIO.LOW)
                print('relay 4 = OFF')	
	if var == '5' :
                GPIO.output(rel5, GPIO.HIGH)
                print('relay 5 = ON') 	     
        else:
                GPIO.output(rel5, GPIO.LOW)
                print('relay 5 = OFF')			
	if var == '6' :
                GPIO.output(rel6, GPIO.HIGH)
                print('relay 6 = ON') 	     
        else:
                GPIO.output(rel6, GPIO.LOW)
                print('relay 6 = OFF')	
	if var == '7' :
                GPIO.output(rel7, GPIO.HIGH)
                print('relay 7 = ON') 	     
        else:
                GPIO.output(rel7, GPIO.LOW)
                print('relay 7 = OFF')	     	     
	if var == '8' :
                GPIO.output(rel8, GPIO.HIGH)
                print('relay 8 = ON') 	     
        else:
                GPIO.output(rel8, GPIO.LOW)
                print('relay 8 = OFF')	
	if var == '9' :
                GPIO.output(rel9, GPIO.HIGH)
                print('relay 9 = ON') 	     
        else:
                GPIO.output(rel9, GPIO.LOW)
                print('relay 9 = OFF')
	if var == '10' :
                GPIO.output(rel10, GPIO.HIGH)
                print('relay 10 = ON') 	     
        else:
                GPIO.output(rel10, GPIO.LOW)
                print('relay 10 = OFF')
	if var == 'off' :
                for word in list1:
                        GPIO.output(word, GPIO.LOW)
                        print ('relays off ' + str(word)) 
	if var == 'quit' : break 


