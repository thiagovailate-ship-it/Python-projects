#ATIVIDADE 1: Cofrinho do Pedrinho (Lá ele)
moeda1 = int(input('Quantidade de moedas de 1 centavo: '))
moeda5 = int(input('Quantidade de moedas de 5 centavos: '))
moeda10 = int(input('Quantidade de moedas de 10 centavos: '))
moeda25 = int(input('Quantidade de moedas de 25 centavos: '))
moeda50 = int(input('Quantidade de moedas de 50 centavos: '))
moeda1r = int(input('Quantidade de moedas de 1 real: '))

valor_total = (
    (moeda1 * 0.01) +
    (moeda5 * 0.05) +
    (moeda10 * 0.10) +
    (moeda25 * 0.25) +
    (moeda50 * 0.50) +
    (moeda1r * 1)
)

print('\n--- Cofrinho do Pedrinho ---')
print(f'Moedas de 1 centavo: {moeda1}')
print(f'Moedas de 5 centavos: {moeda5}')
print(f'Moedas de 10 centavos: {moeda10}')
print(f'Moedas de 25 centavos: {moeda25}')
print(f'Moedas de 50 centavos: {moeda50}')
print(f'Moedas de 1 real: {moeda1r}')

print(f'\nPedrinho possui R$ {valor_total:.2f} no total.')

#ATIVIDADE 2: Calcula quantidade de suco e água para uma determinada quantia de litros
litros = float(input('Digite quantos litros: '))
partes = litros / 10
agua = partes * 8
suco = partes * 2

print(f'São necessários {agua} litros de água')
print(f'São necessários {suco} litros de suco de maracujá')

#ATIVIDADE 3: Desconto de produto com o valor final
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.10
novo_preco = preco - desconto
print(f'Voce recebeu um desconto de R$ {desconto:.2f}! o novo valor é de R$ {novo_preco:.2f}!')


#ATIVIDADE 4: Salário Fixo + Comissão
salario = float(input('Digite o valor do salário recebido: '))
vendas = float(input('Digite o valor de vendas: '))
comissao = vendas * 0.04
print(f'O valor total recebido foi de R${salario:.2f} + R${comissao:.2f}, totalizando R${salario + comissao:.2f}')


#ATIVIDADE 5: Peso se emagrecer ou engordar
peso = float(input('Digite o seu peso em Kg: '))
engordou = peso * 0.15
emagreceu = peso * 0.20
novo_peso1 = peso + engordou
novo_peso2 = peso - emagreceu

print(f'O seu peso é {peso} Kg. Se voce engordar, fica com {novo_peso1} Kg (Não exagere muito nas pizzas).')
print(f'Se voce emagrecer 20%, o seu novo peso vai ser de {novo_peso2} Kg (Não fique muito tempo sem comer também, hehe).')


#ATIVIDADE 6: 
salario_minimo = float(input('Digite o valor atual do salário minimo: '))
salario_funcionario = float(input('Digite o seu salário: '))
quantidade_salario = salario_funcionario / salario_minimo

print(f'O funcionário recebe {quantidade_salario:.2f} salários minimos')

#ATIVIDADE 7: tabuada
numero = int(input('Digite um número para a tabuada: '))

print(f'{numero} x 1 = {numero * 1}')
print(f'{numero} x 2 = {numero * 2}')
print(f'{numero} x 3 = {numero * 3}')
print(f'{numero} x 4 = {numero * 4}')
print(f'{numero} x 5 = {numero * 5}')
print(f'{numero} x 6 = {numero * 6}')
print(f'{numero} x 7 = {numero * 7}')
print(f'{numero} x 8 = {numero * 8}')
print(f'{numero} x 9 = {numero * 9}')
print(f'{numero} x 10 = {numero * 10}')


#ATIVIDADE 8: Meses, semanas e dias vivendo neste planeta
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nascimento

dias = idade * 365
semanas = dias // 7
meses = idade * 12

print(f'Voce tem {idade} anos!')
print(f'Totalizando {meses} meses, {semanas} semanas e {dias} dias vivo!')


#ATIVIDADE 9: Desconto das contas do João
joao_salario = 1200.00
c1 = 200.00
c2 = 120.00
multa = (c1 + c2) * 0.02
resto_salario = joao_salario - c1 - c2 - multa

print(f'Restou R$ {resto_salario:.2f} do João')
