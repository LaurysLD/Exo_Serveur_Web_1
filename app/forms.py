from dataclasses import dataclass


@dataclass
class ItemData:
    title: str
    details: str


@dataclass
class AuthData:
    username: str
    password: str


def parse_item(form_data):
    title = (form_data.get("title") or "").strip()
    details = (form_data.get("details") or "").strip()

    errors = {}
    if not title:
        errors["title"] = "Le titre est requis."
    if not details:
        errors["details"] = "La description est requise."

    if errors:
        return None, errors

    return ItemData(title=title, details=details), {}


def parse_auth(form_data):
    username = (form_data.get("username") or "").strip()
    password = (form_data.get("password") or "").strip()

    errors = {}
    if not username:
        errors["username"] = "L'identifiant est requis."
    if not password:
        errors["password"] = "Le mot de passe est requis."

    if errors:
        return None, errors

    return AuthData(username=username, password=password), {}
