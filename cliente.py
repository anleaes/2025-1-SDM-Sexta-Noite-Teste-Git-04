class Cliente:
 def __init__ (self , nome, endereco, idade ):
  self._nome = nome 
  self._endereco = endereco
  self._idade = idade

  def Usuario (self):
    return f"Usuario: {self.nome}\nEndereço:{self.endereço}"