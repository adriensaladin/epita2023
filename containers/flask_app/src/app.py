from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a simple Flask demo.'

#reflected xss
@app.route('/search', methods=['GET'])
def search():
    lookupstring = request.args.get("lookupstring", default=None)
    if lookupstring:
        return "Sorry, we could not find " + lookupstring
    else: return "<form>Search for: <input type='text' name='lookupstring'></form>"
    

# "admin" page
@app.route("/admin")
def admin():
    return "Super secret admin page"


if __name__ == '__main__':
    app.run(debug=True)
