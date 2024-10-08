# Write a program that allows users to enter numbers unless the user enters 1 and then display
#  the largest and smallest number respectively among all the numbers entered (including 1 as input).

num = []
while True:
  line = int(input())
  if line == 1:
    break
  try:
    num.append(line)
  except:
    print("Incorrect Input")
num.append(1)
print(max(num), min(num))


# arr = []
# while True:
#   try:
#     word = input()
#     if word == "exit":
#       break
#     else:
#       arr.append(word)
#   except:
#     print("please give exit in the input")
# arr.join(arr, " ")
# print(arr)