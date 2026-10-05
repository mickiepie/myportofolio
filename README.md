Nama : Ria Lavenia Kharissa

NPM : 2506543905

Kelas : PBP A


## Progress Pengerjaan & Dokumentasi Mingguan

* **Minggu 1 (Tugas 1)**
  * **Target:** Merancang struktur awal portofolio statis dengan semantic HTML5 dan CSS responsif.
  * **Implementasi:** Menyusun tata letak halaman utama, penggunaan efek *animated gradient*, *polaroid card*, dan lainnya.
  * **Hasil:** Halaman web berhasil menampilkan identitas dan adaptif di layar desktop maupun layar ponsel kecil.

* **Minggu 2 (Tugas 2)**
  * **Target:** Implementasi Model-View-Template (MVT) pada Django.
  * **Implementasi:** Mengatur *routing* URL dan *views*, mendefinisikan skema model `Project`, menjalankan `makemigrations` dan `migrate`, serta menyusun `tests.py`.
  * **Hasil:** Halaman *Projects* dapat bekerja dengan baik dan seluruh *test case* berhasil lulus.

* **Minggu 3 (Tugas 3)**
  * **Target:** Menerapkan mekanisme form & data delivery
  * **Implementasi:** Membuat formulir berbasis `ModelForm` dengan proteksi `{% csrf_token %}`, menyusun alur penambahan dan pengeditan data proyek/pengalaman.
  * **Hasil:** Fitur formulir CRUD berjalan lancar di lingkungan lokal maupun server PWS.

  * **Minggu 4 (Tugas 4)**
  * **Target:** Menerapkan pola autentikasi dan otorisasi dengan sistem autentikasi Django.
  * **Implementasi:** Mengonfigurasi grup `Editor` via Django Admin dan membatasi akses fungsi menggunakan `raise PermissionDenied`. Mengimplementasikan fitur *Star* dan menyembunyikan tombol aksi pada template berdasarkan otorisasi pengguna.
  * **Hasil:** Sistem autentikasi dan otorisasi berfungsi dengan baik, fitur interaktif *star* berjalan lancar, dan seluruh pengujian dengan  Selenium berhasil.

  * **Minggu 5 (Tugas 5)**
  * **Target:** Memahami fungsi JavaScript pada front-end development, menggunakan JavaScript secara dasar, dan menerapkan AJAX dan Fetch API dengan aman.
  * **Implementasi:** Menerapkan AJAX menggunakan Fetch API untuk memuat data *Project* dan *Experience* secara asinkron tanpa me-*reload* halaman, mengganti perulangan template Django dengan perakitan elemen DOM via JavaScript, serta menyertakan mekanisme perlindungan XSS dan keamanan CSRF pada permintaan.
  * **Hasil:** seluruh fitur interaktif AJAX berfungsi lancar dengan notifikasi (*toast*) keberhasilan atau kegagalan yang tepat sasaran.

## Tugas 1

1. Saya menggunakan elemen semantik HTML5 pada web portoffolio saya, yaitu elemen <section>, <header>, dan <footer>. Elemen ini membantu saya dalam menyusun kerangka static web saya sehingga struktur dokumen saya dapat tersusun dengan lebih terorganisir dan readable. Elemen semantik HTML5 ini juga memudahkan saya dalam melakukan styling pada CSS.

2. Tantangan utama saya adalah menyusun layout desktop berbasis grid dua kolom dimana foto profil berada di sebelah kanan teks identitas dan bio menjadi bertumpuk secara vertikal dan berposisi di tengah(center). Selain itu, mengubah navigasi yang awalnya horizontal menjadi menu dropdown garis tiga(hamburger) juga lumayan menantang bagi saya. Saya mengevaluasieleman mana yang harus diubah posisinya dengan berpikir apa yang harus dilihat oleh user pertama kali saat membuka web portofolio saya. Saya meyakini bahwa nama/identitas harus berada di posisi teratas, diikuti foto, dan terakhir bio/penjelasan. saya meyakini bahwa urutan seperti ini adalah urutan yang seimbang. Kemudian untuk ukuran, pada layar desktop ukuran nama dibuat sangat besar karena layar desktop yang luas. Saat berpindah ke layar mobile, saya mengurangi ukurannya dan memastikan teks diatur menjadi rata tengah agar tidak terpotong saat layar menjadi sempit.

