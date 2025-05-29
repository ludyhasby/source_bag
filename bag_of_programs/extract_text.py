import fitz
doc = fitz.open("test.pdf")
counter = 0
print("Hasil Ekstraksi Request Clients")
for page in doc:
    text = page.get_text()
    if "Nama" in text:
        print(f"Nama Koruptor\t:", text.split()[78])
        for count, i in enumerate(text.split()):
            if i == "Pekerjaan":
                start_pekerjaan = count+2
            if i == "Terdakwa":
                end_pekerjaan = count-1
        print(f"Pekerjaan\t:", " ".join(text.split()[start_pekerjaan:end_pekerjaan]))
    if "Jumlah kerugian Negara" in text:
        print(f"Total Kerugian Negara\t:", text.split()[232])
        break