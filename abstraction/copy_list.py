names = ['Peng Lin', 'Kang Lieyong']
n = names[:]

print(n is names)
print(n == names)
n[0] = 'Peng Shasha'
print(n)
