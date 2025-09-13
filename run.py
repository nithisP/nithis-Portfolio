from app import create_app

app = create_app()

if __name__ == '__main__':
    # Development only; in production Render uses gunicorn via Procfile
    app.run(debug=True)
