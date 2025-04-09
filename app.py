from Flask import Flask # type: ignore
import time

app = Flask(__name__)

@app.route('/process')
def process():
    time.sleep(1)  # Simulasi beban pemrosesan
    return "Request processed!"

if __name__ == '__main__':
    app.run(debug=True)
