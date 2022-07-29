import random
import copy

rates = [
    ['プレイヤー', 2.00, 'プレイヤーの勝ちです!'],
    ['バンカー', 1.95, 'バンカーの勝ちです!'],
    ['タイ', 9.00, '引き分けです!']
]

def setup(player_card, banker_card):
    player_card.clear()
    banker_card.clear()
    for _ in range(2):
        card_append(player_card)
        card_append(banker_card)

def betting(pocket):
    bet = ''
    bet_error = True
    while bet_error:
        message = ''
        bet = input(f'賭け金を入力してください(1-{pocket}): ')
        if bet.isnumeric():
            bet = int(bet)
            # 掛け金が0円以下の場合の処理
            if bet <= 0:
                message = '賭け金は1円以上にしてね!'
            # 掛け金が所持金以上の場合の処理
            elif bet > pocket:
                message = '借金してまで賭けられないよ！'
            else:
                bet_error = False
        # 掛け金が数字以外の場合
        else:
            message = '数字を入れてね!'
        print(message)
    return bet

def choose():
    template = '{}: {}\n   {}'
    print('下から賭けるものを選んでください:')
    
    for i, (name, rate, _) in enumerate(rates):
        print(template.format(str(i), name, rate))

    print('-' * 20)
    choice = ''
    choice_error = True
    while choice_error:
        message = ''
        choice = input(f'0-{len(rates)-1}: ')
        # choiceが数字の場合
        if choice.isnumeric():
            choice = int(choice)
            if choice in [0, 1, 2]:
                choice_error = False
            else:
                message = '0～2の中から選択してね!'
        # choiceが数字ではない場合
        else:
            message = '数字を入れてね'
        print(message)
    return choice


def card_append(card):
    card.append(random.randint(1, 13))

def sum_card(card):
    cards = copy.deepcopy(card)
    sum_cards = 0
    for card in cards:
        if card > 9:
            card = 0
        sum_cards += card
    return sum_cards % 10

def third_player(player_card, player_score):
    # 条件に合致すれば3枚目を追加する
    if (player_score) < 6:
        card_append(player_card)
    return player_card

def third_banker(player_card, banker_card, player_score, banker_score):
    # 条件に合致すれば3枚目を追加する
    if banker_score < 3:
        card_append(banker_card)
    elif banker_score == 3:
        if (player_score == 6) or (player_score == 7):
            card_append(banker_card)
        elif len(player_card) > 2:
            if player_card[2] != 8:
                card_append(banker_card)
    elif banker_score == 4:
        if (player_score == 6) or (player_score == 7):
            card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] != 0) or (player_card[2] != 1) or (player_card[2] != 8) or (player_card[2] != 9):
                card_append(banker_card)
    elif banker_score == 5:
        if (player_score == 6) or (player_score == 7):
            card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] == 4) or (player_card[2] == 5) or (player_card[2] == 6) or (player_card[2] == 7):
                card_append(banker_card)
    elif banker_score == 6:
        if (player_score == 6) or (player_score == 7):
            card_append(banker_card)
        elif len(player_card) > 2:
            if (player_card[2] == 6) or (player_card[2] == 7):
                card_append(banker_card)
    return banker_card

def run():
    pocket = 100
    print('バカラやろうよ！')
    # 有り金が尽きるまで繰り返す
    while pocket > 0:
        player_card = []
        banker_card = []
        # プレイヤー、バンカー、タイのいずれかを選ぶ
        choice = 0
        choice = choose()
        # 掛け金を入力する
        bet = betting(pocket)
        # プレイヤーのカードを2枚、バンカーのカードを2枚セットする
        setup(player_card, banker_card)
        # プレイヤーとバンカーのカードを表示する
        print('プレイヤー:' + str(player_card))
        print('バンカー:' + str(banker_card))
        # プレイヤー2枚の合計とバンカー2枚の合計を計算する
        player_score = sum_card(player_card)
        banker_score = sum_card(banker_card)
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
        player_score = sum_card(player_card)
        banker_score = sum_card(banker_card)
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
                pocket -= int(bet)
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