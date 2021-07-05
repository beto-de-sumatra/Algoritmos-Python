#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

Preço = float (input('Qual o valor do litro de combustível?'))
Quantia = float (input('Quanto deseja abastecer?'))
Litros = int (Quantia / Preço)
print('Vai ter', Litros,'litros')



#2. Faça um programa que calcule a média de consumo de combustível de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km_inicial = float (input('Qual é o Km inicial?'))
km_final = float (input('Qual é o Km final'))
litros = float (input('Quantos litros foram gastos?'))
subtração = km_final - km_inicial
media = subtração + litros / 2
print('Sua média de consumo de combustível é de', média, 'litros')



#3. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

valor_original = float (input('Qual é o valor original da sua dívida?'))
dias_em_atraso = float (input('Qual é a quantidade de dias em atraso?'))
juros = float(input('Qual o valor dos dias em atraso?'))
operação = dias_em_atraso * juros
valor_final = valor_original + operação
print('Sua dívida total é de', valor_final)



#4. Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.

largura1 = float (input('Qual é a largura do cômodo 1? '))
comprimento1 = float (input('Qual é o comprimento do cômodo 1? '))
area1 = largura1 * comprimento1
largura2 = float (input('Qual é a largura do cômodo 2? '))
comprimento2 = float (input('Qual é o comprimento do cômodo 2? '))
area2 = largura2 * comprimento2
largura3 = float (input('Qual é a largura do cômodo 3? '))
comprimento3 = float (input('Qual é o comprimento do cômodo 3? '))
area3 = largura3 * comprimento3
largura4 = float (input('Qual é a largura do cômodo 4? '))
comprimento4 = float (input('Qual é o comprimento do cômodo 4? '))
area4 = largura4 * comprimento4
area_total = area1 + area2 + area3 + area4
print('A área total da casa é', area_total, 'm²')



#5. Faça um programa que calcule a conversão monetária de Real para Dólar. O usuário informa o valor da cotação do dólar (ex.: 3,78) e quanto em real deseja converter (ex. 150,00). O programa exibe quantos dólares valem os reais informados.

dolar = float (input('Qual é o valor da cotacão do Dólar?' ))
conversão = float (input('Quanto em reais deseja converter?' ))
resultado = int (conversão / dolar)
print('Sua conversão monetária em Dólar é de', resultado)



#6. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario = float (input('Qual é o seu salário atual?'))
reajuste = float (input('Qual é o percentual de reajuste?'))
operação = reajuste / 100
operação2 = salario * operação
valor_final = salario + operação2
print('Seu novo salário é', valor_final, 'reais')



#7. Faça um programa que calcula o tempo (em anos) que uma pessoa irá demorar para poupar R$ 1.000.000,00 (Um Milhão de Reais). O usuário informa o salário mensal e o total de despesas mensais

salario = float (input('Qual a quantia do seu salário mensal? '))
despesas = float (input('Qual é o total de suas despesas mensais? '))
operação = salario - despesas
tempo = operação * 12
anos = int (100000000 / tempo)
print('Irá demorar', int (tempo), 'anos para você obter o valor de R$1.000.000,00')



#8. Faça um programa que leia um valor inteiro e mostre na tela uma sequência incluindo os dois números que vem antes, o número digitado, e os dois números que vem depois dele. Ex.: digitou 5; o programa mostra 3 4 5 6 7.

numero = int (input('Digite um número...'))
anterior1 = numero - 1
anterior2 = numero - 2
posterior1 = numero + 1
posterior2 = numero + 2
print(anterior2, anterior1, numero, posterior1, posterior2)



#9. Crie um programa que pergunta o nome do usuário e o ano de nascimento do usuário e calcula qual idade ele tem (ou terá, se ainda não fez aniversário neste ano). Ex.: Nome = Carlos, Ano = 1999. O programa mostra a mensagem: “Carlos tem 20 anos”.

nome = input('Qual é o seu nome? ')
ano = int (input('Em que ano você nasceu? '))
idade = 2020 - ano
print(nome, 'tem', idade, 'anos')



#10. Faça um programa que receba as dimensões de uma sala de aula (comprimento e largura) e as dimensões de uma carteira. Considerando que:
•	Entre duas fileiras deve haver 0,5 m de espaço;
•	Entre duas cadeiras na mesma fileira deve haver 0,2 m de espaço;
•	Deve ser reservada ao professor um espaço de 1,5 m de comprimento;
Calcule quantas carteiras cabem na sala de aula.

comprimento_sala = float (input('Qual é o comprimento da sala? '))
largura_sala = float (input('Qual é a largura da sala? '))
comprimento_cadeira = float (input('Qual é o comprimento da cadeira? '))
largura_cadeira = float (input('Qual é a largura da cadeira? '))
quant_largura = int (largura_sala / (largura_cadeira + 0.5))
quant_comprimento = (comprimento_sala - 1.5) / (comprimento_cadeira + 0.2)
total = int (quant_largura * quant_comprimento)
print('Na sala cabem', total, 'cadeiras')
