def meny():
    print("""
    1. Lägg till önskelista
    2. Läs upp önskelista
    """)
    a = int(input("Välj ett alternativ:  "))
    return a

def skapa_öl():
    childname = input("Vad heter barnet?:  ")
    filename = input("Vad vill du att önske listan ska heta?:  ")
    with open (filename, "w", encoding="utf8") as öl:
        öl.write(childname+str("s önskelista\n"))
        n = 1
        b = 2
        while b > 1:
            a = str(input("vad vill du lägga till på önskelistan (skriv # om du är klar):  "))
            if a == "#":
                b = -1
                main()
            else:
                öl.write(f"{n}. {a}\n")
                n += 1

def läsup_öl():
    filename = input("Vad heter önskelistan?:  ")
    with open(filename+str(".txt"), "r", encoding="utf8") as öl:
        lines = öl.readlines()
        for line in lines:
            print(line, end="")

def main():
    k = meny()
    if k == 1:        
        skapa_öl()
    if k == 2:
        läsup_öl()


if __name__ == "__main__":
    main()