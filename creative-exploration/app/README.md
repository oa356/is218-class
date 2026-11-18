# Campus resource finder

Run from this folder in WSL, Linux or macOS using Python 3.12+. The local SQLite database persists in this folder. Keep the same private key when restarting. The five campus services and locations are fictional.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
# One-time setup
python -c 'from pathlib import Path; import secrets; p=Path(".django-key"); f=p.open("x"); p.chmod(0o600); f.write(secrets.token_urlsafe(48)); f.close()'
# Each new terminal
export DJANGO_SECRET_KEY="$(cat .django-key)"
python manage.py migrate
python manage.py test
python manage.py runserver
```

Open http://127.0.0.1:8000/. Create a throwaway account and sign in. Search for `trasnit`, bookmark Transit Desk, then sign out and sign in again. Look for **Your bookmarks (1)**. A different account should start with an empty list.

[Project record and results](../README.md#review-2--first-working-slice) · [Search strategies](finder/search.py) · [Automated checks](finder/tests.py)
