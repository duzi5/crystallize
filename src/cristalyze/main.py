import json
import uuid
import os

class Model():
    def __init__( self, nome_da_pasta, *colunas):
        self.dici = []
        self.colunas = colunas
        os.mkdir(nome_da_pasta)
        self.nome_da_pasta = nome_da_pasta

    def create(self, *valores):
        dici = dict(zip(self.colunas, valores))
        id = str(uuid.uuid4())
        dici["id"] = id
        jason = json.dumps(dici, indent=4) 
        with open(f'{self.nome_da_pasta}/{id}.json', 'w') as arquivo:
            arquivo.write(jason)
        
    def update(self, chave, valor):
        self.dici[chave] = valor
    
    def delete_all(self):
        self.dici.clear()

    def read(self):
        print(self.dici)
        return self.dici

    def find(self, id): 
        files = os.listdir(self.nome_da_pasta)
        nome_arquivo = f'{id}.json'
        for filename in files:
            if filename == nome_arquivo:
                with open(self.nome_da_pasta, 'r') as arquiv:
                    x = json.load(arquiv)
                return x    
            else: 
                print('documento não encontrado')
    
    def find_atribute(self, atributo, valor):
        files = os.listdir(self.nome_da_pasta)
        for filename in files:
            with open(f'{self.nome_da_pasta}/{filename}', 'r') as arquiv: 
                x = json.load(arquiv)
                if x[atributo] == valor:
                    return x
                else:
                    return "Não há registros para esse filtro de busca."

