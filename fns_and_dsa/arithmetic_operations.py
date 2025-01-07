def perform_operation(num1, num2, operation):
   if operation == "add":
      return num1 + num2
   elif operation == "subtract":
      return num1 - num2
   elif operation == "divide":
      if num2 == 0:
         return "error, number not divisible by 0"
      else:
        return num1/num2
   elif operation == "multiply":
      return num2 *num1
   else:
      return "Invalid operation"
# perform_operation("num1, num2, operation")
      

