print("Välkommen till miniräknaren")#Välkomnar användaren
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
            print("----------------------")
            av=int(input("Vill du avsluta (ja:1/nej:2): ")) #Frågar om användaren vill avsluta tjänsten
            if av==1: #aktiverar alternativ ja
                print("avslutar") #visar att den avslutar
                break #Avbryter exekveringen
            elif av==2: #aktiverar alternativ nej
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
            print("----------------------")
            av=int(input("Vill du avsluta (ja:1/nej:2): ")) #Frågar om användaren vill avsluta tjänsten
            if av==1: #aktiverar alternativ ja
                print("avslutar")
                break
            elif av==2: #aktiverar alternativ nej
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
            print("----------------------")
            av=int(input("Vill du avsluta (ja:1/nej:2): "))#Frågar om användaren vill avsluta tjänsten
            if av==1: #aktiverar alternativ ja
                print("avslutar")
                break#Avbryter exekveringen
            elif av==2: #aktiverar alternativ nej
                print("----------------------")  
    elif choice==4: #Kör om man valde 4
        print("Du valde division") #skriver ut vad du valde
        ångra=int(input("ångrar du dig (ja:1/nej:2): "))#låter dig gå tillbaka till menyn om du valde fel
        if ångra==1: #aktiverar alternativ ja
            print("Tillbaka med dig")
            print("----------------------")
        elif ångra==2: #aktiverar alternativ nej
            Tal1=float(input("Skriv ut ett tal: ")) #Låter användaren skriva in ett tal
            Tal2=float(input("Skriv ut ett nytt tal: ")) #Låter användaren skriva in ett nytt tal
            print(f"Kvoten är {Tal1/Tal2}")#Räknar ut kvoten
            print("----------------------")
            av=int(input("Vill du avsluta (ja:1/nej:2): "))#Frågar om användaren vill avsluta tjänsten
            if av==1: #aktiverar alternativ ja
                print("avslutar")
                break#Avbryter exekveringen
            elif av==2: #aktiverar alternativ nej
                print("----------------------")  
    elif choice==5: #Kör om man valde alternativ 5
        print("Avslutar")
        break#Avbryter exekveringen