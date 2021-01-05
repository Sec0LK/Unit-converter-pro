'''
*UNIT CONVERTER*

this tool develop by:
    Sec0LK

used moduels for this tool:
    units,
    unit-converter
day01:bulding basic structure with one module (tempurature)
day02:adding different methods
'''
from unit_converter.converter import convert, converts

lib = {"temp":["convert: °C ==> °F","convert: °F ==> °C"],
       "time":["convert: min ==> hour","convert: hour ==> min"]}

def input_data():                                                           #to input values in method
    try:
            data = input("\t[-]Enter value: ")
    except:
        print("[!] error occured! input error")
    return data

def show_all(add):                                                                   #to print unit method
    if add in lib:
        for i in range(0,2):
            print("\t"+lib[add][i])
            
def method(choos):                                                                   #to method
    
    if choos == "0":
        opn = lib['temp'][0]
        print('|[+]added| : '+opn+ " selected")
        value=input_data()
        print("result:")
        print("\t"+converts(value+'°C', '°F'))
        
    elif choos == "1":
        opn = lib['temp'][1]
        print('|[+]added| : '+opn+ " selected")
        value=input_data()
        print("result:")
        print("\t"+converts(value+'°F', '°C'))
      
    

def method2(choos):                                                                   #to method
    
    if choos == "0":
        opn = lib['time'][0]
        print('|[+]added| : '+opn+ " selected")
        value=input_data()
        print("result:")
        print("\t"+converts(value+'min', 'h'))
        
    elif choos == "1":
        opn = lib['time'][1]
        print('|[+]added| : '+opn+ " selected")
        value=input_data()
        print("result:")
        print("\t"+converts(value+'h', 'min'))      
    
#print(converts(data+'°C', '°F'))

while True:
    print("\n\tUnit coverter ver.101 [python3.8]")
    print("\n| 0| Temperature >\n| 1| Time >\n| 2| Distance >\n|97| Help >\n|99| Exit >\n")
    try:
        local =int(input("enter: "))
    
        if local == 0:                             #temperature 
            add = "temp"
            show_all(add)
            choos=input("Enter choose: ")
            try:
                method(choos)
            except:
                print("[!] error occured! input error")
            
            
        elif local == 1:
            add = "time"
            show_all(add)
            choos=input("Enter choose: ")
            print(type(choos))
            try:
                method2(choos)
            except:
                print("[!] error occured! input error")
    
        elif local == 99:                           #exit
            break
       
    except:
        pass 
        #print(lib["temp"].)
        
    
