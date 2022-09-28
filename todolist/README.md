Kathleen Daniella Wijaya | 2106637366 

# TUGAS 4 PBP

Link menuju aplikasi Heroku yang sudah dideploy: https://tugasduapebepe.herokuapp.com/todolist/

# {% csrf_token %}
Cross-Site Request Forgery (CSRF) attacks merupakan suatu serangan pada aplikasi web dimana request/permintaan yang tidak diinginkan oleh user dijalankan. Maka dari itu, potongan kode {% csrf_token %} pada elemen < form > bertujuan untuk menghindari serangan tersebut dengan men-generate suatu token yang bersifat rahasia dan unik lalu memasukkannya ke dalam HTTP request user sehingga server dapat menentukan jika authorized user yang membuat request atau bukan. By default, token tersebut akan dicek oleh views.py yang menangani path yang diinginkan. Jika valid, maka permintaan akan diproses. Jika tidak valid atau tidak terdapat token, maka permintaan tidak akan diproses. Dengan begitu, jika tidak terdapat potongan kode {% csrf_token %} pada elemen < form >, maka kemungkinan terjadinya CSRF attack akan lebih besar.

# < form > secara Manual
Kita dapat membuat elemen < form > secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Walaupun server Django dapat secara otomatis menyiapkan dan menata data form agar data tersebut siap untuk di-render, kita dapat melakukan hal ini secara manual yang mengizinkan kita untuk mengurutkan kembali fields. Caranya adalah dengan menggunakan potongan kode {{ form.nama_field }}.
 
# Proses Alur Data dari Submisi hingga Muncul pada HTML
Pertama-tama, user melakukan request. Request tersebut bisa dilakukan dengan berbagai macam cara, salah satunya dengan memasukkan alamat di browser (contoh: http://localhost:8000/path). Berdasarkan contoh tersebut, browser akan men-generate HTTP request ke alamat yang dimasukkan oleh user. Server akan menerima HTTP request tersebut dan mencari views.py yang menghandle path yang diinginkan user. Setelah mendapatkan views.py, server akan men-generate HTML page form dan mengirimkannya sebagai respon ke user melalui tampilan browser. Kemudian, user mengisi form dan submit. Browser akan men-generate HTTP request, metode, dan argumen (semua fields yang diisi oleh user pada form) lalu mengirimkannya ke URL destination (path yang dituliskan pada action form sehingga form yang disubmit akan dikirimkan ke alamat tersebut). Data form dapat dikirim dengan menggunakan beberapa method, seperti get, post, put, patch, delete, dan lain sebagainya. Metode post perlu digunakan untuk menyimpan data pada database server. Server menerima HTTP request berupa form yang sudah diisi oleh user lalu mencari views.py yang menghandle path yang dituliskan pada action form tersebut. Server akan memproses dan mengolah data tergantung pada fungsi di views.py (contoh: jika user ingin melakukan login, maka data akan diproses untuk autentikasi). Setelah itu, hasil pengolahan data akan ditempelkan pada template HTML yang tersedia dan server akan men-generate HTML page sebagai respon ke user melalui tampilan browser.
 
# Implementasi Checklist
- Masuk ke dalam repositori proyek Django Tugas 2 pada VSCode.
- Membuat folder untuk aplikasi baru bernama "todolist".
- Membuat file "apps.py" pada folder "todolist" untuk menyertakan konfigurasi aplikasi untuk aplikasi todolist.
- Membuat file "models.py" pada folder "todolist" yang berisi models untuk aplikasi "todolist". Models ini memiliki atribut user, date, title, dan description. Untuk atribut user, digunakan tipe model models.ForeignKey dengan parameter (User) untuk menandakan many-to-one relationship yang berarti semua user adalah objek dari class User. 
- Membuat file "forms.py" pada folder "todolist". Pada file ini, digunakan class ModelForm untuk membuat class Form dari models.py sehingga fields yang diinginkan pada form dapat diambil dari models.py.
- Masuk ke dalam repositori proyek Django Tugas 2 pada terminal.
- Membuat dan menyalakan virtual environment.
- Menginstal dependencies yang diperlukan untuk menjalankan proyek Django.
- Mempersiapkan migrasi skema model ke dalam database Django lokal dengan perintah "makemigrations" dan menerapkan skema model tersebut dengan perintah "migrate".
- Membuat file "views.py" pada folder "todolist" yang berisi fungsi-fungsi untuk membuat halaman utama, form login, form register, form create task, dan logout. Pada file ini, forms.py diimport agar dapat dilakukan pengambilan data dari form yang sudah diisi oleh user. Lalu, models.py juga diimport agar data form dapat disimpan pada database dan dapat dilakukan pengambilan data dari database. 
- Membuat file "urls.py" pada folder "todolist" untuk mengimplementasikan URL routing halaman utama, form login, form register, form create task, dan logout.
- Membuat folder "templates" yang berisi file "todolist.html" untuk mengatur HTML halaman utama, "form.html" untuk mengatur HTML form create task, "login.html" untuk mengatur HTML form login, dan "register.html" untuk mengatur HTML form register. Pada file "todolist.html", dilakukan iterasi terhadap variabel list_barang yang sudah didefinisikan pada file views.py dan yang sudah ikut di-render ke dalam HTML untuk menampilkan daftar task ke dalam tabel. Selain itu, terdapat juga dua button yang masing-masing mengarah ke form create task dan logout. Pada ketiga file HTML yang mengatur form, terdapat potongan kode {% csrf_token %} untuk memastikan request user. Pada file "form.html" dan "register.html", terdapat {{ form.as_table }} untuk men-generate form.
- Mengimplementasikan URL routing untuk "todolist" pada file "urls.py" yang ada pada folder "tugasduapebepe" (nama aplikasi heroku).
- Menambahkan "todolist" pada file "settings.py" yang ada pada folder "tugasduapebepe", khususnya bagian "INSTALLED_APPS".
- Melakukan add, commit, dan push perubahan yang telah dilakukan ke Github.
- Melakukan deployment ke Heroku terhadap aplikasi Django yang sudah dibuat.

