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
    "twelwe": (12, 0),
    "thirteen": (13, 1),
    "fifteen": (15, 1),
    "twenty": (20, 1),
    "thirty": (30, 1),
    "fifty": (50, 1),
    "hundred": (10**2, 2),
    "thousand": (10**3, 2),
    "million": (10**6, 2),
    "billion": (10**9, 2),
    "trillion": (10**12, 2),
    "quadrillion": (10**15, 2)
}

def stringtonumber(text):
    try:
      text_lower = text.lower() # make text lowercase

      text_list = text_lower.split() # split the seperated texts in a list

      sum = 0
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
                  else:
                      sum += value[0]
                      break # Breaks the inner loop
      
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

