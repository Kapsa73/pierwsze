tekst = "Natenczas Wojski chwycił na taśmie przypięty swój róg bawoli długi, centkowany, kręty. I zadął. Dźwięk jak wicher niewstrzymanym dechem, niesie w puszczę muzykę i podwaja echem."
print(tekst)
print()


def podziel(a):
    odcinek = 0
    podzielony_tekst = ""
    for i in a:
        odcinek += 1
        if odcinek > 50 and i == " ":
            podzielony_tekst += "\n"
            odcinek = 0
        else:
            podzielony_tekst += i
    return podzielony_tekst


x = podziel(tekst)
print(x)
