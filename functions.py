from sklearn import model_selection, linear_model, ensemble, metrics
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from prettytable import PrettyTable
import csv


path = "Screen-Time-Data.csv"
df = pd.read_csv(path, encoding="ISO-8859-1")  # zapis Dataframe do zmiennej
df2 = df
del df2["Date"]
del df2["Week Day"]
del df["index"]

# Poprawa wyswietlania zmiennych w tabeli
df.rename(columns={"Reading and Reference": "Read & Ref"}, inplace=True)
df.rename(columns={"Health and Fitness": "Fit"}, inplace=True)
df.rename(columns={"Total Screen Time ": "Screen Time"}, inplace=True)
df.rename(columns={"Productivity": "Product"}, inplace=True)
df.rename(columns={"Creativity": "Creat"}, inplace=True)
df.rename(columns={"Entertainment": "Ente"}, inplace=True)
table_joga = df.to_string()
tab_info = df.info()


def create_table(file_path):
    table = PrettyTable()

    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        table.field_names = header

        for line in csv_reader:
            table.add_row(line)

    print(table)


def box_plot():
    df["Screen Time"].plot(kind="box")
    print("Total screen Time - Czas spedzony w telefonie [min]")
    plt.show()
    df["Social Networking"].plot(kind="box")
    print("Social Networking - Czas spedzony na portalach spolecznosciowych [min]")
    plt.show()
    df["Product"].plot(kind="box")
    print("Productivity - Produktywne czynnosci")
    plt.show()
    df["Read & Ref"].plot(kind="box")
    print("Reading & Reference -Czytanie, artykuły, podnoszenie umiejętności")
    plt.show()

def display():
    options = {
        '1': 'tabela',
        '2': 'info',
        '3': 'wykres pudelkowy',
        '4': 'histogram',
        '5': 'Wartosc max',
        '6': 'Korelacja',
        '7': 'Testowanie modeli',
        '0': 'Zakoncz'
    }
    print("Wybierz opcje: ")
    for key, value in options.items():
        print(key, '-', value)

def choices(chose):
    if chose == "1":
        print("--tabela--")
    elif chose == "2":
        print("--info--")
        print("Week Day - Dzien tygodnia")
        print("Total screen Time - Czas spedzony w telefonie [min]")
        print("Social Networking - Czas spedzony na portalach spolecznosciowych [min]")
        print("Reading & Reference -Czytanie, artykuły, podnoszenie umiejętności")
        print("Others - Inne")
        print("Productivity - Produktywne czynnosci")
        print("Health & Fitness Zdrowie i cwiczenia")
        print("Entertainment - rozrywka")
        print("Creativity - Kreatywność w danym dniu ")
        print("Yoga - Odbyte ćwiczenia Yogi ")
    elif chose == "3":
        print("3 - wykresy pudelkowe")
    elif chose == "4":
        print("4 - histogram")
    elif chose == "5":
        print("5 - Wart max")
    elif chose == "6":
        print("6 - Wart korelacji")
    elif chose == "7":
        print("7 - Testowanie modeli")
    elif chose == "0":
        print("0 - zakoncz")
    elif (
        chose != "1"
        or chose != "2"
        or chose != "3"
        or chose != "0"
        or chose != "4"
        or chose != "5"
        or chose != "6"
        or chose != "7"
    ):
        print("Zly wybor")


def display_statistics():
    columns = [col for col in df.columns if col not in ["Date", "Week Day"]]
    statistics = {}
    for column_name in columns:
        mean = df[column_name].mean()
        median = df[column_name].median()
        mode = df[column_name].mode()[0]
        statistics[column_name] = {"Mean": mean, "Median": median, "Mode": mode}

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    plt.title("Statistics")
    plt.xlabel("Statistic")
    plt.ylabel("Value")
    for column_name, values in statistics.items():
        plt.bar(values.keys(), values.values(), label=column_name)
    plt.legend()
    plt.show()


def histogram():
    df["Other"].hist()
    print("Czestotliwosc wystepowania innych aktywnosci")
    plt.show()


def train_and_compare_models(df2):
    X = df2.drop("Screen Time", axis=1).to_numpy()
    y = df2.drop("Screen Time", axis=1).to_numpy()

    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.2, random_state=12345
    )

    def train_model(classifier, feature_vector_train, label, feature_vector_valid):
        classifier.fit(feature_vector_train, label)
        with open("screen_classifier.pickle", "wb") as handle:
            pickle.dump(classifier, handle)
        predictions = classifier.predict(feature_vector_valid)
        score_vals = [
            metrics.mean_squared_error(predictions, y_test),
            metrics.mean_absolute_error(predictions, y_test),
        ]
        return score_vals

    accuracy = train_model(linear_model.LinearRegression(), X_train, y_train, X_test)
    accuracy_compare = {"LR": accuracy}
    print("LR: ", accuracy)

    regressor = ensemble.RandomForestRegressor(n_estimators=100, random_state=0)
    accuracy = train_model(regressor, X_train, y_train, X_test)
    accuracy_compare["random forrest tree"] = accuracy
    print("random forrest tree", accuracy)

    df_compare = pd.DataFrame(accuracy_compare, index=["mse", "mae"])
    df_compare.plot(kind="bar")
    print("MAE - Mean Abolute Error (Sredni blad bezwzgledny)")
    print("MSE - Mean Squared Error- (Sredni blad do kwadratu)")
    plt.show()


def create_correlation_heatmap(df2):
    korelacja = df2.corr()
    print(korelacja)
    fig, ax = plt.subplots(figsize=(10, 10))
    colormap = sns.color_palette("BrBG", 10)
    sns.heatmap(korelacja, cmap=colormap, annot=True, fmt=".2f")
    ax.set_yticklabels(df2.columns)
    plt.show()
