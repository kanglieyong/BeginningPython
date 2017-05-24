fibs = [0, 1]
num = input('How many Fibonacci number do you want? ')
for i in range(int(num)-2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
