def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя один друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя ', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя ', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей, целых', friends_count)


for friends_count in range(0, 21):
    print_friends_count(friends_count)