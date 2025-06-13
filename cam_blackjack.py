import cv2
import Cards
from Running_Count import calcular_contagem
import os

# Função para calcular pontuação do Blackjack
def blackjack_score(rank_names):
    score = 0
    aces = 0

    value_map = {
        "Two": 2, "Three": 3, "Four": 4, "Five": 5,
        "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
        "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
    }

    for rank in rank_names:
        val = value_map.get(rank, 0)
        score += val
        if rank == "Ace":
            aces += 1

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def converter_para_valor_hi_lo(rank_names):
    conversao = {
        "Two": "2", "Three": "3", "Four": "4", "Five": "5",
        "Six": "6", "Seven": "7", "Eight": "8", "Nine": "9", "Ten": "10",
        "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"
    }
    return [conversao.get(rank, rank) for rank in rank_names]

# Inicializa a câmera
videostream = cv2.VideoCapture(0)
if not videostream.isOpened():
    print("Erro: Não foi possível abrir a câmera")
    exit()

# Carrega as imagens de treino
path = os.getcwd()
train_ranks = Cards.load_ranks(os.path.join(path, 'Card_Imgs/'))
train_suits = Cards.load_ranks(os.path.join(path, 'Card_Imgs/'))

frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

baralhos_restantes = int(input("Quantidade de baralhos restante: "))  # ajuste conforme o jogo 

while True:
    ret, image = videostream.read()
    if not ret:
        print("Erro ao capturar frame")
        break

    t1 = cv2.getTickCount()
    pre_proc = Cards.preprocess_image(image)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

    ranks_detected = []

    if len(cnts_sort) != 0:
        cards = []
        k = 0
        for i in range(len(cnts_sort)):
            if cnt_is_card[i] == 1:
                cards.append(Cards.preprocess_card(cnts_sort[i], image))
                card = cards[k]
                card.best_rank_match, card.best_suit_match, card.rank_diff, card.suit_diff = \
                    Cards.match_card(card, train_ranks, train_suits)
                ranks_detected.append(card.best_rank_match)
                image = Cards.draw_results(image, card)
                k += 1

        if len(cards) != 0:
            temp_cnts = [card.contour for card in cards]
            cv2.drawContours(image, temp_cnts, -1, (255, 0, 0), 2)

    # Converte para valores Hi-Lo
    valores_cartas = converter_para_valor_hi_lo(ranks_detected)
    rc, tc = calcular_contagem(valores_cartas, baralhos_restantes)

    # Exibe a pontuação do Blackjack
    total_score = blackjack_score(ranks_detected)
    cv2.putText(image, f"Pontuacao: {total_score}", (10, 60), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Exibe a contagem Hi-Lo
    cv2.putText(image, f"Running Count: {rc}", (10, 100), font, 0.9, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(image, f"True Count: {tc}", (10, 130), font, 0.9, (255, 255, 0), 2, cv2.LINE_AA)

    # Exibe FPS
    cv2.putText(image, f"FPS: {int(frame_rate_calc)}", (10, 26), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Blackjack Detector + Hi-Lo", image)

    t2 = cv2.getTickCount()
    frame_rate_calc = 1 / ((t2 - t1) / freq)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videostream.release()
cv2.destroyAllWindows()
