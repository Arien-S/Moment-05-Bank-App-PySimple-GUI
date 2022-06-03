from numpy import size  #importerar size från numpy för att ändra fönster storlek
import PySimpleGUI as sg  #importerar Pysimplegui som sg

sg.theme("DarkBlack")  #sätter GUI temat

def UserChoice():

    layout = [ 
                [sg.Text("            Välkommen till [ ARSA ]  bank!")],  #sätter text och 3 buttons och ger de varaibelnamn(key)
                [sg.Text("")],
                [sg.Text("Logga in")],
                [sg.Button('Logga in',key=("Login"),size=(310))],
                [sg.Text("Skapa konto")],
                [sg.Button('Skapa konto',key=("Make"),size=(310))],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Button('Lämna',key=("Exit"),size=(310))]
                
                ]

    window = sg.Window('Bank Applikation', layout, size=(310, 340))
    
             
                
    while True:                             #Gör en loop som gör konstant och kollar om knappar är tryckta.
        event, values = window.read()
 
        if event == sg.WIN_CLOSED or event == "Exit":          
            break
        if event == "Login":    #tar en till login funktionen
            Login() 
        if event == "Make":        #tar en till register funktionen
            Register()
        window.close()




def Login():

    layout = [ 
                [sg.Text("            Välkommen till [ ARSA ]  bank!")],  #sätter text och 3 buttons och ger de varsitt varaibelnamn(key)
                [sg.Text("                     Skriv in ditt Namn:")],
                [sg.Input("",key=("Name"))],
                [sg.Text("                     Skriv in ditt lösenord:")],
                [sg.Input("",key=("Pass"))],
                [sg.Button('Logga in',key=("Login"),size=(310))],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Button('Lämna',key=("Exit"),size=(310))]
                
                ]

    window = sg.Window('Bank Applikation', layout, size=(310, 340))  
    
    
    with open("Password.txt", "r") as file:  #Öppnar Password filen gör den till en varaibel som senare andvänds för att kolla om inputen stämmer
        Password = file.read()            
        Password = str(Password)
        file.close()

    with open("Name.txt", "r") as file:      #Öppnar Namn filen gör den till en varaibel som senare andvänds för att kolla om inputen stämmer
        UserName = file.read()            
        UserName = str(UserName)
        file.close()
        
             
                
    while True:                             #Gör en loop som gör konstant och kollar om knappar är tryckta.
        event, values = window.read()
 
        if event == sg.WIN_CLOSED or event == "Exit":          
            break
        if event == "Login" and values["Pass"] == Password and values["Name"] == UserName:   #om både namn och lösenord är korrekt så sker inloggning
            Menu() 
        if event == "Login" and values["Pass"] != Password or values["Name"] != UserName:       #om ett av de är fel så får man en popup och får försöka igen
            sg.popup("Fel lösenord eller namn")
            sg.popup("Försök igen")  
            Login()
       
        window.close()                     
            


def Register():

    layout = [ 
                [sg.Text("            Välkommen till [ ARSA ]  bank!")],  #sätter text och 3 buttons och ger de varaibelnamn(key)
                [sg.Text("                     Skriv in ditt namn:")],
                [sg.Input("",key=("Name"))],
                [sg.Text("                     Skriv in ett lösenord:")],
                [sg.Input("",key=("Pass"))],
                [sg.Button('Skapa konto',key=("Register"),size=(310))],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Button('Tilbaka',key=("Back"),size=(310))],
                [sg.Button('Lämna',key=("Exit"),size=(310))]
                
                ]

    window = sg.Window('Bank Applikation', layout, size=(310, 340))       #Skapar och döper min window,ändrar stolek på den och lägger in min layout(gör om detta många gånger)                   

    while True:                             #Gör en loop som gör konstant och kollar om knappar är tryckta.
        event, values = window.read()
 
        if event == sg.WIN_CLOSED or event == "Exit":          #Om krysset på windown klickas stängs programmet
            break
        
        if event == "Register":                               #öppnar password filen och skriver in det man skrivit i input
            with open("Password.txt", 'w+') as file:           #stänger sedan filen
                value = (values["Pass"])
                value = str(value)
                file.write(value)
                file.close()
            with open("Name.txt", 'w+') as file:      #Gör samma sak med namnet angivet
                value2 = (values["Name"])
                value1 = str(value2)
                file.write(value1)
                file.close()
            
                Login()
        if event == "Back":
            UserChoice()

        window.close()    



   
