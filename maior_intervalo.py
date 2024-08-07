def maior_intervalo(s):
    max_intervalo = 0
    intervalo_atual = -1
    for i, char in enumerate(s):
        if char == 'A':
            intervalo_atual = i
        elif char == 'B' and intervalo_atual != -1:
            max_intervalo = max(max_intervalo, i - intervalo_atual)
    print(f"O maior intervalo entre 'A' e 'B' é {max_intervalo}")

