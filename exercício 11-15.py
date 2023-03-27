import math
#PACOTE MATH
#A função 'ceil()'  arredonda pro mais próximo



#EX 11
num1=int(input('Digite um inteiro'))
num2=int(input('Digite outro inteiro'))
num3=int(input('Digite um real'))
print(f'O dobro do primeiro mais a metade do segundo é: {(num1 * 2)+ (num2/2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(num1*3)+(int(num3))}')
print(f'O terceiro elevado ao cubo é: {num3**3}')

#EX12

al= float(input('Digite a sua altura: '))
print(f'O seu peso ideal seria: {(72.7*al)-58}')

#EX 13
alt= float(input('Digite a sua altura: '))
print(f'O seu peso ideal seria: Para homens:{(72.7 * alt)-58}\n Para mulheres:{(72.7 * alt)-44.7}')



#EX 14 
pes= float(input('Digite o peso do peixe: '))
pes_padrao= 50
excedente=  pes - pes_padrao
print(f'O excedente é: {excedente} e a multa a ser paga é: {excedente * 4}')

#EX 15

hr= int(input('Quanto você ganha por hora?'))
men= int(input('Quantas horas por mês?'))
resul= hr * men
print(f'{resul}. Esse é o seu salário mensal BRUTO')
ir=resul-(resul *0.11)
inss=resul-(0.08*resul)
sind= resul- (resul*0.05)
tot= resul-(((resul - ir)-inss)- sind)
print(f'Esse é o seu salário, depois de descontar o Imposto de Renda{ir}')
print(f'Esse é o seu salário, depois de descontar o INSS{inss}')
print(f'Esse é o seu salário, depois de descontar o Sindicato{sind}')
print(f'Esse é o seu salário LÍQUIDO {tot}')