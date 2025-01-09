import asyncio

from package.models.TeleBot import TeleBot
from package.controllers.DataRecord import DataRecord

class TeleBotCont:
 
 def __init__(self):
  
  self.opcoes = {
   'msg': self.speak,
   'newid': self.save_chatid,
   'menu' : self.showMenu
  }
 
 def showMenu(self):
  print(f'\n--------------------------------------------------------------------------\n\nMensagens (MiniCell Bot)\n\n' + 
  'Opções:\n\n' + 
  'Enviar uma mensagem: msg\n' +
  'Salvar um novo ID do telegram: newid\n\n' +
  'Exibir menu novamente: menu\n' +
  'Sair do App: sair\n\n----------\n')
 
 def startMenu(self):
  self.showMenu()
  self.menu()
 
 def menu(self):
  entrada = input('Digite a opção desejada: ')
  nome = self.opcoes.get(entrada, self.default)
  if(entrada == "sair"):
   return False
  self.pessoas = DataRecord("dataContatos.json")
  nome()
  self.default()
 
 def default(self):
  self.menu()
  
 def speak(self):
  pessoa = input('\nDigite o nome completo da pessoa a ser contatada: ')
  	
  if self.pessoas.verify_name(pessoa):
   chatid = self.pessoas.return_param(pessoa, 'teleid')
  else:
   print(f'Essa pessoa não existe.\n')
   return False

  self.bot = TeleBot()
 	
  mensagem = input('\nDigite a mensagem a ser enviada: ')
  asyncio.run(self.bot.speak(mensagem, chatid))
  
  print(f'\n----------\n')
  
  del self.bot
  
  return True
  
 def save_chatid(self):
  pessoa = input('\nDigite o nome compĺeto da pessoa a ser salvada: ')
  
  if self.pessoas.verify_name(pessoa):
   self.bot = TeleBot()
   
   print(f'\nMande uma mensagem para o bot @MiniVit_bot, pelo celular do(a) {pessoa}, e depois escreva "enviado": ')
   test = input()
   
   if test != 'enviado':
    print(f'\nResposta inesperada!')
    return False
   
   tempid = asyncio.run(self.bot.save_chatid())
   
   self.pessoas.change_param_auto(pessoa, 'teleid', tempid)
   pessoasa = self.pessoas.save()
   
   del self.bot
   
   return True
  else:
   print(f'Essa pessoa não existe.\n')
   return False
