def  summintervals(a):


 #ftiaxnw lista me ta akra twn sinwlwn kai tin taksinomw se afksousa seira
    akra = []
   
    for i in range(len(a)):
                
                akra.append(a[i][0])
                akra.append(a[i][-1])
    
    akra.sort()      

#ftiaxnw lista me ta eswterika twn sinwlwn
    
    eswterika=[]
    k=-1
    
    for i in range(len(a)):
        k = k + 1
        for j in range(a[k][0]+1,a[k][-1]):
              eswterika.append(j)
              
    
#diagrafw apo tin lista twn akrwn ekeina ta akra pou iparxoun kai sti lista twn
#eswterikwn wste na min epanalambanontai diastimata
    a=set(akra)
    e=set(eswterika)

    a.difference_update(e)
    akr=list(a)        
#kai telika gia na brw ta miki twn diastimatwn briskw ti diafora twn akrwn tous
#ana dio kai athrizw oles tis diafores diladi ola ta miki               
    print (eswterika)
    print (akra)
    s=0
    for i in range(0,len(akr)-1,2):
        
        s= akr[i+1]-akr[i]+s

    print(s)
summintervals([[1,5],[10,20],[1,6],[16,19],[5,11]])





