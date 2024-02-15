l=[100,200,300,400,500,300,400,700,100,400]
x = {}
for i in range(len(l)-2):
  for j in range(i,len(l)-2):
	x[(i,j+2)] = l[i] + l[j+2]
print(max(x.values()))