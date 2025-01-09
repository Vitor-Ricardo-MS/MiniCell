from package.models.Calculadora import Calculadora

class CalcControl:
 
 def __init__(self):
  
  Calc = Calculadora
  self.opcoes = {
   'soma': Calc.soma,
   'sub' : Calc.sub,
   'mult': Calc.mult,
   'div' : Calc.div,
   'pot' : Calc.pot,
   'fat': Calc.fatorial,
   'mod' : Calc.mod,
   'somarM': Calc.addM,
   'somarRespM': Calc.addMResp,
   'subM': Calc.subM,
   'subRespM': Calc.subMResp,
   'exibirM': Calc.showM,
   'menu' : self.showMenu,
   'sair' : self.end
  }
 
 def showMenu(self):
  print(f'\n--------------------------------------------------------------------------\n\nCalculadora\n\n' + 'Opções:\n\n' + 
  'Somar 2 números: soma\n' + 
  'Subtrair 2 números: sub\n' + 
  'Multiplicar 2 números: mult\n' + 
  'Dividir 2 números: div\n' + 
  'Achar o mod n de um numero: mod\n' +
  'Elevar um número a alguma potência: pot\n' +
  'Achar o fatorial de um número: fat\n'
  'Somar um número ao M: somarM\n' + 
  'Somar a resposta anterior ao M: somarRespM\n' +
  'Subtrair um número do M: subM\n' +
  'Subtrair a resposta anterior do M: subRespM\n' +
  'Exibir M : exibirM\n\n' +
  'Exibir menu novamente: menu\n' +
  'Sair do App: sair\n\n--------------------------------------------------------------------------\n')
 
 def startMenu(self):
  self.showMenu()
  self.menu()
 
 def menu(self):
  entrada = input('Digite a opção desejada: ')
  nome = self.opcoes.get(entrada, self.default)
  nome()
  if(entrada == "sair"):
   return False
  self.default()
   
 def end(self):
  return False
 
 def default(self):
  self.menu()

