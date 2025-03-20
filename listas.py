# Defina uma lista com a idade de 10 atletas
#
# - Itere pela lista (usando o for)
#   - Se for menor de idade, imprimir menor de idade
#   - Se for maior de idade, imprimir maior de idade

# Definindo a lista
integrantes = ['alex', 'victor', 'felipe', 'luis']
print(integrantes)
print(len(integrantes))

# Vendo o tamanho da lista
tamanho = len(integrantes)
print(tamanho)

# Pegando um elemento específico da lista
print(integrantes[3])

# Adicionando um elemento na lista
integrantes.append('haroldo')
print(integrantes)
print(len(integrantes))

# Removendo um elemento da lista
integrantes.remove('luis')
print(integrantes)
print(len(integrantes))

# Iterando na lista
for integrante in integrantes:
    print(integrante)
