from flask import Flask

def export(lib):
    exec("from %s import __file__ as fn" % lib)
    return open(locals()['fn'],"r").read()

app = Flask(__name__)
@app.route("/import/<lib>",methods=['GET'])
def remote_import(lib):
    try:
        return export(lib)
    except Exception as e:
        print(e)
        return "False", 404
app.run(host="127.0.0.1",port=5000)