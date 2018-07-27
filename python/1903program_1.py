def dec2bin(n):
    if not n:
        return ''
    else:
        return dec2bin(n/2) + str(n%2)

def manoj():
    print dec2bin(1)
manoj()
#def pad(p, s):
#    print "0"*(p-len(s))+s

#def combos(n):
#    for i in range(2**n):
#        print pad(n, dec2bin(i))

#combos(2)
