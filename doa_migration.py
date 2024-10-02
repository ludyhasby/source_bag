import streamlit as st
import webbrowser
import time

st.write("Website ini telah di migrasi pada https://doa.afin.store/. Silahkan mengunjungi link tersebut, anda akan diarahkan ke https://doa.afin.store/ dalam beberapa saat.")
my_bar = st.progress(0, text="Waiting Respons to Redirect")

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text="Waiting Respons to Redirect")
time.sleep(1)
my_bar.empty()
webbrowser.open_new_tab('https://doa.afin.store/')