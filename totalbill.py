def totalcalc(billamount, tipperc):
    totalbill=billamount*(1 + 0.01*tipperc)
    total=round(totalbill ,2)
    print(f"please pay ${total}")

totalcalc(150, 20)