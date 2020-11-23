print("Välkommen till miniräknaren")#Välkomnar användaren
Tal=1
Tal3=0
while True:#Håller igång loopen
    print("1: räkna med addition / +") #Skriver ut alternativ 1
    print("2: räkna med subtraktion / -") #Skriver ut alternativ 2
    print("3: räkna med multiplikation / *") #Skriver ut alternativ 3
    print("4: räkna med division / /") #Skriver ut alternativ 4
    print("5: avsluta") #Skriver ut alternativ 5
    choice=int(input("Skriv ett tal emellan 1-5: "))#Gör så att man kan välja alternativ
    if choice==1: #Kör om man valde 1
        print("Du valde addition") #skriver ut vad du valde
        ångra=int(input("ångrar du dig (ja:1/nej:2): "))#låter dig gå tillbaka till menyn om du valde fel
        if ångra==1: #aktiverar alternativ ja
            print("Tillbaka med dig") #skriver ut en text
            print("----------------------") #separations grund
        elif ångra==2: #aktiverar alternativ nej
            Tal1=float(input("Skriv ut ett tal: ")) #Låter användaren skriva in ett tal
            Tal2=float(input("Skriv ut ett nytt tal: ")) #Låter användaren skriva in ett annat tal
            print(f"Summan är {Tal1+Tal2}") #Adderar talen
            talResultat=Tal1+Tal2#Skapar en varaiabel av summan
            while Tal!=0: #Låter en ny loop köra så länga man inte skriver 0
                Tal=float(input("Tal ge tal (Om du vill avsluta skriv 0): "))#låter användaren skriva hur många tal hen vill tills hen skriver 0
                talResultat= talResultat + Tal #lägger på talet på tal resulatet
                if Tal==0:#om tal=0 avsluta loopen
                    print(f"{talResultat}") #skriv ut reultatet
                    print("----------------------")
    elif choice==2: #Kör om man valde 2
        print("Du valde subtraktion") #Visar vad du valde
        ångra=int(input("ångrar du dig (ja:1/nej:2): ")) #låter användaren ångra
        if ångra==1: #aktiverar alternativ ja
            print("Tillbaka med dig") 
            print("----------------------")
        elif ångra==2: #aktiverar alternativ nej
            Tal1=float(input("Skriv ut ett tal: ")) #låter användaren välja ett tal
            Tal2=float(input("Skriv ut ett nytt tal: "))#låter användaren välja ett till tal
            print(f"Differensen är {Tal1-Tal2}") #Räknar ut differensen
            talResultat=Tal1-Tal2 #Skapar en varaiabel av differsensen
            while Tal!=0:
                Tal=float(input("Tal ge tal: "))
                talResultat= talResultat - Tal #tar bort talet från tal resulatet
                if Tal==0:
                    print(f"{talResultat}")
                    print("----------------------")
    elif choice==3: #Kör om man valde 3
        print("Du valde multiplikation") #skriver ut vad du valde
        ångra=int(input("ångrar du dig (ja:1/nej:2): "))#låter dig gå tillbaka till menyn om du valde fel
        if ångra==1: #aktiverar alternativ ja
            print("Tillbaka med dig")
            print("----------------------")
        elif ångra==2: #aktiverar alternativ nej
            Tal1=float(input("Skriv ut ett tal: ")) #Låter användaren skriva in ett tal
            Tal2=float(input("Skriv ut ett nytt tal: ")) #Låter användaren skriva in ett nytt tal
            print(f"Produkten är {Tal1*Tal2}")#Räknar ut produkten
            talResultat=Tal1*Tal2 #Gör om produkten till en variabel
            while Tal3!=1:
                Tal3=float(input("Tal ge tal: "))
                talResultat= talResultat * Tal3 #Multplicerar resultatet med det nya talet
                if Tal3==1:
                    print(f"{talResultat}")
                    print("----------------------")
    elif choice==4: #Kör om man valde 4
        print("Du valde division") #skriver ut vad du valde
        ångra=int(input("ångrar du dig (ja:1/nej:2): "))#låter dig gå tillbaka till menyn om du valde fel
        if ångra==1: #aktiverar alternativ ja
            print("Tillbaka med dig")
            print("----------------------")
        elif ångra==2: #aktiverar alternativ nej
            Tal1=int(input("Skriv ut ett tal: ")) #Låter användaren skriva in ett tal
            Tal2=int(input("Skriv ut ett nytt tal: ")) #Låter användaren skriva in ett nytt tal
            print(f"Kvoten är {Tal1/Tal2}")#Räknar ut kvoten
    elif choice==5: #Kör om man valde alternativ 5
        print("Avslutar")
        break#Avbryter exekveringen