import random

koutia=['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
def grapse():
    print('\n'*50)
    print('     1          2        3')
    print('             |          |')
    print('      '+  koutia[1]+'     |    '+koutia[2]+'    |     '+koutia[3])
    print('   _____|_____|_____')
    print('             |          |')
    print('4    '+  koutia[4]+'     |    '+koutia[5]+'    |     '+koutia[6])
    print('   _____|_____|_____')
    print('             |          |')
    print('7    '+  koutia[7]+'     |    '+koutia[8]+'    |     '+koutia[9])
    print('             |          |')
    print('\n')
grapse()
#status: katastasi tou paixnidiou 0= paizei,1=kapoios nikise, 2= isopalia
status=0
win=""
def check():    
    global status #katastasi tou paixnidiou
    global win#deixnei to gramma tou nikiti 
    #orizontia
    if(koutia[1] == koutia[2] and koutia[2] == koutia[3] and koutia[1] != '  '):    
        status = 1
        win=koutia[1]
    elif(koutia[4] == koutia[5] and koutia[5] == koutia[6] and koutia[4] != '  '):    
        status = 1 
        win=koutia[4]
    elif(koutia[7] == koutia[8] and koutia[8] == koutia[9] and koutia[7] != '  '):    
        status = 1
        win=koutia[7]
    #katheta    
    elif(koutia[1] == koutia[4] and koutia[4] == koutia[7] and koutia[1] != '  '):    
        status = 1 
        win=koutia[1]	
    elif(koutia[2] == koutia[5] and koutia[5] == koutia[8] and koutia[2] != '  '):    
        status = 1    
        win=koutia[2]
    elif(koutia[3] == koutia[6] and koutia[6] == koutia[9] and koutia[3] != '  '):    
        status = 1  
        win=koutia[3]
    #diagwnia   
    elif(koutia[1] == koutia[5] and koutia[5] == koutia[9] and koutia[5] != '  '):    
        status = 1 
        win=koutia[1]
    elif(koutia[3] == koutia[5] and koutia[5] == koutia[7] and koutia[5] != '  '):
        status = 1 
        win=koutia[3]
    #isopalia    
    elif(koutia[1]!='  ' and koutia[2]!='  ' and koutia[3]!='  ' and koutia[4]!='  ' and koutia[5]!='  ' and koutia[6]!='  ' and koutia[7]!='  ' and koutia[8]!='  ' and koutia[9]!='  '):    
        status = 2 
    else:            
        status = 0


giros = raw_input('Press 1 to go first, 2 to go second')
while giros !="1" and giros !="2":
    giros = raw_input('Press 1 to go first, 2 to go second')
player_symbol= raw_input('You want to use x or o?')
while player_symbol !="x" and giros !="o":
    player_symbol= raw_input('You want to use x or o?')


if  player_symbol == "x":
	ai_symbol = "o"
else:
	ai_symbol = "x"
	
	
while status==0:
	if giros == "2":
		i=random.randint(1, 9)
		while koutia[i]!="  ":
			i=random.randint(1, 9)
		koutia[i]=ai_symbol
		giros = "1"
		grapse()
		check()
	elif giros=="1":
		i=input('Select a box')
		while koutia[i]!="  ":
			print('Selected box is not empty')
			i=input('Select a box')
		koutia[i]=player_symbol
		giros = "2"
		grapse()
		check()

if status == 1:
	if win==player_symbol:
		print('you win')
	else:
		print('you lose')
else:
	print('tie')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