def Menu(): #Gör en funktion för menyn som tar en till valt konto(också funktioner)
    layout = [ 
                [sg.Text("            Välkommen till [ ARSA ]  bank!")],  #sätter text och 3 buttons och ger de varaibelnamn(key)
                [sg.Text("                        Välj ett konto:")],
                [sg.Button('Konto 1',key=("Konto_1"),size=(310))],
                [sg.Button('Konto 2',key=("Konto_2"),size=(310))],
                [sg.Button('Konto 3',key=("Konto_3"),size=(310))],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Text("")],
                [sg.Button('Logga ut',key=("Exit"),size=(310))]
                
                ]


    
    window = sg.Window('Bank Applikation', layout, size=(310, 340))       #Skapar och döper min window,ändrar stolek på den och lägger in min layout(gör om detta många gånger)                   

    while True:                             #Gör en loop som gör konstant och kollar om knappar är tryckta.
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:          #Om krysset på windown klickas stängs programmet
            break
        
        if event == "Exit":
            UserChoice()
            
        if event == "Konto_1":              #Tar en till passande function beroende på knapptryck
            Transactions_Konto_1()            
        if event == "Konto_2":
            Transactions_Konto_2()
        if event == "Konto_3":
            Transactions_Konto_3()
             

        window.close()                      #Stänger fönster
                                      

