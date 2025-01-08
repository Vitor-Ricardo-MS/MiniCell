from package.controllers.CalcControl import CalcControl
from package.controllers.ContControl import ContControl
from package.controllers.TeleBotCont import TeleBotCont

class mainMenu:
 
 def __init__(self):
   
   self.cont = ContControl()
   self.calc = CalcControl()
   self.bot = TeleBotCont()
   
   self.opcoes = {
    'calc': self.calc.startMenu,
    'cont' : self.cont.startMenu,
    'msg' : self.bot.startMenu,
    'menu' : self.showMenu,
    'fechar' : exit
   }
   
 def showMenu(self):
  print(f'\n--------------------------------------------------------------------------\n\nMinicell\n\n' + 'Apps:\n\n' + 
  'Calculadora simples: calc\n' + 
  'Contatos: cont\n' + 
  'Mensagens (Telegram Bot): msg\n\n' +
  'Fechar o Programa: fechar\n\n----------\n')
 
 def startMenu(self):
  self.showMenu()
  self.menu()
 
 def menu(self):
  entrada = input('Digite a opção desejada: ')
  nome = self.opcoes.get(entrada, self.default)
  nome()
  self.default()
 
 def default(self):
  self.startMenu() 
