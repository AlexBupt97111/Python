A=[True]*150 #за замовчуванням всі числа - прості; 150 - межа (не включно)
A[0]=A[1]=False #нульовий та перший елемент в даній вибірці  - не прості, тому каскадним присвоєнням - значення Брехня
for k in range(2,150):#від 2 (тому що 1 має лише 1 дільник+воно ні просте ні складене) до 150 не включно
  if A[k]:#якщо A[k] -правда- то це число просте і кратні йому числа(k*k) - не прості
    for m in range(k*k,150,k):#цикл де індексом m  в діапазоні від k до 150 пробігаємся кроком k
     A[m]=False#
for k in range(150):#
  print(k,"-","просте" if A[k] else"складене")#"-"- тернарний оператор (прямо в Print-е)
  
