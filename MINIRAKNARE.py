while==True:
    print("1: räkna med addition / +")
    print("2: räkna med subtraktion / -")
    print("3: räkna med multiplikation / *")
    print("4: räkna med division / /")
    print("5: avsluta")
    choice=int(input("Skriv ett tal emellan 1-5: "))
    if choice==1:
        print("Du valde addition")
        Tal1=float(input("Skriv ut ett tal: "))
        Tal2=float(input("Skriv ut ett nytt tal: "))
        print(f"Summan är {Tal1+Tal2}")
    elif choice==2:
        print("Du valde subtraktion")
        Tal1=float(input("Skriv ut ett tal: "))
        Tal2=float(input("Skriv ut ett nytt tal: "))
        print(f"differensen är {Tal1-Tal2}")
    elif choice==3:
        print("Du valde multplikation")
        Tal1=float(input("Skriv ut ett tal: "))
        Tal2=float(input("Skriv ut ett nytt tal: "))
        print(f"produkten är {Tal1*Tal2}")
    elif choice==4:
        print("Du valde division")
        Tal1=float(input("Skriv ut ett tal: "))
        Tal2=float(input("Skriv ut ett nytt tal: "))
        print(f"kvoten är {Tal1/Tal2}")
    elif choice==5:
        while print("Avslutar"):
            break
        