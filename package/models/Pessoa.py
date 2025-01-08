class Pessoa:

 def __init__(self):
 
  self.setName()
  self.setNumber()
  self.setEmail()
  self.__teleid = "0"

 def setName(self):
  a = input('Nome da Pessoa: ')
  if(a == ""):
   self.__nome = ""
  else:
   self.__nome = a
  
 def setNumber(self):
  a = input('Número de celular: ')
  if(a == ""):
   self.__numero = ""
  else:
   self.__numero = a
  
 def setEmail(self):
  a = input('Email: ')
  if(a == ""):
   self.__email = ""
  else:
   self.__email = a
 
 def setTeleID(self):
  a = input('Id to Telegram (BOT MiniCell): ')
  if(a == ""):
   self.__teleid = ""
  else:
   self.__teleid = a
   
 def getNome(self):
  return self.__nome
  
 def getNumero(self):
  return self.__numero
  
 def getEmail(self):
  return self.__email
  
 def getTeleID(self):
  return self.__teleid

