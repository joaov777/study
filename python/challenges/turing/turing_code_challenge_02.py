## Turing - Code challenge 02

def isValid(s: str) -> bool:

    oo = ['(', '{', '[']
    co = [')', '}', ']']
    mo = ['()', '{}', '[]']

    while True:

        for i in range(0, len(s)):
            if s[0] in co or len(s) % 2 != 0 or len(s) == 0:
                break
            elif s[i] in co:
                x = len(range(0, i))
                while len(s) != 0:
                    if s[x-1]+s[x] in mo:
                        s.pop(x)
                        s.pop(x-1)
                        if not x == 1:
                            x -= 1
                    else:
                        return False

                    if len(s) == 0:
                        return True

        return False

if __name__ == '__main__':



    line = input()
    line = list(line)
    # line = ['[','{','}',']','(',')']
    if isValid(line):
        print("valid")
    else:
            print("invalid")
