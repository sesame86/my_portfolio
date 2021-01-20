from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/movie_recommend')
def movie_recommend():
    return render_template('movie_recommend_page.html')

@app.route('/price_predict')
def price_predict():
    return render_template('price_predict_page.html')

@app.route('/news')
def mews():
    return render_template('news_page.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)