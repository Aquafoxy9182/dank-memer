#import revelant modules
from re import X
import time
import pyautogui
import itertools
import random
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
import termcolor
from win32gui import GetWindowText, GetForegroundWindow
import os
from selenium import webdriver

 #----------------------------------------var--------------------------#

#st = str(0) #the input 

count = 0 #the count of repeats

randnum = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8", "9", "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" , "19" , "20" ,]

sellcount = 0 # the count of sell

timer = 1800 # a timer
 
 #--------------------------------------define------------------------------#

#def isDivisibleBy5(st) :# usles now just keeping for refrens code 
    #n = len(st)
    #return ( (st[n-1] == '0') or #if the last number is 0 yes
           #(st[n-1] == '5')) #if the last number is 5 yes

 #--------------------------------------------------------------------#

def deposit():  #anti tieft program 
    time.sleep(10) #the time per repeat 

    print('Executing "pls deposit"')
    text = open ('deposit.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

 #--------------------------------------------------------------------#
 
#def sendSpambot(): #does the pls comands 
    #time.sleep(35) #the time per repeat 

    #text = open ('cumt.txt')
    #for each_line in text:
        #pyautogui.typewrite(each_line)
        #pyautogui.press('enter')  

def sendSpambot(): #does the pls comands 
     
    hunt()
    time.sleep(2)#so it don't skip anything
    fish()
    time.sleep(2) 
    beg()
    time.sleep(2) 
    dig()
    time.sleep(2) 
    guess()
    time.sleep(13) #the time per repeat  

 #--------------------------------------------------------------------#

def sell():#sell's all items 
    print('Executing "sell"')
    keyboard = Controller()
    keyboard.type('pls sell Ant max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Boar max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Fresh Bread max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Cookie max')
    keyboard.press(Key.enter) 
    time.sleep(5)
    keyboard.type('pls sell Deer max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Duck max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Exotic Fish max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Common Fish max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Garbage max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Jelly Fish max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Ladybug max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Rabbit max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Seaweed max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Skunk max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Stickbug max')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('pls sell Worm max')
    keyboard.press(Key.enter)
    time.sleep(3)

 #--------------------------------------------------------------------# 

def clock1():
    timer = timer + 35
    
def clock2():
    timer = timer + 45

def clock3():
    timer = timer + 88       
 
 #---------------------------------------------basic comands------------------#

def hunt():
    print('Executing "pls hunt"')
    keyboard = Controller()
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    
def fish():
    print('Executing "pls fish"')
    keyboard = Controller()
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    
def beg():
    print('Executing "pls beg"')
    keyboard = Controller()
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    
def guess():
    print('Executing "pls guess"')
    keyboard = Controller()
    keyboard.type('pls guess')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('hint')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type(random.choice(randnum))
    keyboard.press(Key.enter)

def dig():
    print('Executing "pls dig"')
    keyboard = Controller()
    keyboard.type('pls dig')
    keyboard.press(Key.enter)   

def pm():
    print('executing "pls pm"')     
    keyboard = Controller()
    keyboard.type('pls pm')
    keyboard.press(Key.enter)

def Lucky():
    print('executing "pls lucky"') 
    keyboard = Controller()
    keyboard.type('pls use Lucky Horseshoe')
    keyboard.press(Key.enter)
 #-----------------------------------script---------------------------------------#
 
num = y = 1000000 # how many times it reapets 
for _ in itertools.repeat(None, num):
 if timer == 1800 or timer > 1800 :
     Lucky()
     timer = 0 
     
 elif timer < 1800 :
   if sellcount == 20 or sellcount > 20 : # does the sell 
       print(sellcount)
       sell()
       deposit()
       clock3
       sellcount = 0

   elif sellcount < 20 :    
     if count == 5 : # does the deposit into discord
       print(sellcount)  
       print(count)
       sendSpambot()
       deposit()
       clock2()
       count = 0

     elif count < 5 : # does the comands into discord
       print(sellcount) 
       print (count)
       sendSpambot()
       clock1()
       count = count + 1 # does the count + 1
       sellcount = sellcount + 1 # does the count of sell + 1 
  
#----------------------------------end-of-code----------------------------------#
