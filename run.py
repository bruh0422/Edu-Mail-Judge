from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        mail = request.form.get('mail')
        mail_rool, mail_domain = mail.split('@')

        return f'''
        <script>
        alert('{mail} {"非" if "edu" not in mail_domain else ""}隸屬於教育機構');
        window.location.href = '/';
        </script>
        '''

@app.route('/github')
def github():
    return redirect('https://github.com/')

@app.route('/sign')
def sign():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == '__main__':
    app.run(debug=True)