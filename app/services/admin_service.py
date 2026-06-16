from app.repositories.admin_repository import get_by_email

def authenticate_admin(db, email, password):
    admin = get_by_email(db, email)
    if not admin:
        return None

    if admin.password_hash != admin.password_hash:
        return None

    return admin