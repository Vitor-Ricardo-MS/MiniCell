from package.controllers.DataRecord import DataRecord
from package.models.Pessoa import Pessoa

class ContControl:
 
 def __init__(self):
   
   self.pessoas = DataRecord("dataContatos.json")
   self.opcoes = {
    'add': self.addPessoa,
    'exibir' : self.exibirPessoas,
    'param' : self.retornarParam,
    'alterar': self.mudarParam,
    'deletar' : self.deletarPessoa,
    'salvar' : self.salvarPessoas,
    'menu' : self.showMenu,
    'sair' : self.end
   }
   
 def showMenu(self):
  print(f'\n--------------------------------------------------------------------------\n\nContatos\n\n' + 'Opções:\n\n' + 
  'Adicionar contato: add\n' + 
  'Alterar contato: alterar\n' + 
  'Deletar contato: deletar\n' + 
  'Exibir contatos: exibir\n' +
  'Exibir um parâmetro de uma contato: param\n' + 
  'Salvar mudanças: salvar\n\n' +
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
 
 def addPessoa(self):
   print('')
   p = Pessoa()
 
   if not self.pessoas.verify_name(p.getNome()):
     self.pessoas.write(p)
     print(f'{p.getNome()} foi adicionado aos contatos!\n\n----------\n')
     return True
   else:
     print(f'{p.getNome()} já existe nos contatos!\n\n----------\n')
     return False
     
 def exibirPessoas(self):
   print(f"\nPessoas: ")
   pessoasa = self.pessoas.get_models()
   if pessoasa:
       for index, pessoasa in enumerate(pessoasa, start=1):
           print(f"{index}. Nome: {pessoasa['_Pessoa__nome']}, Número: {pessoasa['_Pessoa__numero']}, Email: {pessoasa['_Pessoa__email']}, TeleID: {pessoasa['_Pessoa__teleid']}\n")
       print('----------\n')
       return True
   else:
       print("Nenhuma pessoa cadastrada.\n\n----------\n")
       return False
       
 def mudarParam(self):
   nome = input('\nNome da pessoa à ser alterada: ')
   
   if self.pessoas.verify_name(nome):
     if (self.pessoas.change_param(nome)):
      return True
     return False
   else:
     print(f'Essa pessoa não existe.\n\n----------\n')
     return False
     
 def retornarParam(self):
   nome = input('\nNome da pessoa à ser alterada: ')
   
   if self.pessoas.verify_name(nome):
     param = input('\nQual parâmetro deseja exibir (nome, email, numero, teleid)? ')
   
     resp = self.pessoas.return_param(nome, param)
     
     print(f'O {param} do {nome} é: {resp}\n\n----------\n')
     return True
   else:
     print(f'Essa pessoa não existe.\n\n----------\n')
     return False
     
 def deletarPessoa(self):
   nome = input('\nNome da pessoa à ser deletada: ')
   
   if self.pessoas.verify_name(nome):
     if (self.pessoas.delete(nome)):
       return True
     return False
   else:
     print(f'Essa pessoa não existe.\n\n----------\n')
     return False
     
 def salvarPessoas(self):
   if(self.pessoas.save()):
    return True
   return False
