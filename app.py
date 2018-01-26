from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            count = data['checked']
            # TODO add to database
            response = {"count": count}
        except:
            response = {"status": 'error'}
        return jsonify(response)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
