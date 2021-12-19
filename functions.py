import pandas as pd
from csv import writer
from datetime import date

# df = pd.read_csv("EuroMillions_numbers.csv")


def addData(date: date, n1: int, n2: int, n3: int, n4: int, n5: int, e1: int, e2: int, win: int, gain: int):
    # row = ListeNum.dict()
    # res = list(row.values())
    res = []
    res.append(date)
    res.append(n1)
    res.append(n2)
    res.append(n3)
    res.append(n4)
    res.append(n5)
    res.append(e1)
    res.append(e2)
    res.append(win)
    res.append(gain)
    with open('EuroMillions_numbers.csv', 'a') as f_object:
        writer_object = writer(f_object,delimiter=';')
        writer_object.writerow(res)
        f_object.close()
    

