Nama : Ria Lavenia Kharissa

NPM : 2506543905

Kelas : PBP A

## Tugas 1

1. Saya menggunakan elemen semantik HTML5 pada web portoffolio saya, yaitu elemen <section>, <header>, dan <footer>. Elemen ini membantu saya dalam menyusun kerangka static web saya sehingga struktur dokumen saya dapat tersusun dengan lebih terorganisir dan readable. Elemen semantik HTML5 ini juga memudahkan saya dalam melakukan styling pada CSS.

2. Tantangan utama saya adalah menyusun layout desktop berbasis grid dua kolom dimana foto profil berada di sebelah kanan teks identitas dan bio menjadi bertumpuk secara vertikal dan berposisi di tengah(center). Selain itu, mengubah navigasi yang awalnya horizontal menjadi menu dropdown garis tiga(hamburger) juga lumayan menantang bagi saya. Saya mengevaluasieleman mana yang harus diubah posisinya dengan berpikir apa yang harus dilihat oleh user pertama kali saat membuka web portofolio saya. Saya meyakini bahwa nama/identitas harus berada di posisi teratas, diikuti foto, dan terakhir bio/penjelasan. saya meyakini bahwa urutan seperti ini adalah urutan yang seimbang. Kemudian untuk ukuran, pada layar desktop ukuran nama dibuat sangat besar karena layar desktop yang luas. Saat berpindah ke layar mobile, saya mengurangi ukurannya dan memastikan teks diatur menjadi rata tengah agar tidak terpotong saat layar menjadi sempit.

3. Website yang saya buat saat ini adalah static web murni, sehingga batasan utama yang saya rasakan adalah setiap konten didalamnya yang harus saya tulis ulang ketika saya ingin menambah atau mengubah sesuatu. Misalnya jika saya ingin menambah pengalaman saya, maka  saya harus menulis lagi di HTML atau mengubah hal tertentu lagi di CSS. Selain itu, fitur email yang disajikan saat ini bukan mengirim secara langsung, tetapi meminta browser untuk membuka Gmail di device user. Oleh karena itu, fungsionalitas dinamis yang ingin saya tambahkan adalah fitur untuk menambah/mengedit pengalaman dan foto saya tanpa harus membuka kode dan form yang dapat langsung mengirim pesan ke email saya atau tersimpan di database


## Penggunaan AI

Saya menggunaka bantuan AI(Gemini) dalam mengerjakan tugas ini. Saya menggunakan AI untuk:

- Merancang hamburger menu interaktif menggunakan checkbox
- Menambahkan efek gradasi warna bergerak(animated gradient) pada latar belakang foto profil
- Memahami fungsi horizontal scrolling pada section Experience menggunakan properti CSS seperti `overflow-x` `scroll-snap`, dan kustomisasi tampilan scrollbar dengan `::-webkit-scrollbar` agar kartu pengalamannya dapat bergeser dan estetik.

## Tugas 2

1. Alurkerja Django saat Pengguna Membuka Halaman Projects:
- Pengguna mengetik alamat web di browser(contoh: `/experience/`)
- routing utama, yaitu Django menerima permintaan lalu melemparnya ke file pengatur alamat(`main/urls.py`)
- routing aplikasi. Terjadi ketika file mencocokkan alamat `/experience/` dengan dungsi pemrosesannya di `views.py`, yaitu `show_experience`.
- pemrosesan utama, dimana fungsi `show_experience` menghubungi model untuk meminta daftar experience
- model dan database. Model mengambil data experience yang tersimpan lalu menyerahkannya kembali ke view.
- template, yaitu `experience.html`. View membungkus data experience ke dalam contex lalu mengumpankannya ke berkas html(`experience.html`). disini django template language memproses dan merender data satu per satu menjadi bentuk kartu pengalaman
- tampilan akhir. Server mengirimkan hasil akhir berupa html utuk kembali ke browser pengguna untuk ditampilkan ke layar.

