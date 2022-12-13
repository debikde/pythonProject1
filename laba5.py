class Calculator:
  def __init__(self):
    pass

  def summ(self, x1, x2):
    return x1 + x2

  def multiply(self, x1, x2):
    return x1 * x2


  def minus(self, x1, x2):
    return x1 - x2

  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2
    else:
      return "error: x = 0"



# print("Введите число")
# x = int(input())
x = 8
# print("Введите действие")
# comand = input()
comand = "+"
# print("Введите второе число")
# x2 = int(input())
x2 = 10
calc = Calculator()
if comand == "+":
  print("ответ=", calc.summ(x,x2))

if comand == "-":
  print("ответ=",calc.minus(x,x2))

if comand == "*":
  print("ответ=",calc.multiply(x,x2))

if comand == "/":
  print("ответ=",calc.divide(x,x2))

