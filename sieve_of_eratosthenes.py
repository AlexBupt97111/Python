A = [True] * 150
A[0] = A[1] = False
for k in range(2, 150):
  if A[k]:
    for m in range(k * k, 150, k):
     A[m] = False
for k in range(150):
  print(k,"-","просте" if A[k] else"складене")
  
