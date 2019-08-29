from flask import Flask, render_template, request, jsonify
from src.model import get_preds


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/commentaire', methods = ['POST', 'GET'])
def display_input_commentaire():
    if request.method == 'POST':
        commentaire = request.form.get('commentaire')
        results = get_preds(commentaire)
        return render_template('commentaire.html', res=results, com = commentaire)
    else:
        results = {}
        return render_template('commentaire.html', res=results)

@app.route('/commentaire_json', methods = ['POST'])
def get_json_commentaire():
    commentaire = request.get_json(force = True) 
    results = {"res" : get_preds(commentaire["commentaire"])}
    return jsonify(results)

        
if __name__ == '__main__':
    app.run(debug=True)