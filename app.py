import random

rates = [
    ['プレイヤー', 2.00, 'プレイヤーの勝ちです!'],
    ['バンカー', 1.95, 'バンカーの勝ちです!'],
    ['タイ', 9.00, '引き分けです!']
]

def setup(player_card, banker_card):
    player_card.clear()
    banker_card.clear()
    for _ in range(2):
        player_card.append(random.randint(1, 13))
        banker_card.append(random.randint(1, 13))

def betting(pocket):
    return int(input(f'賭け金を入力してください(1-{pocket}): '))

def choose():
    template = '{}: {}\n   {}'
    print('下から賭けるものを選んでください:')
    
    for i, (name, rate, _) in enumerate(rates):
        print(template.format(str(i), name, rate))

    print('-' * 20)
    return int(input(f'0-{len(rates)-1}: '))

def player_card_append(player_card):
    player_card.append(random.randint(1, 13))

def banker_card_append(banker_card):
    banker_card.append(random.randint(1, 13))

def third_player_card_append(player_card):
    if (player_card[0] + player_card[1]) < 6:
        player_card_append(player_card)
    return player_card

def third_banker_card_append(player_card, banker_card):
    if (banker_card[0] + banker_card[1]) < 3:
        banker_card_append(banker_card)
    elif banker_card[0] + banker_card[1] == 3:
        if (player_card[0] + player_card[1] == 6) or (player_card[0] + player_card[1] == 7):
            banker_card_append(banker_card)
        if len(player_card) > 2:
            if player_card[2] != 8:
                banker_card_append(banker_card)
    elif banker_card[0] + banker_card[1] == 4:
        if (player_card[0] + player_card[1] == 6) or (player_card[0] + player_card[1] == 7):
            banker_card_append(banker_card)
        if len(player_card) > 2:
            if (player_card[2] != 0) or (player_card[2] != 1) or (player_card[2] != 8) or (player_card[2] != 9):
                banker_card_append(banker_card)
    elif banker_card[0] + banker_card[1] == 5:
        if (player_card[0] + player_card[1] == 6) or (player_card[0] + player_card[1] == 7):
            banker_card_append(banker_card)
        if len(player_card) > 2:
            if (player_card[2] == 4) or (player_card[2] == 5) or (player_card[2] == 6) or (player_card[2] == 7):
                banker_card_append(banker_card)
    elif banker_card[0] + banker_card[1] == 6:
        if (player_card[0] + player_card[1] == 6) or (player_card[0] + player_card[1] == 7):
            banker_card_append(banker_card)
        if len(player_card) > 2:
            if (player_card[2] == 6) or (player_card[2] == 7):
                banker_card_append(banker_card)
    return banker_card

def calc_player_score(player_card, player_score):
    if len(player_card) > 2:
        player_score = (player_card[0] + player_card[1]  + player_card[2]) % 10
    else:
        player_score = (player_card[0] + player_card[1]) % 10
    return player_score

def calc_banker_score(banker_card, banker_score):
    if len(banker_card) > 2:
        banker_score = (banker_card[0] + banker_card[1] + banker_card[2]) % 10
    else:
        banker_score = (banker_card[0] + banker_card[1]) % 10
    return banker_score

def run():
    pocket = 100
    print('バカラやろうよ！')
    player_card = []
    banker_card = []
    bet = ''
    winner = ''
    player_score = 0
    banker_score = 0
    while pocket > 0:
        choice = choose()
        bet = betting(pocket)
        while bet <= 0:
            print('賭け金は1円以上にしてください。')
            bet = betting(pocket)
        while bet > pocket:
            print('借金してまで賭けられないよ！お客さん。')
            bet = betting(pocket)
        setup(player_card, banker_card)
        print('プレイヤー:' + str(player_card))
        print('バンカー:' + str(banker_card))
        
        player_card = third_player_card_append(player_card)
        banker_card = third_banker_card_append(player_card, banker_card)

        if len(player_card) > 2:
            print('プレイヤーに3枚目のカードが追加されました。:' + str(player_card))
        if len(banker_card) > 2:
            print('バンカーに3枚目のカードが追加されました。:' + str(banker_card))

        if player_card[0] > 10:
            player_card[0] = 0
        if player_card[1] > 10:
            player_card[1] = 0
        if len(player_card) > 2:
            if player_card[2] > 10:
                player_card[2] = 0
        if banker_card[0] > 10:
            banker_card[0] = 0
        if banker_card[1] >10:
            banker_card[1] = 0
        if len(banker_card) > 2:
            if banker_card[2] >10:
                banker_card[2] = 0
        
        player_score = calc_player_score(player_card, player_score)
        banker_score = calc_banker_score(banker_card, banker_score)
        
        print('プレイヤー:' + str(player_score))
        print('バンカー:' + str(banker_score))

        if banker_score < player_score:        
            print(rates[0][2])
            if (choice == 0):
                pocket += rates[0][1] * bet
            else:
                pocket -= bet
        elif banker_score > player_score:
            print(rates[1][2])
            if (choice == 1):
                pocket += rates[1][1] * bet
            else:
                pocket -= bet
        elif banker_score == player_score:
            print(rates[2][2])
            if (choice == 2):
                pocket += rates[2][1] * bet
            else:
                pocket -= bet

        print('pocket:' + str(pocket))
        if pocket == 0:
            print('金がないので終了です!')
        print('---------------------------------------------')