from flask import Flask
import president_fetcher

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    president = president_fetcher.getEnWikiPresident()
    if "Michel" not in president and "Temer" not in president:
        return "No!"
    return 'Yes :('


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
