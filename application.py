from flask import Flask
from flask_cors import CORS
from ResponseSender import ResponseSender
app = Flask(__name__)

item_list = [1,2,3,4,5,6,7,9,0]

@app.route('/',methods={"GET"})
def hello():
    return ResponseSender("OK","Hello",item_list,200)

@app.errorhandler(FileNotFoundError)
def internal_server_error_handler(error):
    print(error)
    return "Error Handled",500
    
if __name__=="__main__":
    app.run(debug=True,port=8080,host='0.0.0.0')

