"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

todaysmonth = month_name[todaymonth]

name=str(input("Hello, what is your name? "))
month=str(input("Hi {0}, what was the name of the month you were born in? ".format(name)))
year=int(input("And what year were you born in, {0}? ".format(name)))
day=int(input("And the day? "))

month=month.lower()
todaysmonth=todaysmonth.lower()
fall=["september","october", "november"]
winter=["december", "january", "february"]
spring=["march","april","may"]
summer=["june", "july", "august"]

if month == todaysmonth and day == todaydate:
    print("Happy Birthday!")
elif month == "october" and day == 31:
    print("You were born on Halloween!")
elif month in fall and year < 1980:
    print("{0}, you are a fall baby of the stone age.".format(name))
elif month in fall and year <1990:
    print("{0}, you are a fall baby of the eighties.".format(name))
elif month in fall and year <2000:
    print("{0}, you are a fall baby of the nineties.".format(name))
elif month in fall and year >=2000:
    print("{0}, you are a fall baby of the two thousands.".format(name))
elif month in winter and year < 1980: #winter
    print("{0}, you are a winter baby of the stone age.".format(name))
elif month in winter and year <1990:
    print("{0}, you are a winter baby of the eighties.".format(name))
elif month in winter and year <2000:
    print("{0}, you are a winter baby of the nineties.".format(name))
elif month in winter and year >=2000:
    print("{0}, you are a winter baby of the two thousands.".format(name))
elif month in spring and year < 1980: #spring
    print("{0}, you are a spring baby of the stone age.".format(name))
elif month in spring and year <1990:
    print("{0}, you are a spring baby of the eighties.".format(name))
elif month in spring and year <2000:
    print("{0}, you are a spring baby of the nineties.".format(name))
elif month in spring and year >=2000:
    print("{0}, you are a spring baby of the two thousands.".format(name))
elif month in summer and year < 1980: #spring
    print("{0}, you are a summer baby of the stone age.".format(name))
elif month in summer and year <1990:
    print("{0}, you are a summer baby of the eighties.".format(name))
elif month in summer and year <2000:
    print("{0}, you are a summer baby of the nineties.".format(name))
elif month in summer and year >=2000:
    print("{0}, you are a summer baby of the two thousands.".format(name))


    
    
    