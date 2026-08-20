# Frontend Stack

## Runtime

- Node.js : 25.8.2 (Termux)
- npm : 11.12.1

> Disarankan menggunakan Node.js 22 LTS jika di PC.

---

## Framework

| Package | Version |
|---------|----------|
| vue | 3.5.20 |
| vite | 5.4.19 |
| vue-router | 4.5.1 |
| pinia | 2.3.1 |
| axios | 1.11.0 |

---

## Styling

| Package | Version |
|---------|----------|
| tailwindcss | 3.4.19 |
| postcss | 8.5.25 |
| autoprefixer | 10.5.4 |

> Menggunakan Tailwind CSS v3 karena kompatibel dengan Android/Termux.
> Tailwind CSS v4 tidak digunakan karena dependency `lightningcss`
> bermasalah pada Android ARM.

---

## Development

| Package | Version |
|---------|----------|
| @vitejs/plugin-vue | 5.2.4 |
| eslint | 9.34.0 |
| eslint-plugin-vue | 9.33.0 |
| vue-eslint-parser | 9.4.3 |
| prettier | 3.6.2 |
| @eslint/js | 9.34.0 |
| eslint-config-prettier | 10.1.8 |
| globals | 16.3.0 |

---

## Install

```bash
npm install
```

---

## Run

```bash
npm run dev
```

---

## Notes

- Vue 3
- Vite 5
- Tailwind CSS v3
- Tidak menggunakan TypeScript
- Tidak menggunakan Tailwind v4
- Kompatibel dengan Termux Android ARM