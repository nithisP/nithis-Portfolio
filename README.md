# Portfolio (Flask Version)

This project migrates a static personal portfolio site into a Flask application structure to enable future dynamic features (forms, database, etc.).

## Structure
```
portfolio/
  app/
    __init__.py
    routes.py
    templates/
      base.html
      index.html
      home.html
      education.html
    static/
      css/style.css
      js/script.js
  run.py
  requirements.txt
```

## Quick Start (Windows PowerShell)
1. Create & activate virtual environment:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run development server:
```
python run.py
```
4. Open: http://127.0.0.1:5000

## Deploying to Render
1. Push this repository to GitHub.
2. Create a new Web Service on Render, connect the repo.
3. Environment: Python.
4. Build Command (auto from `render.yaml`): `pip install -r requirements.txt`
5. Start Command: `gunicorn wsgi:app --workers=3 --timeout=60` (also defined in `Procfile`).
6. Ensure `requirements.txt` includes `gunicorn`.

### Why wsgi:app?
`wsgi.py` exposes an `app` object created by the factory in `app/__init__.py`. Gunicorn imports it using the pattern `MODULE:VARIABLE`.

### Environment Variables
Add (optional) in Render dashboard:
```
SECRET_KEY=change_me
FLASK_ENV=production
```

### Common Deployment Issues
- Error `Failed to find attribute 'app' in 'app'`: start command pointed to the wrong module. Use `wsgi:app`.
- 502 after deploy: check logs for import errors; verify that all template/static paths are correct.

### Updating
Push to your main branch; Render auto deploys (autoDeploy: true in `render.yaml`).

## Adding Pages
- Create a new template in `app/templates/` and add a route in `routes.py`.
- Use `{% extends 'base.html' %}` and define blocks: `title`, `extra_head`, `body`, `scripts`.

## Static Assets
Use `url_for('static', filename='css/style.css')` or `js/script.js`. Place images under `app/static/img/` (create folder if needed):
```
<img src="{{ url_for('static', filename='img/myphoto.jpg') }}" alt="Me">
```

## Environment Variables
For production set a secure secret key:
```
$env:FLASK_SECRET_KEY = "change_me"
```
Then modify `create_app` to read from environment if desired.

## Next Enhancements
- Fully migrate all original inline styles into `style.css`.
- Add contact form with email or database logging.
- Add Projects data via a Python list/dict passed to template.
- Create separate Blueprint for API (if needed in future).
- Add tests (pytest + Flask testing client).

## License
Personal project. All rights reserved unless otherwise stated.
