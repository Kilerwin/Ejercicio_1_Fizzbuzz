#código Fizz Buzz

for i in range(1,1001):
  output = ("Fizz" if i % 3 == 0 else "") + ("buzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "")
  print(output or i)