def Transactions_Konto_1():                     #Gör en Funktion för konto 1 (kommer kommentera endast 
                                                #på en av de 3 functionerna eftersom alla är i princip likadana)

    with open("Konto3.txt", "r") as file:      #Öppnar alla konton för läsning för att sedan skapa BalanceAmount Variablen och göra den till en integear
        BalanceAmount03 = file.read()            #så att den går att addera
        BalanceAmount3 = int(BalanceAmount03)
        file.close()
    with open("Konto2.txt", "r") as file:
        BalanceAmount02 = file.read()
        BalanceAmount2 = int(BalanceAmount02)
        file.close()
    with open("Konto1.txt", "r") as file:
        BalanceAmount01 = file.read()
        BalanceAmount1 = int(BalanceAmount01)
        file.close()


    layout = [ 
                [sg.Text("Ta ut")],                                     #sätter knappar(events) och inputs(values) och ger de keys som fungerar som variabler
                [sg.Input("",key=("InAmount"))],
                [sg.Button('Ta ut till Konto 2',key=("InConfirm2"))],
                [sg.Button('Ta ut till Konto 3',key=("InConfirm3"))],
                [sg.Text('Sätt in')],
                [sg.Input('',key=("OutAmount"))],
                [sg.Button('Sätt in från Konto 2',key=("OutConfirm2"))],
                [sg.Button('Sätt in från Konto 3',key=("OutConfirm3"))],
                [sg.Text("")], 
                [sg.Button('Kolla Saldo',key=("BalanceButton"))],
                [sg.Button('Byt konto',key=("MenuReturn")),sg.Button('Stäng ned flik',key=("Exit"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 1', layout, size=(310, 340))   

         

    while True:     
        
        
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":           #Stänger programmet om man klickar på exit eller windows krysset
            break
 
        if event == "BalanceButton":      #skickar en till en window med ens Konto.txt fil som text för att visa saldot
            Balance_Konto_1()
    
        if event == "MenuReturn":          #tar en till meny funktionen när man klickar menyknappen
            Menu()

                                                                                #OBS! På varje if sats sär jag öppnar filer eller tar emot inputs gör jag en try except  på Value Error så att man inte kan skriva in bokstäver  

        if event == "InConfirm2":                                                 #När man klickar ta ut till konto 2  
                                                                                  
            try:                                                                  
                value = int(values["InAmount"]) + BalanceAmount2                               
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_1()
            else:                                                               
                with open("Konto2.txt", 'w') as Konto_2_saldo:                  #så öppnas konto 2 för skrivning     
                    value = str(value)
                    Konto_2_saldo.write(value)                                   #där valuen inskriven adderas på konto 2s saldo
                    Konto_2_saldo.close()               
            try:                                                                    
                value1 = BalanceAmount1 - int(values["InAmount"])               #subtraheras sedan med det kontot man är pås saldo        
            except ValueError:
                break                                                           #kör endast break på denna eftersom den sker när man stänger ned programmet
            else: 
                with open("Konto1.txt", 'w') as Konto_1_saldo:                   #Sedan så öppnas kontot man är inne på för skrivning och valuen inskriven
                    value1 = str(value1)
                    Konto_1_saldo.write(value1)
                    Konto_1_saldo.close()
                    sg.popup("Överföring genomförd!")               #en popup skärm för att notifiera ens överföring
                    Transactions_Konto_1()                              #tar en tilbaka till insättningsskärmen för kontot man är på

                                                                    #samma sak görs igen fast nu tvärtom då pengar ska läggas till i kontot man är på
        if event == "OutConfirm2":                                  #och tas bort från kontot som man väljers saldo{
            try:          
                value = BalanceAmount2 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_1()
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value = str(value)
                    Konto_2_saldo.write(value)
                    Konto_2_saldo.close()
            try:
                value1_1 = int(values["OutAmount"]) + BalanceAmount1
            except ValueError:
                break
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value1_1 = str(value1_1)
                    Konto_1_saldo.write(value1_1)
                    Konto_1_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_1()                                  #}

        
        if event == "InConfirm3":                                               #samma sak sker här som överföringen mellan konto 1 och konto 2 fast nu byts konto 2 ut mot 3{
            try:
                value = int(values["InAmount"]) + BalanceAmount3
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_1()
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value = str(value)
                    Konto_3_saldo.write(value)
                    Konto_3_saldo.close()
            try:
                value1 = BalanceAmount1 - int(values["InAmount"])
            except ValueError:
                break
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value1 = str(value1)
                    Konto_1_saldo.write(value1)
                    Konto_1_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_1()

        if event == "OutConfirm3":
            try:
                value = BalanceAmount3 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_1()
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value = str(value)
                    Konto_3_saldo.write(value)
                    Konto_3_saldo.close()
            try:
                value1_1 = int(values["OutAmount"]) + BalanceAmount1
            except ValueError:
                break
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value1_1 = str(value1_1)
                    Konto_1_saldo.write(value1_1)
                    Konto_1_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_1()

        window.close()                                                #}
        
def Transactions_Konto_2():


    with open("Konto3.txt", "r") as file:
        BalanceAmount03 = file.read()
        BalanceAmount3 = int(BalanceAmount03)
        file.close()
    with open("Konto2.txt", "r") as file:
        BalanceAmount02 = file.read()            
        BalanceAmount2 = int(BalanceAmount02)    
        file.close()
    with open("Konto1.txt", "r") as file:
        BalanceAmount01 = file.read()
        BalanceAmount1 = int(BalanceAmount01)
        file.close()


    layout = [ 
                [sg.Text("Ta ut")],     
                [sg.Input("",key=("InAmount"))],
                [sg.Button('Ta ut till Konto 1',key=("InConfirm1"))],
                [sg.Button('Ta ut till Konto 3',key=("InConfirm3"))],
                [sg.Text('Sätt in')],
                [sg.Input('',key=("OutAmount"))],
                [sg.Button('Sätt in från Konto 1',key=("OutConfirm1"))],
                [sg.Button('Sätt in från Konto 3',key=("OutConfirm3"))],
                [sg.Text("")], 
                [sg.Button('Kolla Saldo',key=("BalanceButton"))],
                [sg.Button('Byt konto',key=("MenuReturn")),sg.Button('Stäng ned flik',key=("Exit"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 2', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        
        if event == "BalanceButton":
            Balance_Konto_2()  

        if event == "MenuReturn":
            Menu()
            
        if event == "InConfirm1":
            try:
                value = int(values["InAmount"]) + BalanceAmount1
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_2()
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value = str(value)
                    Konto_1_saldo.write(value)
                    Konto_1_saldo.close()
            try:
                value2 = BalanceAmount2 - int(values["InAmount"])
            except ValueError:
                break
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value2 = str(value2)
                    Konto_2_saldo.write(value2)
                    Konto_2_saldo.close()

                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_2()

        if event == "OutConfirm1":
            try:
                value = BalanceAmount1 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_2()
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value = str(value)
                    Konto_1_saldo.write(value)
                    Konto_1_saldo.close()
            try:
                value1_2 = int(values["OutAmount"]) + BalanceAmount2
            except ValueError:
                break
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value1_2 = str(value1_2)
                    Konto_2_saldo.write(value1_2)
                    Konto_2_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_2()

        
        if event == "InConfirm3":
            try:
                value = int(values["InAmount"]) + BalanceAmount3
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_2()
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value = str(value)
                    Konto_3_saldo.write(value)
                    Konto_3_saldo.close()
            try:
                value2 = BalanceAmount2 - int(values["InAmount"])
            except ValueError:
                break
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value2 = str(value2)
                    Konto_2_saldo.write(value2)
                    Konto_2_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_2()

        if event == "OutConfirm3":
            try:
                value = BalanceAmount3 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_2()    
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value = str(value)
                    Konto_3_saldo.write(value)
                    Konto_3_saldo.close()
            try:
                value1_2 = int(values["OutAmount"]) + BalanceAmount2
            except ValueError:
                break
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value1_2 = str(value1_2)
                    Konto_2_saldo.write(value1_2)
                    Konto_2_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_2()

        window.close()

def Transactions_Konto_3():


    with open("Konto3.txt", "r") as file:
        BalanceAmount03 = file.read()
        BalanceAmount3 = int(BalanceAmount03)
        file.close()
    with open("Konto2.txt", "r") as file:
        BalanceAmount02 = file.read()
        BalanceAmount2 = int(BalanceAmount02)
        file.close()
    with open("Konto1.txt", "r") as file:
        BalanceAmount01 = file.read()
        BalanceAmount1 = int(BalanceAmount01)
        file.close()


    layout = [ 
                [sg.Text("Ta ut")],     
                [sg.Input("",key=("InAmount"))],
                [sg.Button('Ta ut till Konto 1',key=("InConfirm1"))],
                [sg.Button('Ta ut till Konto 2',key=("InConfirm2"))],
                [sg.Text('Sätt in')],
                [sg.Input('',key=("OutAmount"))],
                [sg.Button('Sätt in från Konto 1',key=("OutConfirm1"))],
                [sg.Button('Sätt in från Konto 2',key=("OutConfirm2"))],
                [sg.Text("")], 
                [sg.Button('Kolla Saldo',key=("BalanceButton"))],
                [sg.Button('Byt konto',key=("MenuReturn")),sg.Button('Stäng ned flik',key=("Exit"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 1', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        
        if event == "BalanceButton":
            Balance_Konto_3()  

        if event == "MenuReturn":
            Menu()
            
        if event == "InConfirm1":
            try:
                value = int(values["InAmount"]) + BalanceAmount1
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_3()   
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value = str(value)
                    Konto_1_saldo.write(value)
                    Konto_1_saldo.close()
            try:
                value3 = BalanceAmount3 - int(values["InAmount"])
            except ValueError:
                break
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value3 = str(value3)
                    Konto_3_saldo.write(value3)
                    Konto_3_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_3()

        if event == "OutConfirm1":
            try:
                value = BalanceAmount1 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_3()  
            else:
                with open("Konto1.txt", 'w') as Konto_1_saldo:
                    value = str(value)
                    Konto_1_saldo.write(value)
                    Konto_1_saldo.close()
            try:
                value1_3 = int(values["OutAmount"]) + BalanceAmount3
            except ValueError:
                break
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value1_3 = str(value1_3)
                    Konto_3_saldo.write(value1_3)
                    Konto_3_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_3()

        
        if event == "InConfirm2":
            try:
                value = int(values["InAmount"]) + BalanceAmount2
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_3() 
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value = str(value)
                    Konto_2_saldo.write(value)
                    Konto_2_saldo.close()
            try:
                value3 = BalanceAmount3 - int(values["InAmount"])
            except ValueError:
                break
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value3 = str(value3)
                    Konto_3_saldo.write(value3)
                    Konto_3_saldo.close()
                    sg.popup("Överföring genomförd!")
                Transactions_Konto_3()

        if event == "OutConfirm2":
            try:
                value = BalanceAmount2 - int(values["OutAmount"])
            except ValueError:
                sg.popup("Endast nummer tillåtna") 
                Transactions_Konto_3()
            else:
                with open("Konto2.txt", 'w') as Konto_2_saldo:
                    value = str(value)
                    Konto_2_saldo.write(value)
                    Konto_2_saldo.close()
            try:
                value1 = int(values["OutAmount"]) + BalanceAmount3
            except ValueError:
                break
            else:
                with open("Konto3.txt", 'w') as Konto_3_saldo:
                    value1 = str(value1)
                    Konto_3_saldo.write(value1)
                    Konto_3_saldo.close()
                    sg.popup("Överföring genomförd!")
                    Transactions_Konto_3()

        window.close()
        





def Balance_Konto_1():                          #Gör en en function med window för att kunna visa varje kontos saldo från en sin txt


    with open("Konto1.txt", "r") as file:          #läser in filen,skapar en variabel till värdet i den
        BalanceAmount = file.read()

    layout = [ 
                [sg.Text("Saldo:                                                                                             ")],     
                [sg.Text(BalanceAmount)],   #visar filens text(saldot)
                [sg.Button('Tillbaka',key=("BackToMain"))]                #Gör en knapp för att gå tilbaka till transaktion fönstret

                ]
    
    window = sg.Window('Bank Applikation', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        if event == "BackToMain":       #tar tilbaka en till föregående fönster(Transaktion för valt konto)
            Transactions_Konto_1() 
        window.close()

def Balance_Konto_2():                                      #Gör samma sak för alla 3 konto saldon{


    with open("Konto2.txt", "r") as file:
        BalanceAmount = file.read()

    layout = [ 
                [sg.Text("Saldo:                                                                                             ")],     
                [sg.Text(BalanceAmount)],
                [sg.Button('Tillbaka',key=("BackToMain"))]

                ]
    
    window = sg.Window('Bank Applikation', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        if event == "BackToMain":
            Transactions_Konto_2() 
        window.close()                                      

def Balance_Konto_3():


    with open("Konto3.txt", "r") as file:
        BalanceAmount = file.read()

    layout = [ 
                [sg.Text("Saldo:                                                                                             ")],     
                [sg.Text(BalanceAmount)],
                [sg.Button('Tillbaka',key=("BackToMain"))]

                ]
    
    window = sg.Window('Bank Applikation', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        if event == "BackToMain":
            Transactions_Konto_3() 
        window.close()                                                                                              #}
         



UserChoice()  #startar programmets första fönster