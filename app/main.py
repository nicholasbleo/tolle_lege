from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/aeneid/aeneid-1.html')

@app.route('/<book>/<passage>')
def get_passage(book, passage):
    template_path = f'/{book}/{passage}'
    return render_template(template_path)