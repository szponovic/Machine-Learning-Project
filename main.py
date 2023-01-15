import functions
import pandas as pd

pd.options.display.large_repr = 'info'
path = "Screen-Time-Data.csv"
df = pd.read_csv(path, encoding="ISO-8859-1")
df2 = df
del df2["Date"]
del df2["Week Day"]
del df["index"]

df.rename(columns={"Reading and Reference": "Read & Ref"}, inplace=True)
df.rename(columns={"Health and Fitness": "Fit"}, inplace=True)
df.rename(columns={"Total Screen Time ": "Screen Time"}, inplace=True)
df.rename(columns={"Productivity": "Product"}, inplace=True)
df.rename(columns={"Creativity": "Creat"}, inplace=True)
df.rename(columns={"Entertainment": "Ente"}, inplace=True)

print(
    "Witaj w programie wyswietlajacym korelacje wplywu jogi na styl zycia...\n"
    "Wybierz akcje jaka chcialbys wykonac"
)

while True:
    functions.display()
    chose = input("Wpisz wybor: ")
    functions.choices(chose)

    if chose == "1":
        functions.create_table(path)

    if chose == "3":
        functions.box_plot()

    elif chose == "4":  # Histogram
        functions.histogram()

    elif chose == "5":  # Funkcja wyswietlajca wartosci max i min z wszystkich kolumn
        functions.display_statistics()

    elif chose == "6":  # wyznaczenie macierzy korelacji
        functions.create_correlation_heatmap(df2)

    elif chose == "7":
        print("Testowanie modeli:")
        functions.train_and_compare_models(df2)

    elif chose == "0":
        break
