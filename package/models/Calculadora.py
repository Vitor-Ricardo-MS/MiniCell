class Calculadora:
 resposta = 0
 M = 0

 @staticmethod
 def soma():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)

  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = float(y)
  
  resp = a+b
  print(f'A soma de {a} e {b} é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def mult():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)

  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = float(y)
  
  resp = a*b
  print(f'O produto de {a} e {b} é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def sub():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)

  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = float(y)
  
  resp = a-b
  print(f'A diferença entre {a} e {b} é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def div():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)

  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = float(y)
  
  resp = a/b
  print(f'A razão entre {a} e {b} é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def pot():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = int(x)
   
  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = int(y)
  
  resp = a**b
  print(f'{a} elevado a {b} é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def fatorial():
  x = input('Digite 1 número: ')
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = int(x)
  
  resp = a
  a -= 1
  while(a > 0):
   resp *= a
   a -= 1
  print(f'{a} fatorial é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def mod():
  x, y = input('Digite 2 números: ').split()
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)

  if y == "Resp":
   b = Calculadora.resposta
  elif y == "M":
   b = Calculadora.M
  else:
   b = float(y)
  
  resp = a%b
  print(f'A valor de {a} (mod {b}) é: {resp}')
  Calculadora.resposta = resp
  
 @staticmethod
 def addM():
  x = input('Digite 1 número: ')
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)
  
  Calculadora.M += a
  print(f'{a} foi adicionado a M')
  
 @staticmethod
 def addMResp():
  Calculadora.M += Calculadora.resposta
  print(f'{Calculadora.resposta} foi adicionado a M')
  
 @staticmethod
 def subM():
  x = input('Digite 1 número: ')
  
  if x == "Resp":
   a = Calculadora.resposta
  elif x == "M":
   a = Calculadora.M
  else:
   a = float(x)
  
  Calculadora.M -= a
  print(f'{a} foi subtraido de M')
  
 @staticmethod
 def subMResp():
  Calculadora.M -= Calculadora.resposta
  print(f'{Calculadora.resposta} foi subtraido de M')
  
 @staticmethod
 def showM():
  print(f'O valor atual de M é: {Calculadora.M}')


