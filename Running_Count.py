#Dicionario Mapeamento das cartas para o valor Hi-Lo
valores_hi_lo = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

def calcular_contagem(cartas, baralhos_restantes):
    # Transformar cartas para maiúsculas e remover espaços
    cartas_formatadas = [carta.strip().upper() for carta in cartas]
    
    # Calcular contagem corrente
    contagem_corrente = 0
    for carta in cartas_formatadas:
        contagem_corrente += valores_hi_lo.get(carta, 0)

    # Calcular contagem verdadeira (ajustada para número de baralhos)
    contagem_verdadeira = contagem_corrente / baralhos_restantes if baralhos_restantes else 0

    return contagem_corrente, round(contagem_verdadeira, 2)

# Interface simples no terminal
def main():
    cartas_input = input("Digite as cartas separadas por espaço (ex: 10 A 3 Q 7): ")
    cartas = cartas_input.split()
    baralhos_restantes = float(input("Quantos baralhos restam no shoe? "))
    
    rc, tc = calcular_contagem(cartas, baralhos_restantes)
    
    print(f"\nContagem Corrente (Running Count): {rc}")
    print(f"Contagem Verdadeira (True Count): {tc}")

if __name__ == "__main__":
    main()
