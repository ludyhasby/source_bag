import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(np, pd):
    import sys
    import platform

    def print_system_specs():
        print("="*30)
        print("🖥️  SYSTEM SPECIFICATIONS")
        print("="*30)
        print(f"OS           : {platform.system()} {platform.release()}")
        print(f"Processor    : {platform.processor()}")
        print(f"Python Ver   : {sys.version.split()[0]}")
        print(f"Pandas Ver   : {pd.__version__}")
        print(f"Numpy Ver    : {np.__version__}")
        print("="*30 + "\n")

    # Panggil fungsi ini sebelum test dimulai
    print_system_specs()
    return


@app.cell
def _(mo):
    mo.md("""
    #Pengujian Pendekatan A dan B
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
    import tracemalloc
    import time
    return csv, np, pd, time, tracemalloc


@app.cell
def _(mo):
    mo.md("""
    ##File Creation
    """)
    return


@app.cell
def _(csv, np):
    with open("compare.csv", newline='', mode='w') as csvFile:
        w = csv.writer(csvFile, delimiter=';')
        w.writerow([f"col_{i+1}" for i in range(50)])
        w.writerows(np.random.randn(10000, 50))
    return


@app.cell
def _(time, tracemalloc):
    # fungsi pemuatan 
    def data_load(func: callable, *args, **kwargs) -> dict:
        # trace memory 
        tracemalloc.start()
        # trace time 
        startTime = time.time()
        result = func(*args, **kwargs)
        # take time and memory
        endTime = time.time()
        currentMemory, peakMemory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # printable 
        execTime = endTime - startTime 
        print(f"Waktu Eksekusi : {execTime:.4f} detik")
        print(f"Peak Memory    : {peakMemory / 1024 / 1024:.2f} MB")
    
        return {
            "head_result": result.head(),
            "time_seconds": execTime,
            "peak_memory_mb": peakMemory / 1024 / 1024
        }
    return (data_load,)


@app.cell
def _(mo):
    mo.md("""
    ##Perbandingan Pendekatan
    """)
    return


@app.cell
def _():
    selectCols = [f"col_{i+1}" for i in range(5)]
    return (selectCols,)


@app.cell
def _(mo):
    mo.md("""
    ###Pendekatan A
    """)
    return


@app.cell
def _(pd, selectCols):
    def pendekatan_A():
        df = pd.read_csv('compare.csv', sep=";")
        # filter 
        return df[selectCols]
    
    return (pendekatan_A,)


@app.cell
def _(data_load, pendekatan_A):
    print("-- Pengujian Pendekatan A --")
    data_load(pendekatan_A)
    return


@app.cell
def _(mo):
    mo.md("""
    ###Pendekatan B
    """)
    return


@app.cell
def _(pd, selectCols):
    def pendekatan_B():
        return pd.read_csv('compare.csv', sep=";", usecols=selectCols)
    
    return (pendekatan_B,)


@app.cell
def _(data_load, pendekatan_B):
    print("-- Pengujian Pendekatan B --")
    data_load(pendekatan_B)
    return


if __name__ == "__main__":
    app.run()
