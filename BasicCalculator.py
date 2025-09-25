# Author:
# Agyeya Mishra
# Department of Civil Engineering
# Delhi Technological University (formerly, Delhi College of Engineering)
# New Delhi, India

import sys
import math
from Functions import *
#Python program to create a simple calculator 

# Store calculation history
history = []

for line in sys.stdin:
    line = line.rstrip()

    #My Contribution Error Handling
    #Now Supports Floating Numbers
    #Will Catch invalid Input(e.g. abc +2)
    if line.lower() in ["quit", "exit"]:
       print("Exiting calculator...")
       exit()
    
    # History recall New Contribution
    if line.lower() == "history":
        if history:
            print("Calculation History:", history)
        else:
            print("No history yet.")
        continue        
     
     # Replace "ans" with the last result if available 
    if "ans" in line and history:
        line = line.replace("ans", str(history[-1]))

    try:  
        if '+' in line:
            nums = line.split('+')
            result= add(float(nums[0]), float(nums[1]))
            print(result)
            history.append(result)

        elif '-' in line:
            nums = line.split('-')
            result = subtract(float(nums[0]), float(nums[1]))
            print(result)
            history.append(result)

        elif '*' in line:
            nums = line.split('*')
            result = multiply(float(nums[0]), float(nums[1]))
            print(result)
            history.append(result)

        elif '/' in line:
            nums = line.split('/')
            denominator = float(nums[1])
            if denominator == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = divide(float(nums[0]),denominator)
                print(result)
                history.append(result)

        elif '%' in line:
            nums = line.split('%')
            result = mod(float(nums[0]), float(nums[1]))
            print(result)
            history.append(result)

        elif '^' in line:
            nums = line.split('^')
            result = exponent(float(nums[0]), float(nums[1]))
            print(result)
            history.append(result)

        elif 'sqrt' in line:
            # My New COntribution: Square Root Function
            num_str = line.replace("sqrt", "").strip()
            num = float(num_str)
            if num < 0:
                print("Error: Cannot take square root of a negative number.")
            else:
                result = math.sqrt(num)
                print(result)
                history.append(result)

            
            # My New Contribution
        elif 'sin' in line:
            num_str = line.replace("sin", "").strip()
            num = float(num_str)
            result = math.tan(math.radians(num))  # degrees -> radians
            print(result)
            history.append(result)
        
        elif 'cos' in line:
            num_str = line.replace("cos", "").strip()
            num = float(num_str)
            result = math.cos(math.radians(num))
            print(result)
            history.append(result)  

        elif 'tan' in line:
            num_str = line.replace("tan", "").strip()
            num = float(num_str)
            result = math.tan(math.radians(num))
            print(result)
            history.append(result)            
        
        else:            
            print("This mathematical expression is either wrong or not supported.")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")            
    
  