3. Website yang saya buat saat ini adalah static web murni, sehingga batasan utama yang saya rasakan adalah setiap konten didalamnya yang harus saya tulis ulang ketika saya ingin menambah atau mengubah sesuatu. Misalnya jika saya ingin menambah pengalaman saya, maka  saya harus menulis lagi di HTML atau mengubah hal tertentu lagi di CSS. Selain itu, fitur email yang disajikan saat ini bukan mengirim secara langsung, tetapi meminta browser untuk membuka Gmail di device user. Oleh karena itu, fungsionalitas dinamis yang ingin saya tambahkan adalah fitur untuk menambah/mengedit pengalaman dan foto saya tanpa harus membuka kode dan form yang dapat langsung mengirim pesan ke email saya atau tersimpan di database


## Penggunaan AI

Saya menggunakan bantuan AI(Gemini) dalam mengerjakan tugas ini. Saya menggunakan AI untuk:

- Merancang hamburger menu interaktif menggunakan checkbox
- Menambahkan efek gradasi warna bergerak(animated gradient) pada latar belakang foto profil
- Memahami fungsi horizontal scrolling pada section Experience menggunakan properti CSS seperti `overflow-x` `scroll-snap`, dan kustomisasi tampilan scrollbar dengan `::-webkit-scrollbar` agar kartu pengalamannya dapat bergeser dan estetik.

### Strategi Prompting & Contoh Chatlog
- **strategi Prompting:**
    1. Menjelaskan struktur HTML yang sudah ada agar solusi CSS yang diberikan tidak merusak tata letak lainnya.
    2. Memberikan batasan seperti *"cukup gunakan CSS tanpa JavaScript"*
- **Contoh ChatLog:**
    >**User:** "kalo layarnya mengecil navbarnya kepotong gini ya, gimana caranya biar ga kepotong ya? bisa pake menu hamburger ga"
    > **AI:** "Navbar kepotong saat layar mengecil karena menu navigasi dibungkus dengan lebar tetap. Kita bisa mengimplementasikan pure CSS hamburger menu menggunakan teknik `<input type="checkbox" id="nav-toggle">` dan pseudoclass `:checked` pada media query `@media (max-width: 768px)`..."

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

Saya menggunakan bantuan AI(Gemini) dalam mengerjakan tugas 2 ini. Saya menggunakan AI untuk:

- Membantu merancang struktur model `Project` serta menangani penambahan field baru
- Menyusun skenario pengujian pada `test.py`
- memahami alur request response Django dan membedah konsep dasar untuk menjawab pertanyaan reflektif no 1 pada tugas 2

### Strategi Prompting & Contoh Chatlog
- **strategi Prompting:**
    1. Menginstruksikan AI berperan sebagai pengajar Django untuk menjelaskan alur MVC/MVT langkah demi langkah dari URL ke View hingga Template.
    2. Meminta AI untuk menyusun skenario untuk pengujian di `test.py`
    3. Meminta rekomendasi AI terkait penentuan fields yang dibutuhkan pada model `Project` dan panduan implementasinya di Django.
