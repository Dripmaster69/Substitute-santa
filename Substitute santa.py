childname = input("Vad heter barnet?:  ")
filename = input("Vad vill du att önske listan ska heta?:  ")

def meny():
    for x in range(1):
        print("""
        1. Lägg till önskelista
        2. Läs upp önskelista
        """)
        a = int(input("Välj ett alternativ:  "))
    return a

def skapa_öl():
    with open (f"{filename}.txt", "w", encoding="utf8") as öl:
        öl.write(f"{childname}s önskelista")
        n = 2
        while True:
            a = input("vad vill du lägga till på önske listan (skriv # om du är klar):  ")
            if a == "#":
                True == False
            öl.write(f"{n}. {a}")
            n += 1

def läsup_öl():
    a = input("Vad heter önskelistan?:  ")
    with open (f"{a}.txt", "r", encoding="utf8") as öl:
        for lines in öl.readlines():
            print(f"{lines}")

def main():
    k = meny()
    if k == 1:        
        skapa_öl()
    if k == 2:
        läsup_öl()


if __name__ == "__main__":
    main()