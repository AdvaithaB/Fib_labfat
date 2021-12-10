from flask import redirect, request, render_template, url_for, Flask
from fib import fb

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/result", methods=["POST"])
def result():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    number = fb(int(u_input))
    return render_template("result.html", fib_num = number, usr_input = u_input)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)