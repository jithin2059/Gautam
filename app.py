from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_url = None

    if request.method == 'POST':
        n = request.form['text_input']

        if n == n[::-1]:
            result = f'The palindrome of {n} is {True} and word is {n[::-1]}.'
        elif n.lower() == 'gautam':
            result = f'{True} Love and palindrome of {n} is Anisha'
            image_url = url_for('static', filename='images/gautam_image.png')
        else:
            result = f'{False} and palindrome of {n} is {n[::-1]}'

    return render_template('index.html', result=result, image_url=image_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
