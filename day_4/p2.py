#part 2

cards = 0
dict_of_cards = {}


with open("day_4.txt") as text:
    
    file_content = text.readlines()
    #print(f' len: {len(file_content)}')
    for item in range(len(file_content)):
        dict_of_cards[item] = 1
    
    print(f'cards: {dict_of_cards}')    
    for n,line in enumerate(file_content):
        data = line.strip().split('\n')
        #print(data)
        clean_data = data[0].split(': ')[1]
        lists_of_ints = [list(map(int, section.split())) for section in clean_data.split('|')]
        winning_nrs = lists_of_ints[0]
        my_numbers = lists_of_ints[1]
        print(f'winning nrs: {winning_nrs}')
        print(f'mine: {my_numbers}')
        
        winners = 0
        for number in my_numbers:
            if number in winning_nrs:
                winners += 1
            else:
                pass
        print(f'winners: {winners}')
        print(f'n is: {n}')
        for winner in range(winners):
            print(winner + 1)
            search = n + winner + 1
            dict_of_cards[search] += (1 * dict_of_cards[n])
        print(dict_of_cards)
        print("*" * 80)
    total_sum = sum(dict_of_cards.values())
    print(total_sum)
