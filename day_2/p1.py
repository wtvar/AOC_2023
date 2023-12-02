#part 1
sum = 0
max_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('day_2.txt') as text:
    #data = text.read()
    
    for line in text:
        data = line.strip().split('\n')
        #print(data)
        for v in data:
            game_id = extract_game_number(v)
            #print(f"game_id is: {game_id['Game']}")
            spl = v.split(';')
            #print(spl)
            valid = True
            for throw in spl:
                #print(f'throw: {throw}')
                #print(type(throw))
                a = extract_counts(throw)
                
                for colour in a:
                    #print(f'colour: {colour}')
                    #print(f'value: {a[colour]}')
                    if a[colour] > max_dict[colour]:
                        #print(f'max is breached for {colour}')
                        valid = False
                    else:
                        pass
            if valid:
                sum += game_id['Game']
                print(f'new sum: {int(sum)}')
                
            
        
