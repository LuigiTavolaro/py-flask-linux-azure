from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('form.html')


@app.route('/inserir',methods = ['POST'])
def enviar():
    if request.method == 'POST':
        nome = request.form['Name']
        email = request.form['Email']
        return 'Nome: {} <br> email: {}'.format(nome, email)


if __name__ == '__main__':
    app.run(debug=True)

    