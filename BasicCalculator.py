# Author:
# Agyeya Mishra
# Department of Civil Engineering
# Delhi Technological University (formerly, Delhi College of Engineering)
# New Delhi, India

import sys
from Functions import *
#Python program to create a simple calculator 

for line in sys.stdin:
    line = line.rstrip()

    #My Contribution Error Handling
    #Now Supports Floating Numbers
    #Will Catch invalid Input(e.g. abc +2)
    if line.lower() in ["quit", "exit"]:
       print("Exiting calculator...")
       exit()


    try:  
        if '+' in line:
            nums = line.split('+')
            print(add(float(nums[0]), float(nums[1])))
        elif '-' in line:
            nums = line.split('-')
            print(subtract(float(nums[0]), float(nums[1])))
        elif '*' in line:
            nums = line.split('*')
            print(multiply(float(nums[0]), float(nums[1])))
        elif '/' in line:
            nums = line.split('/')
            denominator = float(nums[1])
            if denominator == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(divide(float(nums[0]),denominator)) 
        elif '%' in line:
            nums = line.split('%')
            print(mod(float(nums[0]), float(nums[1])))
        elif '^' in line:
            nums = line.split('^')
            print(exponent(float(nums[0]), float(nums[1])))
        else:
            print("This mathematical expression is either wrong or not supported.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")            
    
  
