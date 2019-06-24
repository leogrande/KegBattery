# Main python file to run KegBattery

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def init_page(name=None):
    return render_template('main_page.html', name=name)


# Web page will be available at http://localhost:5000/
if __name__ == "__main__":
    app.run()
