import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    #Kasus 3 - Pengambilan Keputusan Pembersihan Data
    - Data Engineering
    - Ludy Hasby Aulia : 2702409305
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ##Load Library
    """)
    return


@app.cell
def _():
    import pandas as pd
    import csv
    import numpy as np
    from sklearn.impute import KNNImputer
    import time
    import matplotlib.pyplot as plt
    import re
    return KNNImputer, np, pd, plt, re


@app.cell
def _(mo):
    mo.md("""
    ##Dataset
    """)
    return


@app.cell
def _(np, pd):
    customers = pd.DataFrame({ 
        "customer_id": ["C001", "C002", "C003", "C004", "C005", "C006", "C007"], 
        "age": [25, np.nan, 17, 150, 45, np.nan, 23], 
        "income": [5000000, 8000000, -100000, 150000000, 6000000, np.nan, 4500000], 
        "email": ["ani@mail.com", None, "budi@@mail.com", "citra@mail.com", None, "doni@mail.com", "invalid"],
        "city": ["Jakarta", "Bandung", "Jakarta", "Unknown", "Medan", "Surabaya", "jakarta"], 
        "signup_date": ["2025-01-15", "2025-02-30", "2024-13-01", "2025-01-25", "2025-01-20", "2025-01-18", "2025-01-22"]
    }) 
    return (customers,)


@app.cell
def _(mo):
    mo.md("""
    ##Kolom Age - Nilai Hilang dan Tidak Valid
    """)
    return


@app.cell
def _(customers):
    customers.age.isnull().sum()
    # terdapat 2 dari 7 data kosong
    return


@app.cell
def _(customers):
    customers.age.info()
    return


@app.cell
def _(customers):
    customers
    return


@app.cell
def _(customers, np):
    customers.loc[(customers["age"] < 18) | (customers["age"] > 100), "age"] = np.nan
    return


@app.cell
def _(KNNImputer, customers):
    imputer = KNNImputer(n_neighbors=5)
    customers[["age", "income"]] = imputer.fit_transform(customers[["age", "income"]])
    return


@app.cell
def _(customers):
    customers
    return


@app.cell
def _(mo):
    mo.md("""
    ##Kolom Income
    """)
    return


@app.cell
def _(customers):
    customers
    return


@app.cell
def _(customers):
    customers[customers["income"] < 0]
    return


@app.cell
def _(customers, plt):
    data = customers.income
    plt.figure(figsize=(10,5))
    plt.boxplot(data, vert=False)
    plt.title("Boxplot Pendapatan Pelanggan")
    plt.xlabel("Income")
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("""
    ##Kolom Email
    """)
    return


@app.cell
def _(re):
    # fungsi validasi email 
    def validate_email(email):
        r_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        email = str(email).strip().lower()
        return bool(re.match(r_pattern, email))
    return (validate_email,)


@app.cell
def _(validate_email):
    validate_email("")
    return


@app.cell
def _(customers, validate_email):
    customers[customers['email'].apply(validate_email)==False]
    return


@app.cell
def _(customers):
    customers.loc[2, 'email'] = 'budi@mail.com'
    return


@app.cell
def _(customers):
    customers.email
    return


@app.cell
def _(mo):
    mo.md("""
    ##Kolom City
    """)
    return


@app.function
def cleaning_city(city: str) -> str:
    return city.strip().title()


@app.cell
def _(customers):
    customers["city"] = customers["city"].apply(cleaning_city)
    return


@app.cell
def _(customers):
    customers.city.unique()
    return


@app.cell
def _(customers, np):
    customers.city = customers.city.replace("Unknown", np.nan)
    return


@app.cell
def _(customers):
    customers.city.unique()
    return


@app.cell
def _(customers):
    customers.city.value_counts().sort_values().values
    return


@app.cell
def _(customers, plt):
    # bar chart pelanggan per kota
    data2 = customers.city.value_counts().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(x=data2.index, height=data2.values, color='skyblue')
    plt.title("Perbandingan Jumlah Sampel Pelanggan\nPer Kota")
    plt.xlabel("Kota")
    plt.ylabel("Jumlah")
    plt.grid(axis='y')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
