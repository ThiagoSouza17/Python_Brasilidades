from cpf_cnpj import Documento
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento2)

