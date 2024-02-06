Egipt=[]
def Egipskie(p, q):
    if p==0 or q==0:
        return Egipskie
    else:
        l=1
        if q%p==0:
            n = int(q / p)
        else:
            n=int(q/p)+1
        p*=n
        l*=q
        q,n = q*n, n*q
        p-=l
        Egipt.append([l, n])
        Egipskie(p, q)

Egipskie(8, 15)
for list in Egipt:
    list[1]/=list[0]
    list[1]=int(list[1])
    list[0]=1
for i in Egipt:
    print(i[0],"/",i[1])