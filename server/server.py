from flask import flask, jsonify

#app instance
app = flask(__name__)

(app.route("/api/home", methods=['GET']))

def return_home():
    return jsonify[{
        'message': "Hello world!"
    }]
    
if __name__ == '__main__':
    app.run(debug=True)