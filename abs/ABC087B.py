inputs = []
for i in range(4):
    inputs.append(int(input()))

a, b, c, x = inputs

print(
  sum(
    [500*i+100*j+50*k==x
       for i in range(a+1)
       for j in range(b+1)
       for k in range(c+1)]
   )
)