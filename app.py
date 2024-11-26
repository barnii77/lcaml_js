from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)


@app.route("/lcaml_py_repo/<path:path>")
def lcaml_py_repo_file(path):
    return send_from_directory("lcaml_py_repo", path)


@app.route("/docs/<path:path>")
def docs_file(path):
    return send_from_directory("docs", path)


@app.route("/lcaml_main.py")
def lcaml_main_py_file():
    return send_file("lcaml_main.py")


@app.route("/wcaml.py")
def wcaml_py_file():
    return send_file("wcaml.py")


@app.route("/lcaml.js")
def lcaml_js_file():
    return send_file("lcaml.js")


@app.route("/wcaml_utils.lml")
def wcaml_utils_lml_file():
    return send_file("wcaml_utils.lml")


@app.route("/")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run()
