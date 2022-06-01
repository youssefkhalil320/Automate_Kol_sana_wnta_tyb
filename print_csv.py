import csv
import pywhatkit as w
import time
import pyautogui
import keyboard as k
poll_path = r"E:\python\whatssapp\whatssapp-sender-main\numbers.csv"
timee_hours =int(input("Please Enter the hour"))
timeee = int(input("Please Enter the minutes"))
coun_code = input("please enter the country code")
 
with open(poll_path, newline=None) as csvfile:
    csvreader = csv.reader(csvfile)
    for name, number in csvreader:
        w.sendwhatmsg(coun_code+number, f" {name} كل سنة و انت طيب يا ", timee_hours, timeee)
        timeee = timeee+1
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')
        time.sleep(2)
        pyautogui.keyDown('alt')
        pyautogui.keyDown('f4')
        time.sleep(.5)
        pyautogui.keyUp('f4')
        pyautogui.keyUp('alt')
