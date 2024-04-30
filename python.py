from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/choose_pet')
def choose_pet():
    return render_template('choose_pet.html')


@app.route("/give_pet")
def give_pet():
    return render_template("give_pet.html")


@app.route("/contacts_author")
def contacts_author():
    return render_template("contacts_author.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')