2. Alasan menggunakan model adalah agar ketika kita ingin mengedit proyek, kita cukup memperbaruinya dari shell/database tanpa perlu membongkar kode html lagi. selain itu, kode juga lebih rapi dan data lebih dinamis

3. Perbedaan `makemigrations` dan `migrate` adalah:
- `makemigrations`: membuat draf rencana perubahan.
- `migrate`: menerapkan rencana secara nyata ke database. `migrate` mengeksekusi catatan dari `makemigrations` dan langsung membuatkan kolom/tabel di database
- contoh: ketika menambahkan field `thumbnail = models.URLField(...)` di `models.py`, kita wajib menjalankan `python manage.py makemigrations` untuk membuat drafnya, kemudian menjalankan `python manage.py migrate` supaya kolom tersebut dibuat di dalam tabel database.

## Penggunaan AI

Saya menggunaka bantuan AI(Gemini) dalam mengerjakan tugas 2 ini. Saya menggunakan AI untuk:

- Membantu merancang sttruktur model `Project` serta menanganipenambahan field baru
- Menyusun skenario pengujian pada `test,py`
- memahami alur request response Django dan membedah konsep dasar untuk menjawab pertanyaan reflektif no 1 pada tugas 2

### Tugas 3

1. Penggunaan `ModelForm` alih-alih form HTML manual:
    `ModelForm` digunakan karena memiliki beberapa manfaat, yaitu menghemat waktu, menyederhanakan validasi, menghindari pengulangan logika, dan meningkatkan keamanan. Selain itu, `ModelForm` memiliki fitur otomatis yang cocok untuk proses CRUD. Dengan `ModelForm1 kita dapat mengambil field dan aturan validasi dari model secara otomatis, sehingga kita tidak perlu menulis ulang kode.

    Mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form:
    Penambahan `{% csrf_token %}` digunakan untuk melindungi aplikasi dari serangan keamanan Cross-Site Request Forgery(CSRF). Serangan yang ada dapat berupa pencurian data pribaadi,transaksi tidak sah, hingga perubahan data penting.

2. JSON lebih disukai dalam pengembangan aplikasi web dibandiing XML karena penulisan JSON yang jauh lebih pendek dan simple karena hanya menggunakan tanda kurung dan titik dua. Selain itu, ukuran filenya lebih kecil sehingga proses pengiriman data di internet jauh lebih cepat. JSON juga mudahh dipahami oleh javascrpt

3. Alur data pada fungsi `view`:
    Awalnya, browser akan meminta data lewat alamat link tertentu, kemudian Django akan menyambungkan alamat tersebut ke fungsi view yang bertugas untuk mengambil data dari database. Setelah itu, view mengambil daftar data yang ada di database menggunakan perintah Django, data yang diambil diubah menjadi text JSON dengan proses serialisasi. Kemudian, JSON akan dikirimkan kembali ke browser

    Mengapa kita perlu melakukan proses serialization pada model Django:
        proses serialization diperlukan karena data yang diambil dari database masih berbentuk object bawaan Python yang tersimpan di memori komputer server.Object Python ini tidak dapat dikirimkan lewat jaringan internet ke browser, oleh sebab itu kita perlu serialisasi untuk menerjemahkan aobjek  Python tersebut menjadi text standarberupa_JSON.


## Penggunaan AI

Saya menggunaka bantuan AI(Gemini) dalam mengerjakan tugas 3 ini. Saya menggunakan AI untuk:

Prompting:
- memberikan potongan kode
- memperbaiki bug yang ada di dalam CSS
- membantu dalam membuat `tests.py`


Keterbatasan AI:
- Menganggap atribut yang tidak adamenjadi ada
- Karena yang ditanyakan hanyapotongan kode, AI memberikan banyak solusi yang tidak sesuai dengan codenya, hal ini menyebabkan test gagal

perbaikan yang saya lakukan:
- memperbaiki typo yang ada pada pada code
- tidak menyalin, tetapi memahami apa maksud AI dan menyesuaikannya pada code.
