Index = 2

PreviousFibbonaci = 1
Fibbonaci = 1 

while True:
    if len(str(Fibbonaci)) == 1000:
        break
    temp = Fibbonaci
    Fibbonaci += PreviousFibbonaci
    PreviousFibbonaci = temp
    Index += 1
print(Fibbonaci)

print(f"Found: {Index}")