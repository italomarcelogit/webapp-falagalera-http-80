from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hn = socket.gethostname()
    page = f"""
    <h1>Fala Galera!</h1>
    <h3>Website no ar.</h3>
    <h5>{hn} - {socket.gethostbyname(hn)}</h5>
    """
    return page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
