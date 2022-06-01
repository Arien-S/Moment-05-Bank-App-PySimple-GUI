from numpy import size  #importerar size från numpy för att ändra fönster storlek
import PySimpleGUI as sg  #importerar Pysimplegui som sg

sg.theme("DarkBlack")  #sätter GUI temat
   
def Menu(): #Gör en funktion för menyn som tar en till valt konto(också funktioner)
    layout = [ 
                [sg.Text("             Välkommen till ARSA BANK!")],  #sätter text och 3 buttons och ger de varaibelnamn(key)
                [sg.Text("                        Välj ett konto:")],
                [sg.Button('Konto 1',key=("Konto_1"),size=(310))],
                [sg.Button('Konto 2',key=("Konto_2"),size=(310))],
                [sg.Button('Konto 3',key=("Konto_3"),size=(310))]
                
                
                

                
                
                
                ]


    
    window = sg.Window('Bank Applikation', layout, size=(310, 340))       #Skapar och döper min window,ändrar stolek på den och lägger in min layout(gör om detta många gånger)                   

    while True:                             #Gör en loop som gör konstant och kollar om knappar är tryckta.
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:          #Om krysset på windown klickas stängs programmet
            break
        if event == "Konto_1":              #Tar en till passande function beroende på knapptryck
            Transactions_Konto_1()            
        if event == "Konto_2":
            Transactions_Konto_2()
        if event == "Konto_3":
            Transactions_Konto_3()
             

        window.close()                      #Stänger fönster
                                      

