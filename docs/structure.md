## Project Structure
WFS/
│
├── app/                  # Folder untuk FastAPI (Python)
│
└── frontend/                 # Folder utama Vue 3 + Vite + Tailwind
    ├── public/               # Aset statis yang tidak diproses oleh Vite (misal: favicon)
    ├── src/                  # Kode sumber utama aplikasi
    │   ├── assets/           # Gambar, logo, dan file CSS global
    │   │   └── main.css      # Tempat konfigurasi awal Tailwind
    │   │
    │   ├── components/       # Komponen UI yang bisa digunakan kembali (Reusable UI)
    │   │   ├── common/       # Komponen global (Button, Input, Modal)
    │   │   └── layout/       # Komponen tata letak (Navbar, Sidebar, Footer)
    │   │
    │   ├── composables/      # Fungsi logika terisolasi (Vue 3 Composition API / Hooks)
    │   │   └── useAuth.js    # Contoh: Logika untuk cek login/logout
    │   │
    │   ├── router/           # Konfigurasi rute halaman (Vue Router)
    │   │   └── index.js
    │   │
    │   ├── services/         # Hubungan langsung ke API (FastAPI)
    │   │   ├── api.js        # Konfigurasi dasar Axios / Fetch (Base URL, Interceptors)
    │   │   └── userService.js # Fungsi hit endpoint (misal: /users, /login)
    │   │
    │   ├── stores/           # State Management (Pinia)
    │   │   └── auth.js       # Menyimpan data user yang sedang login global
    │   │
    │   ├── views/            # Komponen utama per halaman (Page Views)
    │   │   ├── HomeView.vue
    │   │   ├── LoginView.vue
    │   │   └── DashboardView.vue
    │   │
    │   ├── App.vue           # Komponen root / utama Vue
    │   └── main.js           # Entry point aplikasi JavaScript
    │
    ├── index.html            # File HTML utama tempat Vue di-render
    ├── package.json          # Daftar dependensi (package) proyek
    ├── tailwind.config.js    # Konfigurasi custom Tailwind CSS
    ├── postcss.config.js     # Konfigurasi PostCSS untuk Tailwind
    └── vite.config.js        # Konfigurasi utama Vite (build, proxy, dll)
