# declarando variável como ponto flutuante (decimal)
taxa_importacao = 0.35

# declarando variável como inteiro
quantidade_comprada = 10

# valor do produto
valor_produto = 100

# nome do produto
nome_produto = 'Produto Legal'

# valor bruto
valor_bruto = quantidade_comprada * valor_produto

# taxa de desconto
taxa_desconto = 0.8

# valor do imposto
valor_imposto = valor_bruto * taxa_importacao

# Estudar
#
# listas
# dicionários
#
# if, else,

produtos = {'654'   : 'Produto 1',
            '648'   : 'Produto 2'}

user_input = input("Coloque código do produto: ")
print(user_input)

print(produtos.get(user_input))












# Desafio:
#
# Declarar as seguintes variáveis, de acordo com as melhores práticas do Python (snake_case), descrevendo a variável
# de acordo com o que ela representa
#
# 1) Valor total da compra (bruto), sem impostos
# 2) Valor total da compra (líquido), com impostos
# 3) Valor total da compra, com desconto e impostos
# 4) Dar um print nestas variáveis
#
# Sinal de multiplicação: *
# Sinal de divisão:  /
# Numero decimal (composto)  usa ponto, exemplo: 0.5
# Soma: 1 + 1
# Subtrai: 3 - 2

#
#  # 1)
# valor_total_da_compra = quantidade_comprada * valor_produto
# print(valor_total_da_compra)
#
#
# # 2)
# valor_total_da_compra_liquido = (valor_total_da_compra * taxa_importacao) + valor_total_da_compra
# print(valor_total_da_compra_liquido)
#
# # 3)
# compra_com_desconto = valor_total_da_compra_liquido - taxa_desconto
# print(compra_com_desconto)
#
