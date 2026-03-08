sentences = "Gunung berapi aktif Gunung Kelud ini terletak di perbatasan Kediri, Blitar, dan Malang. Gunung Kelud meletus dahsyat tanggal 13 Februari 2014. Jutaan material padat dan gas disemburkan terlontar ke angkasa. Material-material berat (batu, kerikil, dan pasir) jatuh kembali di sekitar Gunung Kelud. Abunya terbawa angin hinggga menyebar hampir ke seluruh Pulau Jawa. Kini Gunung Kelud telah berubah total. Puncak yang dahulu dihiasi dengan kubah lava kini Kawasan Wisata Gunung Kelud telah berubah menjadi lubang kawah terisi sedimentasi air. Lereng gunung kini menghijau. Pemandangan indah kawah dan pegunungan sekitar inilah yang menjadi daya tarik kawasan ini. Sebelum beranjak pulang, tak lengkap jika tak membawa oleh-oleh khas Gunung Kelud. Tersedia berbagai macam oleh-oleh khas dari Gunung Kelud mulai dari souvenir, makanan khas, serta buah nanas yang banyak ditanam di daerah ini."

# lowercase 
def lowercase(sentences: str) -> str:
    return sentences.lower()
# tokenisasi 
def tokenize(senetences: str) -> str:
    return senetences.split()

stopwords = ["ini", "di", "dan", "jutaan", "ke", "kini", "telah", "kini", "inilah", "yang", "sebelum", "tak", "dari", "kembali", "sekitar", "hingga", "hampir", "dengan"]

def remove_stopwords(list_stop: list, tokenize: str) -> list:
    new_token = []
    for token in tokenize:
        if token not in list_stop:
            new_token.append(token)
    return new_token

if __name__ == "__main__":
    lower_sentences = lowercase(sentences)
    token_sentences = tokenize(lower_sentences)
    new_token_sentences = remove_stopwords(stopwords, token_sentences)

    print(new_token_sentences)