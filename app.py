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


@app.route("/readme.md")
def wcaml_utils_lml_file():
    return send_file("README.md")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/E1/index.lml")
def e1_index_lml():
    return 'println "hello world";'


@app.route("/E2/index.html")
def e2_index_lml():
    return '<!DOCTYPE html><html lang="en"><head><title>Testing page</title></head><body><p>Hello world!</p></body></html>'


if __name__ == "__main__":
    app.run()
