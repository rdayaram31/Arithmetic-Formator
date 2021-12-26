import re
def arithmetic_arranger(problems,solve=False):
  # for to many problems
  if len(problems)>5:
      return "Error: Too many problems."
      
  f_line = ""
  s_line = ""
  d_line = ""
  sum_line = ""
  arranged_problems=""
  # 
  
  for value in problems:
      operator=re.search('[/]',value) or re.search('[*]',value)
      # for operator error Check
      if operator:
          return "Error: Operator must be '+' or '-'."
      # for digit Error check
      char=re.search('[a-z]',value)
      if char:
          return "Error: Numbers must only contain digits."
      firstNumber = value.split(" ")[0]
      operator = value.split(" ")[1]
      secondNumber = value.split(" ")[2]
      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
          return "Error: Numbers cannot be more than four digits."
      # calculating the values
      sum = ""
      if(operator == "+"):
          sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
          sum = str(int(firstNumber) - int(secondNumber))
      # modifing the digit to string value and adjusting with right corner
      length = max(len(firstNumber),len(secondNumber))+2
      top_str = str(firstNumber).rjust(length)
      bottom_str = operator + str(secondNumber).rjust(length-1) 
      line = "-"*length
      result = str(sum).rjust(length)

      # for x in range(length):
      #     line += "-"
    
      if value != value[-1]:
          f_line += top_str + "    "
          s_line += bottom_str + "    "
          d_line += line + "    "
          sum_line += result + "    "
      else:
        f_line += top_str 
        s_line += bottom_str 
        d_line += line 
        sum_line += result 

  if solve :
      arranged_problems = f_line + "\n" + s_line + "\n" + d_line + "\n" + sum_line
  else:
      arranged_problems = f_line + "\n" + s_line + "\n" + d_line
  return arranged_problems


