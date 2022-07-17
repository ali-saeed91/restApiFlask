# REST API (GET)
#Request Method:
    # GET                   Endpoint: 127.0.0.1:5000/api/v1/restApi, It returns JSON file Data
# localhost = 127.0.0.1
# Port number: 5000

from flask import Flask, jsonify, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/restApi")
def restApi():
   try:
        # Opening JSON file
        f = open("./output.json", "r")
        
        # returns JSON object as a dictionary
        data = json.load(f)                     # Use sortkey=False for error
        
        # Closing file
        f.close()
        
        return jsonify(data)
    
   except:
       return jsonify({' Error Message': 'Error happened'}), 500
# Main Driver
if __name__ == "__main__":
    app.run()