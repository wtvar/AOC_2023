#part 2
import re

list = []
final_answer_list = []
with open("day_6b.txt") as text:
    for line in text:
        data = line.strip().split('\n')
        #print(data)
        a = [int(x) for x in re.findall(r"\d+", data[0])]
        #print(a)
        list.append(a)
    print(f'list. {list}')
    
    for k,number in enumerate(list[0]):
        result = 0
        low = 0
        high = number
        target = list[1][0]
        print(f'number: {number}')
        print(type(target))
        print(target)
        
        while low<=high:
            #print(f'target: {target}')
            #print(f'low: {low}')
            #print(f'high: {high}')
            mid = low + (high - low) // 2
            #print(f'mid: {mid}')
            current_value = mid
            check = current_value * (number - current_value)
            #print(f'check: {check} >= {target} = {check>=target}')
            if check <= target:
                # If so, update the lower bound to the middle index
                #print(f'updating lower to {mid + 1}')
                low = mid + 1
            else:
                # Otherwise, update the upper bound to the middle index - 1
                #print(f'updating high to {mid - 1}')
                high = mid - 1
            #print("x" * 88)
        # Return the smallest number greater than or equal to the target
        final_answer_bot =  (low - 1)
        result = 0
        low = 0
        high = number
        target = list[1][0]
        #print(f'number: {number}')
        #print(type(target))
        #print(target)
        
        while low<=high:
            #print(f'target: {target}')
            #print(f'low: {low}')
            #print(f'high: {high}')
            mid = low + (high - low) // 2
            #print(f'mid: {mid}')
            current_value = mid
            check = current_value * (number - current_value)
            #print(f'check: {check} >= {target} = {check>=target}')
            if check >= target:
                # If so, update the lower bound to the middle index
                #print(f'updating lower to {mid + 1}')
                low = mid + 1
            else:
                # Otherwise, update the upper bound to the middle index - 1
                #print(f'updating high to {mid - 1}')
                high = mid - 1
            #print("x" * 88)
        # Return the smallest number greater than or equal to the target
        final_answer_top =  (low - 1)
        """print(f'k: {k},number: {number}')
        answer = []
        number2 = round(number / 2,0)
        print(f'number2 : {number2}')
        c = number2 * (number - number2)
        print(f'c: {c}')
        d = [number2,(number-number2),c,c>list[1][0]]
        print(f'd: {d}')
        answer.append(d)"""
        
        
    
    print(f'bot: {final_answer_bot}')
    print(f'top: {final_answer_top}')
    print(f'answer: {final_answer_top - final_answer_bot}')
