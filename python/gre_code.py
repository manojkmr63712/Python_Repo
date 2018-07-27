import sys

def genCode(n):
    if n == 0:
        return ['']
    code1 = genCode(n-1)
    code2 = []
    for codeWord in code1:
        code2 = [codeWord] + code2

    for i in range(len(code1)):
        code1[i] += '0'
    for i in range(len(code2)):
        code2[i] += '1'
    return code1 + code2 

def main():
    n = int(sys.argv[1])
    code = genCode(n)
    for codeWord in code:
        print(codeWord)

if __name__ == '__main__':
    main()
