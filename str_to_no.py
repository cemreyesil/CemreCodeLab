import re

numbers = {
    "one": (1, 0),
    "two": (2, 0),
    "three": (3, 0),
    "four": (4, 0),
    "five": (5, 0),
    "six": (6, 0),
    "seven": (7, 0),
    "eight": (8, 0),
    "nine": (9, 0),
    "ten": (10, 0),
    "eleven": (11, 0),
    "twelve": (12, 0),
    "thirteen": (13, 1),
    "fifteen": (15, 1),
    "twenty": (20, 1),
    "thirty": (30, 1),
    "forty": (40, 1),
    "fifty": (50, 1),
    "hundred": (10**2, 2),
    "thousand": (10**3, 3),
    "million": (10**6, 3),
    "billion": (10**9, 3),
    "trillion": (10**12, 3),
    "quadrillion": (10**15, 3)
}

def stringtonumber(text):
    try:
      text_lower = text.lower().strip() # make text lowercase
      text_list = re.split(r'[\s-]+', text_lower)  # Handle spaces and hyphenated numbers like "twenty-five"

      sum = 0
      sumlist = []
      for no in text_list:
          for key, value in numbers.items():
              if no.find(key) != -1:
                  if "teen" in no and value[1] == 0:
                      sum += value[0]+10
                      break # Breaks the inner loop
                  elif "ty" in no and value[1] == 0:
                      sum += value[0]*10
                      break # Breaks the inner loop
                  elif value[1] == 2:
                      sum *= value[0]
                      break # Breaks the inner loop
                  elif value[1] == 3:
                      sum *= value[0]
                      sumlist.append(sum)
                      sum = 0
                  else:
                      sum += value[0]
                      break # Breaks the inner loop
                  
      if len(sumlist) != 0:
          for x in sumlist:
              sum += x
      
      if sum == 0:
          return None # Number entered wrongly
      
      number = sum
      fixed_number = str(number)
      count = 0
      index = len(fixed_number)
      while number != 0:
          if count % 3 == 0 and count != 0:
              fixed_number = fixed_number[:index] + ',' + fixed_number[index:] # Add coma to specific part of the text ex: 5000 -> 5,000

          number = number // 10 
          count += 1
          index -= 1

      return fixed_number
    except Exception as e:
        print(e)

print(stringtonumber("one million two HUNDred thirty-four thousand five hundred sixty-seven"))
