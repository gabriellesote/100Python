"""
    Crie um programa que peça ao usuário para digitar o valor total de
    uma venda, o percentual de desconto aplicado e o percentual de
    imposto cobrado. Ao fim, o programa deve mostrar o preço final da
    mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

    Maroquio, Ricardo. Python Essencial (Série Programação Essencial)
    (Portuguese Edition) (p. 45). Edição do Kindle.
"""
valor_total = float(input("Valor total da venda: "))
desconto_percentual = float(input("Percentual de desconto: "))
imposto_percentual = float(input("Percentual de imposto: "))

desconto = desconto_percentual / 100
imposto = imposto_percentual / 100

valor_descontado = valor_total - (valor_total * desconto)
valor_com_imposto = valor_descontado + (valor_descontado * imposto)
diferenca = valor_com_imposto - valor_descontado

print(f"- Valor inicial: R${valor_total:,.2f}\n"
      f"- Valor com {desconto_percentual:.0f}% de desconto: "
      f"R${valor_descontado:,.2f}\n"
      f"- Imposto: {imposto_percentual:.0f}%\n"
      f"Preço Final: R${valor_com_imposto:,.2f}\n"
      f"Imposto no total de R${diferenca:,.2f}")
