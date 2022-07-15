# **BAB 2**

# **Percabangan**

Pada flowchart, logika "jika…maka" digambarkan dalam bentuk cabang. Hal inilah yang disebut dengan percabangan. Selain percabangan, struktur ini juga disebut control flow, decision, struktur kondisi, Struktur if, dsb. Percabangan akan mampu membuat program berpikir dan menentukan tindakan sesuai dengan logika/kondisi yang kita berikan. Tidak seperti bahasa pemrograman lainnya, Python hanya mengenal satu fungsi percabangan (kondisi) saja. Tidak ada switch atau case dalam python, tetapi hanya fungsi if saja. Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalannya program dan menentukan tindakan apa yang akan diambil sesuai dengan kondisi.

![](img/Aspose.Words.f3adbccc-e2e3-42a9-82d3-c56ddd5f1e24.001.png)

## **Struktur Percabangan If**

Percabangan If digunakan saat terdapat satu pilihan keputusan. Blok kode if pada python, memiliki struktur sebagai berikut:

```
if kondisi:
    statements()
```

Bagian kondisi adalah sebuah variabel / atau nilai yang bertipe data boolean. Baik berupa nilai True/False secara langsung, ataupun sebuah ekspresi logika. Jika kondisi bernilai True, maka statements() akan dieksekusi oleh sistem.

Contoh program if:

```
bilangan = 4

if bilangan < 10:
    print("%d adalah bilangan kurang dari 10" % bilangan)
```

“Jika bilangan < "10" maka cetak teks " bilangan adalah bilangan kurang dari 10"” Disini menggunakan operator relasi kurang dari (<) untuk membandingkan isi variabel bilangan. Sedangkan tanda titik-dua (:) adalah tanda untuk memulai blok kode If.

**Perlu diingat**

**Penulisan blok If, harus diberikan indentasi tab atau spasi 2x.**

## **Struktur Percabangan If/Else**

Percabangan If/Else digunakan saat terdapat dua pilihan keputusan.

Misalkan, jika umur diatas atau sama dengan 18 tahun disebut. Sedangkan di bawah itu belum dewasa. Maka flowchartnya adalah sebagai berikut:

![](img/Aspose.Words.f3adbccc-e2e3-42a9-82d3-c56ddd5f1e24.003.png)

Maka bisa membuatnya dalam program:

```
umur = input("Berapa umur kamu: ")

if umur >= 18:
    print("Dewasa")

else:
    print("Belum Dewasa")
```

Selain blok If, terdapat juga blok Else yang akan dieksekusi apabila kondisi umur >= 18 salah (False).

## **Struktur Percabangan If/Elif/Else**

Percabangan If/Elif/Else digunakan apabila terdapat lebih dari dua pilihan keputusan.

Blok kode If/Elif/Else pada python, memiliki struktur sebagai berikut:

```
if begini:
    maka ini
elif begitu:
    maka itu
else:
seperti ini
```

Contoh yang paling umum digunakan untuk kasus percabangan if..elif..else adalah menentukan grade nilai suatu siswa.

Jika nilainya sekian, dia dapat predikat A. Sedangkan jika nilainya sekian maka predikatnya adalah B, dan seterusnya.

Berikut ini aturan yang akan kita gunakan:

1. Predikat A untuk nilai >= 90
1. Predikat B untuk nilai >= 80 < 90
1. Predikat C untuk nilai >= 60 < 80
1. Predikat D untuk nilai >= 40 < 60
1. Selain itu, maka predikat E.

Dari 5 aturan di atas, kita akan menggunakan satu if, 3 elif, dan 1 else.

Berikut adalah contohnya:

```
nilai = int(input('Masukkan nilai: '))

if nilai >= 90:
    print('Predikat A')

elif nilai >= 80:
    print('Predikat B')

elif nilai >= 60:
    print('Predikat C')

elif nilai >= 40:
    print('Predikat D')

else:
    print('Predikat E')

```
