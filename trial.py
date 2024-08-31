dict1 = {
    'name' : {'ph': 'email'},
    'name2' : {'ph2': 'email2'}
}

#def add_contacts(nm, ph)
#    for i, j in dict1.items():
#        for x,y in j.items():
#            print(f"{x}: {y}")
    
    
    
def update_info(name, ph):
    for i, j in dict1.items():
        if(i == name):
            for x, y in j.items():
                dict1.pop(x)
                dict1.update(ph)
                break
    

def delete_contacts(name):
    for i, j in dict1.items():
        if(i == name):
            dict1.pop(i)
            break

def list_all():
    for i, j in dict1.items():
        print(f"{i} : ")
        for x,y in j.items():
            print(f"{x}: {y}")


def search_contacts(name):
    for i, j in dict1.items():
        if(i == name):
            for x,y in j.items():
                print(f"{i}: {j}")
    

#def list_by_ini(ini):
#    for i, j in dict1.items():
        
    

#-----------------------------------------------------------------




while(True):
    print("################################")
    print('0. EXIT')
    print('1. add_contacts --> name, ph')
    print('2. update_info --> ph')
    print('3. delete_contacts -->')
    print('4. list all')
    print('5. search_contacts --> name')
    print('6. list_by_ini --> char')
    print("################################")
    
    ch = str(input("\nEnter your choice: "))

    if(ch == '0'):
        break
    
    elif(ch == '1'):
        name = str(input("name: "))
        ph = int(input("ph: "))
        #email = str(input("email: "))
            
        add_contacts(name, ph)
            
    elif(ch == '2'):
        name = str(input("name: "))
        ph = int(input("ph: "))
        #email = str(input("email: "))
            
        update_info(name, ph)
            
    elif(ch == '3'):
        name = str(input("name: "))
            
        delete_contacts(name)
        
    elif(ch == '4'):
        list_all()
            
    elif(ch == '5'):
        name = str(input("name: "))
            
        search_contacts(name)
        
    elif(ch == '6'):
        ini = str(input("initial letter: "))
            
        list_by_ini(ini)


