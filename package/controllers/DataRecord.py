import json

class DataRecord:
 
 def __init__(self, filename):
  self.__filename = "package/db/" +  filename
  self.__models = []
  self.read()
  
  self.mudarParam = {
   'nome': "_Pessoa__nome",
   'email' : "_Pessoa__email",
   'número': "_Pessoa__numero",
   'numero' : "_Pessoa__numero"
  }
  
  self.deletarPessoa = {
   'sim' : True,
   's' : True,
   'nao' : False,
   'não' : False,
   'n' : False,
   'y' : True
  } 
  
 def default(self):
  return False
 
 def read(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as fjson:
                self.__models = json.load(fjson)
        except FileNotFoundError:
            print(f"O arquivo {self.__filename} não existe!\n\n----------\n")
            self.__models = []
      
 def write(self, model):
        try:
            self.__models.append(vars(model))
        except Exception as e:
            print(f"Erro ao adicionar o modelo: {e}\n\n----------\n")
            
 def delete(self, name):
 	for index, model in enumerate(self.__models, start=0):
            if name == model["_Pessoa__nome"]:
                entrada = input(f'Certeza que deseja deletar {name}? ')
                param = self.deletarPessoa.get(entrada, self.default)
                if(param):
                 self.__models.pop(index)
                 print(f'{name} foi deletado com sucesso!\n\n----------\n')
                 return True
                print(f'{name} não foi deletado.\n\n----------\n')
                return False

 def verify_name(self,name):
        for model in self.__models:
            if name == model["_Pessoa__nome"]:
                return True
        return False
        
 def change_param(self,name):
        for model in self.__models:
            if name == model["_Pessoa__nome"]:
                entrada = input('Qual parâmetro deseja mudar (nome, email, número)? ')
                param = self.mudarParam.get(entrada, self.default)
                if(param != self.default):
                 newname = input(f'Insira o novo {entrada}: ')
                 model.update({param : newname})
                 print(f'Parâmetro mudado com sucesso!\n\n----------\n')
                 return True
                print(f'Falha ao mudar o parâmetro.\n\n----------\n')
                return False
                
 def change_param_auto(self,name, paramname, paramvalue):
        self.mudarParamAuto = {
           'nome': "_Pessoa__nome",
           'email' : "_Pessoa__email",
           'número': "_Pessoa__numero",
           'numero' : "_Pessoa__numero",
           'teleid' : "_Pessoa__teleid"
        }
 
        for model in self.__models:
            if name == model["_Pessoa__nome"]:
                param = self.mudarParamAuto.get(paramname, self.default)
                if(param != self.default):
                 model.update({param : paramvalue})
                 return True
                print(f'Falha ao mudar o parâmetro.\n\n----------\n')
                return False
                
 def return_param(self, name, parametro):
        self.returnParam = {
         'nome': "_Pessoa__nome",
         'email' : "_Pessoa__email",
         'número': "_Pessoa__numero",
         'numero' : "_Pessoa__numero",
         'teleid' : "_Pessoa__teleid"
        }
 
        param = self.returnParam.get(parametro, self.default)

        for model in self.__models:
            if name == model["_Pessoa__nome"]:
                return model[param]
        print(f'Falha ao mudar o parâmetro.\n\n----------\n')
        return False

 def save(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as fjson:
                json.dump(self.__models, fjson, indent=4, ensure_ascii=False)
            print(f'Dados salvos!\n\n----------\n')
            return True
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}\n\n----------\n")
            return False
 
 def get_models(self):
        return self.__models 
        
