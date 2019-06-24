# Main python file to run KegBattery

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "The KegBattery web application!"


# Web page will be available at http://localhost:5000/
if __name__ == "__main__":
    app.run()
