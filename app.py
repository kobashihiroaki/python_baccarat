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
    player = copy.deepcopy(player_card)
    if player[0] > 9:
        player[0] = 0
    if player[1] > 9:
        player[1] = 0
    return player[0] + player[1]

def sum_banker_card(banker_card):
    banker = copy.deepcopy(banker_card)
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
        choice_error = ''
        choice = choose()
        if choice.isnumeric():
            if (int(choice) == 0) or (int(choice) == 1) or (int(choice) == 2):
                choice_error = ''
            else:
                print('0～2の中から選択してね!')
                choice_error = 'true'
        else:
            print('数字を入れてね')
            choice_error = 'true'
        # choice_errorがtrueならば以下の処理を実行
        while choice_error == 'true':
            choice = choose()
            if choice.isnumeric():
                if (int(choice) == 0) or (int(choice) == 1) or (int(choice) == 2):
                    choice_error = ''
                else:
                    print('0～2の中から選択してね!')
                    choice_error = 'true'
            else:
                print('数字を入れてね')
                choice_error = 'true'
        # choice_errorが空ならば以下の処理を実行
        if choice_error == '':
            # 掛け金を入力する
            bet_error = ''
            bet = betting(pocket)
            
            if bet.isnumeric():
                # 掛け金が0円以下の場合の処理
                if int(bet) <= 0:
                    print('賭け金は1円以上にしてね!')
                    bet_error = 'true'
                # 掛け金が所持金以上の場合の処理
                elif int(bet) > pocket:
                    print('借金してまで賭けられないよ！')
                    bet_error = 'true'
                else:
                    bet_error = ''
            # 掛け金が数字以外の場合
            else:
                print('数字を入れてね!')
                bet_error = 'true'
            # bet_errorがtrueの場合
            while (bet_error == 'true'):
                bet = betting(pocket)
                if bet.isnumeric():
                    # 掛け金が0円以下の場合の処理
                    if int(bet) <= 0:
                        print('賭け金は1円以上にしてね!')
                        bet_error = 'true'
                    # 掛け金が所持金以上の場合の処理
                    elif int(bet) > pocket:
                        print('借金してまで賭けられないよ！')
                        bet_error = 'true'
                    else:
                        bet_error = ''
                # 掛け金が数字以外の場合
                else:
                    print('数字を入れてね!')
                    bet_error = 'true'
            # bet_errorが空の場合
            if (bet_error == ''):
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
                        pocket += rates[0][1] * int(bet)
                    else:
                        pocket -= int(bet)
                elif player_score < banker_score:
                    print(rates[1][2])
                    if (choice == 1):
                        pocket += rates[1][1] * int(bet)
                    else:
                        pocket -= int(bet)
                elif banker_score == player_score:
                    print(rates[2][2])
                    if (choice == 2):
                        pocket += rates[2][1] * int(bet)
                    else:
                        pocket -= bet

                print('pocket:' + str(pocket))
                if pocket == 0:
                    print('金がないので終了です!')
                print('---------------------------------------------')