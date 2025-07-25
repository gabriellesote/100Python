"""
Crie um programa que peça ao usuário para digitar o nome, o preço de
custo, o preço de venda e a quantidade em estoque de determinado
produto. Em seguida, o programa deve calcular e mostrar o lucro que
esse produto pode gerar se todo o estoque for vendido.

Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
(Portuguese Edition) (p. 45). Edição do Kindle.

"""
nome = input("Digite o nome do produto: ")
preco_custo = float(input("Preço de custo: "))

preco_venda = float(input("Preço venda: "))
quantidade_estoque = int(input("Quantidade em estoque: "))

lucro_total = (preco_venda * quantidade_estoque) - (preco_custo *
                                                    quantidade_estoque)

print(f"-- {nome} --\n"
      f"Custo: R${preco_custo:,.2f}\n"
      f"Estoque total: {quantidade_estoque}\n"
      f"Preço de venda: R${preco_venda:,.2f}\n"
      f"Lucro total: R${lucro_total:,.2f}")
