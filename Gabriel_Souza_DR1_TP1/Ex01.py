# Escreva um código usando list comprehension em Python que retorne os caracteres individuais de uma string que não são caracteres de espaço em branco. Aplique-a à string "Sítio do pica-pau amarelo \n 2023”.

texto = "Sítio do pica-pau amarelo \n 2023"
resultado = [char for char in texto if char not in [" ", "\n"]]
print(resultado)
