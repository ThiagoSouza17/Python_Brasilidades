from acesso_cep import BuscaEndereco
import re

cep = 49500217
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

logradouro, bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(logradouro+",", bairro,"-", localidade + "/" + uf)



