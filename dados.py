import random;
res = input("Desea lanzar los dados: S/N\n");
while(res =='S'):
  dado1, dado2 = random.randint(1,6), random.randint(1,6)
  print("Tus dados son:" ,dado1,"y",dado2)
  suma = dado1 + dado2
  print("Su sumas es:", suma)
  res = input("Desea volver a lanzar los dados:S/N\n");
  if res == 'N':
    print("Te quedaste con los dados",dado1,"y",dado2)
    suma = dado1 + dado2
    print("Su sumas es:", suma)
