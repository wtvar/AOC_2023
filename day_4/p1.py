#part 1

score = 0

with open("day_4.txt") as text:
    for line in text:
        data = line.strip().split('\n')
        print(data)
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

        score_to_add = 1 * 2 ** (winners - 1)
        score += math.floor(score_to_add)
        print(f'score to add: {math.floor(score_to_add)}')
        print(f'score: {score}')
        print("*" * 80)
