#https://codereview.stackexchange.com/questions/276565/solution-to-arithmetic-arranger-from-freecodecamp
def arithmetic_arranger(problems, solver=False):
  #If problems exceed 5 return error
  if len(problems) > 5:
        return "Error: Too many problems."
   
  topTier = ""
  bottomTier = ""
  operator = ""
  lines = ""
  totals = ""
  for n in problems:
    topNumber = n.split()[0]
    bottomNumber = n.split()[2]
    op = n.split()[1]
    
  #If problem is not "+" or "-" return error
  if op =! "+" and op =! "-":
    return "Error: Operator must be '+' or '-'."
  
  #If problem does not contain number return error
  if not topNumber.isdigit() or not bottomNumber.isdigit():
    return "Error: Numbers must only contain digits."
  
  #If number exceeds 4 four digits return error
  if topNumber > 4 or bottomNumber > 4:
    return "Error: Numbers cannot be more than four digits."
    
    
