'''
Desafio 1- Peça ao usuário a quantidade inicial de produtos em estoque. Use while para permitir registrar vendas e reposições até o usuário digitar “sair”. Ao final, exiba o saldo de produtos.
'''

estoqueBanana = 0
conti = "Continuar"

while conti == "Continuar" or conti == "continuar":
    estoqueAdd = int(input("Insira a quantidade que deseja adicionar: "));
    estoqueBanana+=estoqueAdd
    
    conti = input('Digite "Continuar" ou "Sair" para editar este produto ou não: ');

if estoqueBanana > 0:
    print("Venda do produto Liberada!")


'''
Desafio 2  Cálculo de Média de Temperaturas Semanais Peça as temperaturas de 7 dias usando for.Calcule e exiba:
a média da semana
a maior temperatura
a menor temperatura
'''

temperaturas = []  

for i in range(1, 8):
    temperatura = float(input(f"Digite a temperatura do dia {i}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print(f"\nMédia da semana: {media:.2f}°C")
print(f"Maior temperatura: {maior:.2f}°C")
print(f"Menor temperatura: {menor:.2f}°C")



'''
Desafio 3  Simulador de Caixa Eletrônico
Peça um valor de saque. Use while para calcular quantas cédulas de 100, 50, 20 e 10 reais são necessárias. Exiba o detalhamento do saque.(Exemplo: “2 notas de 100, 1 nota de 50, 1 nota de 20…")
'''


valor = int(input("Digite o valor do saque: R$ "))

cedulas = [100, 50, 20, 10]
contador = 0

while valor > 0 and contador < len(cedulas):
    cedula_atual = cedulas[contador]
    quantidade = valor // cedula_atual
    valor %= cedula_atual 
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {cedula_atual}")
    contador += 1

if valor != 0:
    print("Não é possível sacar valores que não sejam múltiplos de 10.")