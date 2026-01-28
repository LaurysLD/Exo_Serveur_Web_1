from functools import wraps

from flask import Blueprint, redirect, render_template, request, session, url_for

from .forms import parse_auth, parse_item

bp = Blueprint("main", __name__)

_users = {}
_items = []
_next_id = 1


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("main.login"))
        return view(*args, **kwargs)

    return wrapped


@bp.get("/")
def home():
    return render_template("home.html", user=session.get("user"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    errors = {}
    if request.method == "POST":
        auth, errors = parse_auth(request.form)
        if auth:
            if auth.username in _users:
                errors["username"] = "Cet identifiant existe déjà."
            else:
                _users[auth.username] = auth.password
                session["user"] = auth.username
                return redirect(url_for("main.items"))

    return render_template("register.html", errors=errors)


@bp.route("/login", methods=["GET", "POST"])
def login():
    errors = {}
    if request.method == "POST":
        auth, errors = parse_auth(request.form)
        if auth:
            stored = _users.get(auth.username)
            if stored is None or stored != auth.password:
                errors["global"] = "Identifiant ou mot de passe incorrect."
            else:
                session["user"] = auth.username
                return redirect(url_for("main.items"))

    return render_template("login.html", errors=errors)


@bp.post("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.home"))


@bp.route("/items", methods=["GET", "POST"])
@login_required
def items():
    global _next_id
    errors = {}
    if request.method == "POST":
        item, errors = parse_item(request.form)
        if item:
            _items.append(
                {
                    "id": _next_id,
                    "title": item.title,
                    "details": item.details,
                }
            )
            _next_id += 1
            return redirect(url_for("main.items"))

    return render_template(
        "items.html",
        items=_items,
        errors=errors,
        user=session.get("user"),
    )


@bp.route("/items/<int:item_id>/edit", methods=["GET", "POST"])
@login_required
def edit_item(item_id):
    item = next((it for it in _items if it["id"] == item_id), None)
    if item is None:
        return redirect(url_for("main.items"))

    errors = {}
    if request.method == "POST":
        new_data, errors = parse_item(request.form)
        if new_data:
            item["title"] = new_data.title
            item["details"] = new_data.details
            return redirect(url_for("main.items"))

    return render_template("edit_item.html", item=item, errors=errors)


@bp.post("/items/<int:item_id>/delete")
@login_required
def delete_item(item_id):
    index = next((i for i, it in enumerate(_items) if it["id"] == item_id), None)
    if index is not None:
        _items.pop(index)
    return redirect(url_for("main.items"))
