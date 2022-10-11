import re


def Grosspay(Hours,rate):
   Pay=Hours*rate
   return Pay

Hours=int(input("Enter your Working Hours Here: "))
rate=float(input("Enter your Rate of payment Here: "))
print("GrossPay: ", Grosspay(Hours,rate))
