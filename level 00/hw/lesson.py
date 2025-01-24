# hw1

def homework1(a, b, c):
    if a % c == 0:
        start = a
    else:
        start = a + (c - a % c)
    
    if b % c == 0:
        end = b
    else:
        end = b - (b % c)
    
    if start > end:
        return 0
    
    return (end - start) // c + 1

print(homework1(12, 19, 3))  
print(homework1(5, 15, 5)) 

# hw2
def homework2(num,b):
    num = str(num)
    lists1 = []
    lists2 = []
    if "." in str(num):
        num = num.split(".")
        num1 = num[0][::-1]
        num2 = num[1]
        for i in range(len(num1)):
            lists1.append(int(num1[i]) * (b ** i))
        
        for x in range(len(num2)):
            lists2.append(int(num2[x]) * (1 / b ** (x+1)))
        return sum(lists1 + lists2)
        

    else:
        num = num[::-1]
        for i in range(len(num)):
            lists1.append(int(num[i]) * (b ** i))
    
    return sum(lists1)


print(homework2(1011,16))
print(homework2(520.3,6))


