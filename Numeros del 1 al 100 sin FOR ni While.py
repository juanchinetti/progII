def pec(i, n):
    if i <= n:
        print(i)
        pec(i + 1, n)

pec(1, 100)    
       