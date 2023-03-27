import math
#EX 16
ar= int(input('Qual o tamanho da área a ser pintada?(em metros quadrados)'))

pa= ar //3
print(f'Você precisará de {pa} litros de tinta')
cont= pa /18
done= math.ceil(cont)
print(f'Para ser pintado tudo, você precisará, no mínimo, de {done} caixas de tinta, que sairão no valor de R${done * 80},00')


#EX 17 (incompleto)
td= int(input('Qual o tamanho da área a ser pintada?(em metros quadrados)'))

pbu= td //6
print(f'Você precisará de {pbu} litros de tinta')
conta= pbu //18
resto= (pbu / 18)-(conta)
con_cai= math.ceil(pbu/18)
af= resto /3.6
af= math.ceil(af)
print(f'Para ser pintado tudo, você precisará, no mínimo, de {con_cai} caixas de tinta de 18L, que sairão no valor de R${conta * 80},00 e {af} caixas de tinta de 3,6L que sairá por: {af* 25}')




#EX 18
rrr= int(input('Digite o tamanho do arquivo (Em MB)'))
ddd= int(input('Digite a velocidade da internet (Em MB/s)'))
temp= rrr/ddd
print('O tempo é:', temp)