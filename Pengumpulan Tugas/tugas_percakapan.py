nama1=input("masukan nama pembeli :")
nama2=input("masukan nama penjual :")

def penjual():
    print(f"{nama2} Selamat datang di toko kami! Nama saya " f"{nama2}. Apa yang bisa saya bantu?")
    print(f"{nama1} Saya ingin membeli buah.")
    buah = input(f"{nama2} buah apa yang Anda cari? ")
    if buah.lower() in ['apel', 'jeruk', 'pisang','semangka']:
        print(f"{nama2} Kami memiliki {buah} segar di sini. Berapa banyak {buah} yang Anda butuhkan?")
        jumlah = input(f"{nama1}: ")
        print(f"{nama2} Baik, Anda memesan {jumlah} {buah}. Total harga adalah {int(jumlah) * 5000} IDR.")
        print(f"{nama2} Terima kasih atas pembelian Anda! Pesanan Anda akan segera diproses.")
        
    else:
        print(f"{nama2} Maaf, kami tidak memiliki {buah} saat ini. kami memiliki buah apel jeruk pisang dan semangka yang segar")
         
def main():
    penjual()

if __name__ == "__main__":
    main()
