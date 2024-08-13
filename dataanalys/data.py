import requests
from bs4 import BeautifulSoup

def ambil_konten(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa apakah ada kesalahan HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error mengambil data dari website: {e}")
        return None

def cari_kata_dalam_konten(konten, kata):
    soup = BeautifulSoup(konten, 'html.parser')
    teks = soup.get_text()
    kata_ditemukan = teks.lower().count(kata.lower())
    return kata_ditemukan

def program_cari_kata():
    url = input("Masukkan URL website: ")
    kata = input("Masukkan kata yang ingin dicari: ")

    konten = ambil_konten(url)
    if konten:
        jumlah_kata = cari_kata_dalam_konten(konten, kata)
        print(f"Kata '{kata}' ditemukan sebanyak {jumlah_kata} kali di dalam website.")

if __name__ == "__main__":
    program_cari_kata()
