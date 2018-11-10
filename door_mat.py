'''N, M = map(int,input().split())
for i in range(1,N,2): 
    print("{}".format(".|." * i).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N-2,-1,-2): 
    print("{}".format(".|." * i).center(M, "-"))'''

    n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))