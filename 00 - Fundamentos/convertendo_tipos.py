#Conversão de valor decimal (float) para inteiro (int)
print(int(1.97348728))

#Conversão de String para inteiro (int)
print(int("10"))

#Conversão de String para decimal (float)
print(float("10.10"))

#Conversão de inteiro (int) para decimal (float)
print(float(100))

#No exemplo abaixo é retornado um float, uma vez que foi usado apenas uma barra para a divisão
print(100 / 2)

#No exemplo abaixo é retornado um int, uma vez que foi usado duas barras para a divisão
print(100 // 2)

# Teste de erro (No exemplo abaixo é retornado erro uma vez que está tentando converter a string 'teste' para inteiro
idade, nome = ('teste', 'João')
idade = int(idade))

# Teste de printar o tipo de variável (No caso abaixo é retornado int, uma vez que o valor indicado para a variável é um inteiro)
idade = 10
print(type(idade))