def Transactions_Konto_1():                     #Gör en Funktion för konto 1 (kommer kommentera endast 
                                                #på en av de 3 functionerna eftersom alla är i princip likadana)

    with open("Konto3.txt", "r+") as file:      #Öppnar alla konton för läsning för att sedan skapa BalanceAmount Variablen och göra den till en integear
        BalanceAmount3 = file.read()            #så att den går att addera
        print(BalanceAmount3)
        BalanceAmount3 = int(BalanceAmount3)
        file.close()
    with open("Konto2.txt", "r+") as file:
        BalanceAmount2 = file.read()
        print(BalanceAmount2)
        BalanceAmount2 = int(BalanceAmount2)
        file.close()
    with open("Konto1.txt", "r+") as file:
        BalanceAmount1 = file.read()
        print(BalanceAmount2)
        BalanceAmount1 = int(BalanceAmount1)
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
                [sg.Button('Byt konto',key=("MenuReturn"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 1', layout, size=(310, 340))      

    while True:                                 #Gör en loop som körs hela tiden som kollar knapptryck bereonde på vilkor
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        
        if event == "BalanceButton":        #tar en till ens saldo funktion för konto 1 när man klickar menyknappen
            Balance_Konto_1()  

        if event == "MenuReturn":          #tar en till meny funktionen när man klickar menyknappen
            Menu()
            
        if event == "InConfirm2":                               #När man klickar ta ut till konto 1 så öppnas konto 1 för skrivning där valuen inskriven
            with open("Konto2.txt", 'w') as Konto_2_saldo:      #adderas på konto 1s saldo
                value = int(values["InAmount"]) + BalanceAmount2
                value = str(value)
                Konto_2_saldo.write(value)
                Konto_2_saldo.close()
            with open("Konto1.txt", 'w') as Konto_1_saldo:        #Sedan så öppnas kontot man är inne på för skrivning och valuen inskriven
                value1 = BalanceAmount1 - int(values["InAmount"]) #subtraheras sedan med kontots saldo
                value1 = str(value1)
                Konto_1_saldo.write(value1)
                Konto_1_saldo.close()

                sg.popup("Överföring genomförd!")               #en popup skärm för att notifiera ens överföring
            Transactions_Konto_1()                              #tar en tilbaka till insättningsskärmen för kontot man är på

        if event == "OutConfirm2":                                  #samma sak görs igen fast nu tvärtom då pengar ska läggas till i kontot man är på
            with open("Konto2.txt", 'w') as Konto_2_saldo:          #och tas bort från kontot som man väljers saldo{
                value = BalanceAmount2 - int(values["OutAmount"])
                value = str(value)
                Konto_2_saldo.write(value)
                Konto_2_saldo.close()
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value1_1 = int(values["OutAmount"]) + BalanceAmount1
                value1_1 = str(value1_1)
                Konto_1_saldo.write(value1_1)
                Konto_1_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_1()                                  #}

        
        if event == "InConfirm3":                                   #samma sak sker här som överföringen mellan konto 1 och konto 2 fast nu byts konto 2 ut mot 3{
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value = int(values["InAmount"]) + BalanceAmount3
                value = str(value)
                Konto_3_saldo.write(value)
                Konto_3_saldo.close()
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value1 = BalanceAmount1 - int(values["InAmount"])
                value1 = str(value1)
                Konto_1_saldo.write(value1)
                Konto_1_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_1()

        if event == "OutConfirm3":
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value = BalanceAmount3 - int(values["OutAmount"])
                value = str(value)
                Konto_3_saldo.write(value)
                Konto_3_saldo.close()
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value1_1 = int(values["OutAmount"]) + BalanceAmount1
                value1_1 = str(value1_1)
                Konto_1_saldo.write(value1_1)
                Konto_1_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_1()

        window.close()                                                #}
        
def Transactions_Konto_2():


    with open("Konto3.txt", "r+") as file:
        BalanceAmount3 = file.read()
        print(BalanceAmount3)
        BalanceAmount3 = int(BalanceAmount3)
        file.close()
    with open("Konto2.txt", "r+") as file:
        BalanceAmount2 = file.read()
        print(BalanceAmount2)
        BalanceAmount2 = int(BalanceAmount2)
        file.close()
    with open("Konto1.txt", "r+") as file:
        BalanceAmount1 = file.read()
        print(BalanceAmount2)
        BalanceAmount1 = int(BalanceAmount1)
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
                [sg.Button('Byt konto',key=("MenuReturn"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 2', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        
        if event == "BalanceButton":
            Balance_Konto_2()  

        if event == "MenuReturn":
            Menu()
            
        if event == "InConfirm1":
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value = int(values["InAmount"]) + BalanceAmount1
                value = str(value)
                Konto_1_saldo.write(value)
                Konto_1_saldo.close()
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value2 = BalanceAmount2 - int(values["InAmount"])
                value2 = str(value2)
                Konto_2_saldo.write(value2)
                Konto_2_saldo.close()

                sg.popup("Överföring genomförd!")
            Transactions_Konto_2()

        if event == "OutConfirm1":
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value = BalanceAmount1 - int(values["OutAmount"])
                value = str(value)
                Konto_1_saldo.write(value)
                Konto_1_saldo.close()
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value1_2 = int(values["OutAmount"]) + BalanceAmount2
                value1_2 = str(value1_2)
                Konto_2_saldo.write(value1_2)
                Konto_2_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_2()

        
        if event == "InConfirm3":
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value = int(values["InAmount"]) + BalanceAmount3
                value = str(value)
                Konto_3_saldo.write(value)
                Konto_3_saldo.close()
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value2 = BalanceAmount2 - int(values["InAmount"])
                value2 = str(value2)
                Konto_2_saldo.write(value2)
                Konto_2_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_2()

        if event == "OutConfirm3":
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value = BalanceAmount3 - int(values["OutAmount"])
                value = str(value)
                Konto_3_saldo.write(value)
                Konto_3_saldo.close()
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value1_2 = int(values["OutAmount"]) + BalanceAmount2
                value1_2 = str(value1_2)
                Konto_2_saldo.write(value1_2)
                Konto_2_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_2()

        window.close()

def Transactions_Konto_3():


    with open("Konto3.txt", "r+") as file:
        BalanceAmount3 = file.read()
        print(BalanceAmount3)
        BalanceAmount3 = int(BalanceAmount3)
        file.close()
    with open("Konto2.txt", "r+") as file:
        BalanceAmount2 = file.read()
        print(BalanceAmount2)
        BalanceAmount2 = int(BalanceAmount2)
        file.close()
    with open("Konto1.txt", "r+") as file:
        BalanceAmount1 = file.read()
        print(BalanceAmount2)
        BalanceAmount1 = int(BalanceAmount1)
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
                [sg.Button('Byt konto',key=("MenuReturn"))]

                
                
                
                ]

    
    window = sg.Window('Bank Applikation - Konto 1', layout, size=(310, 340))      

    while True:
        event, values = window.read()
 
        if event == sg.WIN_CLOSED:
            break
        
        if event == "BalanceButton":
            Balance_Konto_3()  

        if event == "MenuReturn":
            Menu()
            
        if event == "InConfirm1":
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value = int(values["InAmount"]) + BalanceAmount1
                value = str(value)
                Konto_1_saldo.write(value)
                Konto_1_saldo.close()
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value3 = BalanceAmount3 - int(values["InAmount"])
                value3 = str(value3)
                Konto_3_saldo.write(value3)
                Konto_3_saldo.close()

                sg.popup("Överföring genomförd!")
            Transactions_Konto_3()

        if event == "OutConfirm1":
            with open("Konto1.txt", 'w') as Konto_1_saldo:
                value = BalanceAmount1 - int(values["OutAmount"])
                value = str(value)
                Konto_1_saldo.write(value)
                Konto_1_saldo.close()
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value1_3 = int(values["OutAmount"]) + BalanceAmount3
                value1_3 = str(value1_3)
                Konto_3_saldo.write(value1_3)
                Konto_3_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_3()

        
        if event == "InConfirm2":
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value = int(values["InAmount"]) + BalanceAmount2
                value = str(value)
                Konto_2_saldo.write(value)
                Konto_2_saldo.close()
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value3 = BalanceAmount3 - int(values["InAmount"])
                value3 = str(value3)
                Konto_3_saldo.write(value3)
                Konto_3_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_3()

        if event == "OutConfirm2":
            with open("Konto2.txt", 'w') as Konto_2_saldo:
                value = BalanceAmount2 - int(values["OutAmount"])
                value = str(value)
                Konto_2_saldo.write(value)
                Konto_2_saldo.close()
            with open("Konto3.txt", 'w') as Konto_3_saldo:
                value1 = int(values["OutAmount"]) + BalanceAmount3
                value1 = str(value1)
                Konto_3_saldo.write(value1)
                Konto_3_saldo.close()
                sg.popup("Överföring genomförd!")
            Transactions_Konto_3()

        window.close()
        





def Balance_Konto_1():                          #Gör en en function med window för att kunna visa varje kontos saldo från en sin txt


    with open("Konto1.txt", "r+") as file:          #läser in filen,skapar en variabel till värdet i den
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


    with open("Konto2.txt", "r+") as file:
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


    with open("Konto3.txt", "r+") as file:
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
         




Menu()   #gör meny funktionen när programmet startas