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
    #Kasus 4 - Operasi Group dan Wawasan
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
    import numpy as np
    return np, pd


@app.cell
def _(mo):
    mo.md("""
    ##Dataset
    """)
    return


@app.cell
def _(np):
    np.random.seed(42) 
    return


@app.cell
def _(np, pd):
    n = 1000 
    transactions = pd.DataFrame({ 
        "transaction_id": [f"T{i:04d}" for i in range(1, n+1)], 
        "seller_id": np.random.choice(["S001", "S002", "S003", "S004", "S005"], n), 
        "category": np.random.choice(["Electronics", "Fashion", "Food", "Home", "Beauty"], n), 
        "amount": np.random.randint(50000, 1000000, n), 
        "quantity": np.random.randint(1, 10, n), 
        "payment_method": np.random.choice(["Credit Card", "E-Wallet", "Bank Transfer", "COD"], n), 
        "city": np.random.choice(["Jakarta", "Bandung", "Surabaya", "Medan", "Makassar"], n), 
        "date": pd.date_range("2025-01-01", periods=n), 
        "status": np.random.choice(["completed", "cancelled", "pending"], n, p=[0.7, 0.2, 0.1]) 
    }) 
    return (transactions,)


@app.cell
def _(transactions):
    transactions
    return


@app.cell
def _(mo):
    mo.md("""
    ##Group Dasar dan Wawasan
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ###Penjualan setiap Penjual
    """)
    return


@app.cell
def _(transactions):
    # hitung pendapatan per penjual
    revenuePerSeller = transactions.groupby("seller_id")["amount"].sum().sort_values(ascending=False).reset_index()
    revenuePerSeller
    return (revenuePerSeller,)


@app.cell
def _(mo):
    mo.md("""
    ###Persentase setiap Penjual terhadap total
    """)
    return


@app.cell
def _(revenuePerSeller, transactions):
    totalRevenue = transactions['amount'].sum()

    revenuePerSeller['percentageP'] = revenuePerSeller['amount']/totalRevenue
    return


@app.cell
def _(revenuePerSeller):
    revenuePerSeller
    return


@app.cell
def _(mo):
    mo.md("""
    ###Rata-rata Jumlah Transaksi per Kategori
    """)
    return


@app.cell
def _(transactions):
    meanCategory = transactions.groupby("category")["quantity"].mean().sort_values(ascending=False)
    meanCategory
    return


@app.cell
def _(mo):
    mo.md("""
    ##Group Multilevel
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ###Total Pendapatan berdasar seller_id dan category
    """)
    return


@app.cell
def _(transactions):
    sellerCategory = transactions.groupby(["seller_id", "category"])["amount"].sum().reset_index().sort_values('amount', ascending=False)
    sellerCategory
    return (sellerCategory,)


@app.cell
def _(mo):
    mo.md("""
    ###Pivot Tabel Seller - Category
    """)
    return


@app.cell
def _(transactions):
    pivotSellerCategory = transactions.pivot_table(
        index="seller_id", 
        columns="category", 
        values="amount", 
        aggfunc="sum"
    )

    pivotSellerCategory
    return


@app.cell
def _(mo):
    mo.md("""
    ###Kategori terbaik setiap seller
    """)
    return


@app.cell
def _(sellerCategory):
    topCategoryPerSeller = sellerCategory.drop_duplicates(subset=['seller_id'], keep='first')
    print(topCategoryPerSeller)
    return


@app.cell
def _(mo):
    mo.md("""
    ##Agregasi Kustom
    """)
    return


@app.cell
def _(transactions):
    def mean_transaksi_complete(x):
        mask = transactions.loc[x.index, "status"] == "completed"
        return x[mask].mean()
    return (mean_transaksi_complete,)


@app.cell
def _(transactions):
    def total_pendapatan_complete(x):
        mask = transactions.loc[x.index, "status"] == "completed"
        return x[mask].sum()
    return (total_pendapatan_complete,)


@app.function
def tingkat_penyelesaian(x):
    return (x == "completed").sum() / len(x)


@app.function
def get_mode(x):
    return x.mode().iloc[0] if not x.mode().empty else None


@app.cell
def _(mean_transaksi_complete, total_pendapatan_complete, transactions):
    customeAgg = transactions.groupby('seller_id').agg(
        jumlah_transaksi=('transaction_id', 'count'),
        total_pendapatan_complete=('amount', total_pendapatan_complete), 
        mean_transaksi_complete=('quantity', mean_transaksi_complete), 
        tingkat_penyelesaian=('status', tingkat_penyelesaian), 
        metode_bayar_umum=('payment_method', get_mode)   
    )

    customeAgg
    return (customeAgg,)


@app.cell
def _(customeAgg):
    # tambahkan peringkat 
    customeAgg['rank_pendapatan'] = customeAgg['total_pendapatan_complete'].rank(ascending=False, method='dense').astype(int)

    customeAgg
    return


@app.cell
def _(customeAgg):
    # penjual yang layak diberi reward 
    customeAgg.sort_values(["total_pendapatan_complete", "tingkat_penyelesaian"], ascending=False)
    return


@app.cell
def _(customeAgg):
    # penjual perlu diperhatikan 
    customeAgg.sort_values(["tingkat_penyelesaian", "total_pendapatan_complete"], ascending=True)
    return


if __name__ == "__main__":
    app.run()
