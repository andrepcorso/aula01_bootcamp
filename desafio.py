# 1) Solicita ao usuário que digite seu nome

nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite sua porcentagem de bônus: "))

# 4) Calcule o valor do bônus final

calculo_bonus = 1000 + salario * bonus

# 5) Imprima cálculo do KPI para o usuário

print("O cálculo do bonus é: 1000 + ", salario, " x ",bonus)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(nome,", seu salário é R$",salario,", sua porcentagem de bônus é ", bonus, "então seu bônus é igual a R$", calculo_bonus)

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# Colocar , ao inves de ponto
