""" 1 - Crie uma lista para cada informação a seguir:

    Lista de números de 1 a 10;
    Lista com quatro nomes;
    Lista com o ano que você nasceu e o ano atual.
"""
nums = []
for num in range(1,11):
    nums.append(num)

nomes = ['Diego', 'Rafael', 'Jonathan', 'Gabriel']

ano_nascimento = [1994, 2025]

""" 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""
for nome in nomes:
    print(f'- ' + nome)


""" 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""

print()
acum_soma_impar = 0
for num in nums:
    if(num % 2 != 0):
        acum_soma_impar += num
print(f'Soma números ímpares: {acum_soma_impar}')
print()

""" 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
"""
for i in range(10,0,-1):
    print(f'- {i}')
print()

""" 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
"""
num_tabuada = int(input('Digite um número: '))
for i in range(1,11):
    print(f'{num_tabuada} x {i} = {num_tabuada * i}')
print()

""" 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""
nums.append('a') # Add para chamar o except abaixo
acum_soma = 0
for num in nums:
    try:
        acum_soma += num
    except Exception as e:
        print(f'Não foi possível realizar a soma: Erro {e}')
print(acum_soma)
print()

""" 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""
nums2 = [12, 47, 8, 23, 35, 2, 50, 16, 29, 41]
acum_num = 0
try:
    for num in nums2:    
        acum_num += num
    media_num = acum_num / len(nums)
    print(f'Média da lista nums2: {media_num:.2f}')
except ZeroDivisionError:
    print('Não é válido a divisão por zero')
except Exception as e:
    print(f'Não foi possível realizar a média: Erro {e}')
print()