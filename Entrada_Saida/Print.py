#Função print() -> imprime algo na tela 
print('Hello world')
#Obs: se utiliza a virgula para separa os argumenstos passados
print

#sep -> define como as coisas vão ser separadas dentro do print (por padrão separa com o espaço ' ')
print(1, 2, 3, sep='-')   
#end -> define o que acontece após o print (por podrão quebra a linha '\n')
print(1, 2, 3, end=' OK\n')

#Escape -> o compilador vai ignora o proximo caractere após a \
print("Hello \"World\"")
#r -> é usado para mostrar os escapes, utilizando o r no iniico do argumento 
print(r"Mostrando os \"escape\"")
#Obs: caso queira usar aspas simples ou dupla basta usar a outra opçaõ para abrir/fechar e dentro utiliza a que desejar 
print("Usando aspas 'Simples' ")
print('Usando aspas "Duplas" ')

#Concatenação -> junção de dois argumentos
print('Hello'+'world')
#Obs: str só pode ser concatenado com outra str
#print('1'+ 1) Não da certo, tem que coverter uma dos tipos
#Obs: int pode ser concatenado com float
#     quando se concatena tipos numericos se realiza uma soma e o resultado é do tipo float
print(type(1+1.0))

#Repetição -> utilizando o operador * é possivel repetir uma str
varios_oi = 'oi ' * 5
print(varios_oi)
#Obs: quando se faz isso com float ou int é realizado apenas uma multiplicação simples 