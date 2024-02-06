from string import ascii_uppercase
def loaddata(data):
    file=open(data, "r")
    ids=list(map(str.strip, file.readlines()))
    return ids
def zad1():
    ids=loaddata("identyfikator.txt")
    numbers=[]
    for id in ids:
        ch=[]
        for i in range(len(id)):
            if i>2:
                ch.append(id[i])
        numbers.append(ch)
    highest =0
    highestn = [0]
    for n, number in enumerate(numbers):
        count=0
        for i in number:
            count+=int(i)
            if count>highest:
                highestn=[]
                highest=count
                highestn.append(ids[n])
            elif highest==count:
                highestn.append(ids[n])
    print(highest, highestn)
def zad2():
    ids=loaddata("identyfikator.txt")
    idm=[]
    for item in ids:
        ch=[]
        c=[]
        for i in range(len(item)):
            if i<=2:
                ch.append(item[i])
            else:
                c.append(item[i])
        idm.append([ch, c])
    print(idm)
    palindroms=[]
    for id in idm:
        for i in id:
            r=i[::-1]
            print(i, r)
            c=0
            for n in range(len(r)):
                if r[n]!=i[n]:
                    c+=1
            if c==0:
                palindroms.append(id)

    print(palindroms)
def zad3():
    weight=[7, 3, 1, 0, 7, 3, 1, 7, 3]
    Alphabet=ascii_uppercase
    values=[]
    wrong=[]
    for i in range(26):
        values.append(i+10)
    ids=loaddata("identyfikator.txt")
    for id in ids:
        sum=0
        for i in range(len(id)):
            if i==3:
                pass
            elif i<=2:
                a=values[ascii_uppercase.index(id[i])]
                sum+=weight[i]*a
            else:
                sum+=weight[i]*int(id[i])
            print(sum)
        if sum%10!=int(id[3]):
            print(sum%10)
            wrong.append(id)
    print(wrong)
zad3()