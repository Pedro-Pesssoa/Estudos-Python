nome = 'Pedro'
idade = 21
altura = 1.70
dinheiro = 30000.50

#Primeira forma -> direto no print 
print('{} tem {} anos e mede {:.2f} ele tem {:,.2f} reais'.format(nome, idade, altura, dinheiro))

#Segunda forma -> com variavel 
texto = '{} tem {} anos e mede {:.2f} ele tem {:,.2f} reais'
formato = texto.format(nome, idade, altura, dinheiro)
print(formato)

#Repetindo valores e trocando ordem
texto2 = 'Com {ida} anos e mede {alt:.2f} ele tem {din:,.2f} reais, lembrando {alt:.2f} de altura'
formato2 = texto2.format(nom=nome, ida=idade, alt=altura, din=dinheiro)
print(formato2)

#Com :.valorf é possivel definir quantas casas descimais vão aparecer 
#Ao acrecentar a , caso o numero for grande ele séra separado por virgulas