- **Contoh Chatlog:**

  > **User:** "Aku mau bikin fitur portofolio proyek di Django. kira-kira model Project butuh field apa saja ya? Terus gimana cara hubungin ke models.py?"
  >
  > **AI:** "Untuk entitas portofolio proyek, kamu bisa menggunakan struktur field berikut di `main/models.py`:
  > ```python
  > from django.db import models
  > 
  > class Project(models.Model):
  >     title = models.CharField(max_length=200)
  >     description = models.TextField()
  >     tech_stack = models.CharField(max_length=255)
  >     link = models.URLField(blank=True, null=True)
  >     thumbnail = models.URLField(blank=True, null=True)
  > ```
  > Setelah mendefinisikan modelnya, buat berkas migrasi dan terapkan ke database SQLite dengan perintah:
  > ```bash
  > python manage.py makemigrations
  > python manage.py migrate
  > ```"

  > **User:** "Gimana cara bikin unit test di `tests.py`? Aku  mau pastiin semua code yang udah aku bikin bener semua."
  >
  > **AI:** "Gunakan kelas `TestCase` bawaan Django:
  > ```python
  > from django.test import TestCase, Client
  > from django.urls import reverse
  > from main.models import Project
  > 
  > class ProjectTest(TestCase):
  >     def setUp(self):
  >         self.client = Client()
  >         self.project = Project.objects.create(
  >             title='Web Portfolio',
  >             description='Proyek portofolio Django',
  >             tech_stack='Django, HTML, CSS'
  >         )
  > 
  >     def test_project_page_status_and_template(self):
  >         response = self.client.get(reverse('main:show_projects'))
  >         self.assertEqual(response.status_code, 200)
  >         self.assertTemplateUsed(response, 'project.html')
  > ```"

  > **User:** "Jelaskan step-by-step dengan bahasa yang sederhana gimana request pengguna dari browser diproses hingga menampilkan halaman template pada Django."
  >
  > **AI:** "Alurnya melalui siklus Request-Response MVT: Browser Request -> urls.py (URL Dispatcher) -> views.py (Handler Logic) -> models.py (Query Database ORM) -> Template Rendering (DTL) -> HTTP Response kembali ke browser."
    

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

Saya menggunakan bantuan AI(Gemini) dalam mengerjakan tugas 3 ini. Saya menggunakan AI untuk:

Prompting:
- memberikan potongan kode
- memperbaiki bug yang ada di dalam CSS
- membantu dalam membuat `tests.py`

Keterbatasan AI:
- Menganggap atribut yang tidak ada menjadi ada
- Karena yang ditanyakan hanyapotongan kode, AI memberikan banyak solusi yang tidak sesuai dengan codenya, hal ini menyebabkan test gagal

perbaikan yang saya lakukan:
- memperbaiki typo yang ada pada pada code
- tidak menyalin, tetapi memahami apa maksud AI dan menyesuaikannya pada code.

### Strategi Prompting & Contoh Chatlog
- **Strategi Prompting:**
    1. mengirim pesan eror dari terminal ketika terjadi error
    2. Meminta AI untuk menyusun skenario untuk pengujian di `test.py`
- **Contoh Chatlog:**
  > **User:** "pas aku edit malah kaya gini: Forbidden (403) CSRF verification failed. Reason given for failure: Origin checking failed - https://... does not match any trusted origins."
  >
  > **AI:** "Error tersebut terjadi karena Django memverifikasi domain pengirim POST request. Pada platform PWS dengan protokol HTTPS, kamu perlu mendaftarkan domain tersebut ke `CSRF_TRUSTED_ORIGINS` di dalam `settings.py`..."
  >
  > **User:** "aku pake gambar di drive btw, kenapa broken image?"
  >
  > **AI:** "Link Google Drive format web preview diblokir oleh browser untuk hotlinking tag `<img>`. Ubah URL dari format `/file/d/FILE_ID/view` menjadi direct link `https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000`."


## Tugas 4

Saya menggunakan bantuan AI (ChatGPT) dalam mengerjakan Tugas 4 ini untuk:

