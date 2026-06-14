#WFS SMEs/UMKM
Websites company profile dan content management system (CMS) untuk SMEs/UMKM, dibangun menggunakan FastAPI dan Jinja2

---

## Features
- Admin authentication
- Content management (news, event, promo)
- Gallery management
- Menu management

---

## Tech Stack
- FastAPI
- SQLAlchemy
- Jinja2
- SQLite
- Alembic
- Uvicorn

---

##  Run Locally

```bash
git clone <repo-url>
cd WFS
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---