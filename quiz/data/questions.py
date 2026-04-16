# =========================================
# MATERI 1 - AUTH & SECURITY
# =========================================
# Referensi: Django Auth & Security :contentReference[oaicite:0]{index=0}

materi1 = [
    {
        "id": 1,
        "question": "Apa perbedaan Authentication dan Authorization?",
        "options": [
            "Authentication untuk akses, Authorization untuk login",
            "Authentication identifikasi user, Authorization hak akses",
            "Keduanya sama",
            "Tidak ada jawaban benar"
        ],
        "answer": "Authentication identifikasi user, Authorization hak akses"
    },
    {
        "id": 2,
        "question": "Apa fungsi authenticate()?",
        "options": [
            "Membuat user",
            "Verifikasi kredensial user",
            "Menghapus user",
            "Menyimpan session"
        ],
        "answer": "Verifikasi kredensial user"
    },
    {
        "id": 3,
        "question": "Jika authenticate() gagal, apa hasilnya?",
        "options": ["User object", "False", "None", "Error"],
        "answer": "None"
    },
    {
        "id": 4,
        "question": "Kenapa password tidak disimpan dalam bentuk plain text?",
        "options": [
            "Agar cepat",
            "Agar mudah",
            "Karena di-hash untuk keamanan",
            "Karena tidak support"
        ],
        "answer": "Karena di-hash untuk keamanan"
    },
    {
        "id": 5,
        "question": "Permission default Django adalah?",
        "options": [
            "read, write, execute",
            "view, add, change, delete",
            "create, update",
            "none"
        ],
        "answer": "view, add, change, delete"
    },
]

# =========================================
# MATERI 2 - FORMS & STATIC FILES
# =========================================
# Referensi: Django Forms :contentReference[oaicite:1]{index=1}

materi2 = [
    {
        "id": 1,
        "question": "Apa itu Django Forms?",
        "options": [
            "Database tool",
            "HTML + validasi input",
            "Template engine",
            "Static file"
        ],
        "answer": "HTML + validasi input"
    },
    {
        "id": 2,
        "question": "Fungsi utama Django Forms?",
        "options": [
            "Menampilkan gambar",
            "Memproses input user",
            "Menyimpan file",
            "Menghapus data"
        ],
        "answer": "Memproses input user"
    },
    {
        "id": 3,
        "question": "Class dasar form di Django?",
        "options": [
            "forms.Model",
            "forms.Form",
            "forms.Input",
            "forms.Base"
        ],
        "answer": "forms.Form"
    },
    {
        "id": 4,
        "question": "Apa fungsi csrf_token?",
        "options": [
            "Styling",
            "Keamanan form",
            "Database",
            "Session"
        ],
        "answer": "Keamanan form"
    },
    {
        "id": 5,
        "question": "Static files adalah?",
        "options": [
            "Data user",
            "CSS, JS, gambar",
            "Database",
            "View"
        ],
        "answer": "CSS, JS, gambar"
    },
]

# =========================================
# MATERI 3 - ORM & MIGRATION
# =========================================
# Referensi: Django ORM :contentReference[oaicite:2]{index=2}

materi3 = [
    {
        "id": 1,
        "question": "Apa itu ORM?",
        "options": [
            "Database server",
            "Mapping Python ke database",
            "Frontend tool",
            "CSS"
        ],
        "answer": "Mapping Python ke database"
    },
    {
        "id": 2,
        "question": "ORM menggantikan apa?",
        "options": [
            "HTML",
            "SQL manual",
            "CSS",
            "JS"
        ],
        "answer": "SQL manual"
    },
    {
        "id": 3,
        "question": "Model di Django merepresentasikan?",
        "options": [
            "File",
            "Tabel database",
            "View",
            "Template"
        ],
        "answer": "Tabel database"
    },
    {
        "id": 4,
        "question": "makemigrations digunakan untuk?",
        "options": [
            "Apply database",
            "Membuat migration",
            "Menghapus data",
            "Run server"
        ],
        "answer": "Membuat migration"
    },
    {
        "id": 5,
        "question": "migrate digunakan untuk?",
        "options": [
            "Membuat model",
            "Menerapkan perubahan ke database",
            "Menghapus file",
            "Menjalankan server"
        ],
        "answer": "Menerapkan perubahan ke database"
    },
]

# =========================================
# MAPPING SEMUA MATERI
# =========================================

questions_data = {
    "auth": materi1,
    "forms": materi2,
    "orm": materi3,
}