- **Memberikan gambaran:** Membantu memahami dan menyusun logika untuk fitur otorisasi
- **Membantu implementasi fitur `Star`:** membantu memahami implementasi fitur Star secara interaktif
- **Membantu menyusun CSS** membantu proses styling halaman.
Tautan Log Percakapan AI:[https://chatgpt.com/share/6ab9f920-6ed0-83ec-ba61-8a8e67886f24]


## Tugas 5

1. **Debouncing** adalah teknik untuk menunda sebuah fungsi hingga suatu jeda waktu berlalu tanpa event baru. Selama pengguna masih mengetik, timer sebelumnya dibatalkan dan dimulai lagi. Jadi, browser hanya mengirim permintaan setelah pengguna berhenti mengetik selama sejenak. Pada fitur pencarian, teknik ini penting karena mencegah browser mengirimkan permintaan ke server secara beruntun setiap ketikan. Teknik ini jugaa membuat permintaan pada fitur pencarian hanya akan dikirim ketika pengguna berhenti mengetik sehingga dapat mengurangi beban server, menghemat *bandwidth*, dan mencegah terjadinya bentrokan respons di mana data hasil pencarian dari ketikan awal datang terlambat dan menimpa hasil dari ketikan baru.

2. Penggunaan `await` bersama dengan `fetch()` berfungsi untuk menjeda eksekusi baris kode JavaScript selanjutnya hingga proses pengambilan data asinkron dari server (berupa *Promise*) selesai diproses dan mengembalikan hasilnya. Jika kita tidak menggunakan `await`, maka kode JavaScript di bawahnya akan langsung dieksekusi tanpa menunggu proses `fetch()` selesai. Akibatnya, variabel penampung hasil `fetch()` tersebut yang hanya berisi objek *Promise* yang berstatus *pending* (menunggu), sehingga data tidak bisa ditampilkan atau akan menyebabkan *error* saat diproses lebih lanjut.

3. **Cross-Site Scripting (XSS)** adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain. Salah satu jenisnya adalah stored XSS, yaitu ketika kode berbahaya disimpan ke database (misalnya sebagai judul proyek) lalu ikut dijalankan setiap kali data tersebut ditampilkan. Data yang dimuat melalui AJAX/JavaScript lebih rentan terhadap serangan ini karena pengembang sering kali menyisipkan data JSON mentah langsung ke dalam *DOM* menggunakan properti seperti `innerHTML`. Jika pengembang lupa membuat fungsi *escaping* manual di JavaScript, skrip berbahaya tersebut akan langsung dieksekusi oleh browser. Sebaliknya, *template* bawaan Django jauh lebih aman karena memiliki fitur *auto-escaping* aktif yang otomatis menetralisir semua karakter HTML berbahaya sebelum halaman dikirim ke pengguna.

## Penggunaan AI

Saya menggunakan bantuan AI (ChatGPT) dalam mengerjakan Tugas 5 ini untuk:

- **Membantu implementasi fitur Edit (AJAX):** Membantu merancang "Modal Recycling" sehingga modal yang dipakai untuk menambah data (Create) bisa dipakai juga untuk mengubah data (Update), tanpa perlu memuat ulang halaman (*reload*).
- **Memberikan gambaran dan *debugging*:** membantu menyesuaikan format tanggal menjadi `YYYY-MM-DD` menggunakan metode `.substring(0, 10)` agar kalender pada form modal Edit terisi otomatis, kemudian membantu mengatasi tombol edit yang tidak dapat berfungsi
- **Memahami konsep teoretis:** Membantu membedah konsep dasar *debouncing*, *asynchronous programming* (`await`), dan keamanan XSS untuk menjawab pertanyaan reflektif.

Tautan Log Percakapan AI: 
[https://chatgpt.com/share/6ac1e34a-6c00-83ec-a295-97f5cecfb9de] 
[https://chatgpt.com/share/6ac1e359-5970-83ec-bc6c-79243f63d713]

### Strategi Prompting & Contoh Chatlog
- **Strategi Prompting:**
  1. Memberikan potongan kode HTML dan `views.py` yang sudah ada, lalu menginstruksikan AI untuk menyesuaikan fitur Edit agar berjalan menggunakan metode AJAX yang sama persis dengan fitur Create.

### Keterbatasan AI & Perbaikan Manual
Meskipun AI sangat membantu, ada beberapa keterbatasan yang saya temukan selama pengerjaan:
- **Keterbatasan AI (Kurang Konteks):** AI terkadang memberikan solusi yang kurang tepat karena tidak bisa melihat keseluruhan file proyek saya.
- **Perbaikan Manual:** Saya tidak menyalin kode AI mentah-mentah. Saya menelusuri sendiri apa yang salah dan mengubahnya. Selain itu, saya mengerjakan tugas ini dengan melihat tutorial 5 dan juga mencari referensi tambahan dari internet seperti W3Schools dan GeeksforGeeks untuk membantu saya memperbaiki *bug* dan memahami kode dengan lebih baik secara mandiri.


