#part 2
sum = 0


total_power = 0
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
            maxes = {}
            for throw in spl:
                #print(f'throw: {throw}')
                #print(type(throw))
                a = extract_counts(throw)
                
                for colour in a:
                    #print(f'colour: {colour}')
                    #print(f'value: {a[colour]}')
                    if colour in maxes:
                        if a[colour] > maxes[colour]:
                            maxes[colour] = a[colour]
                        else:
                            pass
                    else:
                        maxes[colour] = a[colour]
                    
            #print(game_id)        
            #print(maxes)
            power = 1
            for value in maxes:
                power *= maxes[value]
            #print(power)
            total_power += power
        print(total_power)    
            
        
