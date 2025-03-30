import math
raio = float(input("Entre com o valor do raio:"))
area = 3.14 * raio * raio
if area<0:
    print ("Não é possível calcular")
else:
    print ("A area da circunferencia é:",area)