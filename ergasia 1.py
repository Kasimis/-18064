def  summintervals(a):


 #ftiaxnw lista me ta akra twn sinwlwn kai tin taksinomw se afksousa seira
    pl1=0
    akra = []
   
    for i in range(len(a)):
                pl1=pl1+2
                akra.append(a[i][0])
                akra.append(a[i][-1])
    
    akra.sort()
            

#ftiaxnw lista me ta eswterika twn sinwlwn
    pl2=0
    eswterika=[]
    k=-1
    
    for i in range(len(a)):
        k = k + 1
        for j in range(a[k][0]+1,a[k][-1]):
           if j not in c:
              eswterika.append(j)
              pl2=pl2+1

#diagrafw apo tin lista twn akrwn ekeina ta akra pou iparxoun kai sti lista twn
#eswterikwn wste na min epanalambanontai diastimata
    for i in range(pl2-1):
      for j in range(pl1-1):
           if akra[i]==c[j]:
               del akra[i]
#kai telika gia na brw ta miki twn diastimatwn briskw ti diafora twn akrwn tous
#ana dio kai athrizw oles tis diafores diladi ola ta miki               
    s=0
    for i in range(0,len(akra)-1,2):
        
        s= akra[i+1]-akra[i]+s

    print(s)


