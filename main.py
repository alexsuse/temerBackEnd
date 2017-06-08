"""Is Temer still president of Brazil?

Simple Flask app that returns a text response stating
if Michel Temer is still president of Brazil.
"""
from flask import Flask
import president_fetcher

app = Flask(__name__)

@app.route('/')
def isTemerPresident():
    """Returns if Michel Temer is president of Brazil"""
    president = president_fetcher.getEnWikiPresident()
    if "Michel" not in president and "Temer" not in president:
        return "No!"
    return 'Yes :('


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
