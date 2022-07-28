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
    return input(f'賭け金を入力してください(1-{pocket}): ')

def choose():
    template = '{}: {}\n   {}'
    print('下から賭けるものを選んでください:')
    
    for i, (name, rate, _) in enumerate(rates):
        print(template.format(str(i), name, rate))

    print('-' * 20)
    return input(f'0-{len(rates)-1}: ')

def player_card_append(player_card):
    player_card.append(random.randint(1, 13))

def banker_card_append(banker_card):
    banker_card.append(random.randint(1, 13))

def sum_player_card(player_card):
    player = player_card
    if player[0] > 9:
        player[0] = 0
    if player[1] > 9:
        player[1] = 0
    return player[0] + player[1]

def sum_banker_card(banker_card):
    banker = banker_card
    if banker[0] > 9:
        banker[0] = 0
    if banker[1] > 9:
        banker[1] = 0
    return banker[0] + banker[1]

def third_player(player_card, player_score):
    # 条件に合致すれば3枚目を追加する
    if (player_score) < 6:
        player_card_append(player_card)
    return player_card

def third_banker(player_card, banker_card, player_score, banker_score):
    # 条件に合致すれば3枚目を追加する
    if banker_score < 3:
        banker_card_append(banker_card)
    elif banker_score == 3:
        if (player_score == 6) or (player_score == 7):
            banker_card_append(banker_card)
        elif len(player_card) > 2:
            if player_card[2] != 8:
                banker_card_append(banker_card)
    elif banker_score == 4:
        if (player_score == 6) or (player_score == 7):
            banker_card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] != 0) or (player_card[2] != 1) or (player_card[2] != 8) or (player_card[2] != 9):
                banker_card_append(banker_card)
    elif banker_score == 5:
        if (player_score == 6) or (player_score == 7):
            banker_card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] == 4) or (player_card[2] == 5) or (player_card[2] == 6) or (player_card[2] == 7):
                banker_card_append(banker_card)
    elif banker_score == 6:
        if (player_score == 6) or (player_score == 7):
            banker_card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] == 6) or (player_card[2] == 7):
                banker_card_append(banker_card)
    return banker_card

def calc_player_score(player_card):
    player = player_card
    # 数字が10以上であれば0にする
    if player[0] > 9:
        player[0] = 0
    if player[1] > 9:
        player[1] = 0
    # カードの枚数が3枚の場合
    if len(player_card) > 2:
        if player[2] > 10:
            player[2] = 0
        player_score = (player[0] + player[1]  + player[2]) % 10
    # カードの枚数が3枚ではない場合
    else:
        player_score = (player[0] + player[1]) % 10
    
    return player_score

def calc_banker_score(banker_card):
    # 数字が10以上であれば0にする
    banker = banker_card
    if banker[0] > 9:
        banker[0] = 0
    if banker[1] > 9:
        banker[1] = 0
    # カードの枚数が3枚の場合
    if len(banker_card) > 2:
        if banker[2] > 9:
            banker[2] = 0
        banker_score = (banker[0] + banker[1] + banker[2]) % 10
    # カードの枚数が3枚ではない場合
    else:
        banker_score = (banker[0] + banker[1]) % 10
    
    return banker_score

def run():
    pocket = 100
    print('バカラやろうよ！')
    # 有り金が尽きるまで繰り返す
    while pocket > 0:
        player_card = []
        banker_card = []
        # プレイヤー、バンカー、タイのいずれかを選ぶ
        choice = choose()
        while not str.isnumeric(choice):
            print('数字を入れてね')
            choice = choose()
        while not(int(choice) == 0) or (int(choice) == 1) or (int(choice) == 2):
            print('0～2の中から選択してね!')
            choice = choose()
        # 数値型に変換
        choice = int(choice)
        # 掛け金を入力する
        bet = betting(pocket)

        if str.isdigit(bet):
            # 掛け金が0円以下の場合の処理
            if int(bet) <= 0:
                print('賭け金は1円以上にしてね!')
                bet = betting(pocket)
            # 掛け金が所持金以上の場合の処理
            elif int(bet) > pocket:
                print('借金してまで賭けられないよ！')
                bet = betting(pocket)
        # 掛け金が数字以外の場合
        else:
            print('数字を入れてね!')
            bet = betting(pocket)
        # 入力した掛け金を数値型に変換
        bet = int(bet)
        # プレイヤーのカードを2枚、バンカーのカードを2枚セットする
        setup(player_card, banker_card)
        # プレイヤーとバンカーのカードを表示する
        print('プレイヤー:' + str(player_card))
        print('バンカー:' + str(banker_card))
        # プレイヤー2枚の合計とバンカー2枚の合計を計算する
        player_score = sum_player_card(player_card)
        banker_score = sum_banker_card(banker_card)
        # 3枚目の追加が必要であれば追加する
        player_card = third_player(player_card, player_score)
        banker_card = third_banker(player_card, banker_card, player_score, banker_score)
        # 3枚目が追加された場合、プレイヤーとバンカーのカードを表示する
        if len(player_card) > 2:
            print('プレイヤーに3枚目のカードが追加されました。')
            print('プレイヤー:' + str(player_card))
        if len(banker_card) > 2:
            print('バンカーに3枚目のカードが追加されました。')
            print('バンカー:' + str(banker_card)) 
        # プレイヤーの合計とバンカーの合計を計算する
        player_score = calc_player_score(player_card)
        banker_score = calc_banker_score(banker_card)
        # プレイヤーとバンカーの合計値を出力する
        print('プレイヤーの合計:' + str(player_score))
        print('バンカーの合計:' + str(banker_score))
        # プレイヤーとバンカーのどちらが勝ちか判定し、所持金の計算をする
        if player_score > banker_score:        
            print(rates[0][2])
            if (choice == 0):
                pocket += rates[0][1] * bet
            else:
                pocket -= bet
        elif player_score < banker_score:
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