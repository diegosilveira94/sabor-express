# permitir que o usuário escolha o tempo de foco e o tempo de pausa
# função que pergunte ao usuário quanto tempo deseja configurar para o período de foco e 
# verificar se o tempo inserido está dentro de um intervalo aceitável (por exemplo, entre 25 e 45 minutos).

def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")

configurar_tempo_foco()