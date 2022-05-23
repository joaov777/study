## Turing - Code Challenge 1

def calPoints(ops) -> int:

    i = 0
    while i < len(ops):
        
        if ops[i] == "C":
             ops.pop(i)
             ops.pop(i-1)
             i-=2
        elif ops[i] == "D":
             ops.insert(i,int(ops[i-1])*2)
             ops.pop(i+1)

        elif ops[i] == "+":
             ops.insert(i,int(ops[i-1])+int(ops[i-2]))
             ops.pop(i+1)
        i+=1

    result = list(map(int,ops))
    return sum(result)

if __name__ == '__main__':
    #line = input()
    #ops = line.strip().split()

    ops = ['5','2','C','D','+']
    ops2 = ['5','-2','4','C','D','9','+','+']

    print(calPoints(ops2))
