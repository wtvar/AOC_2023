#part 1
import re



list = []
final_answer_list = []
with open("day_6.txt") as text:
    for line in text:
        data = line.strip().split('\n')
        print(data)
        a = [int(x) for x in re.findall(r"\d+", data[0])]
        print(a)
        list.append(a)
    print(f'1. {list}')
    
    for k,number in enumerate(list[0]):
        result = 0
        
        print(k,number)
        answer = []
        for v in range(1,number):
            c = v *(number-v)
            d = [v,(number-v),c,c>list[1][k]]
            print(d)
            answer.append(d)
        #print(answer)
        for z,y in enumerate(answer):
            #print(z,y[3])
            if y[3] == True:
                result += 1
            else:
                pass
        print(f'result: {result}')
        final_answer_list.append(result)
    
    product = 1 
    print(final_answer_list)
    for num in final_answer_list:
        product *= num
    print(product)
