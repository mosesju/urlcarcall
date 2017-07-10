from __future__ import print_function
#from future.standard_library import install_aliases

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Request: ")
    #json.loads(url.read().decode()) possibly
    req = request.get_json(silent=True, force=False)
    print("Request Success")
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    #if req.get("result").get("action") != "getUrl"
        #return {"speech": "Did not function"}

    data = json.loads(result)
    res = makeWebhookResult(data)
    return res

def makeWebhookResult(data):
    #gets class
    result = req.get("result")
    parameters = result.get("parameters")
    className = parameters.get("Class")
    className = className.upper()

    #gets model
    result = req.get("result")
    parameters = result.get("parameters")
    model = parameters.get("Model")

    #Formats URL
    oUrl = "https://www.mbusa.com/mercedes/vehicles/build/class-"
    premodel="/model-"
    postmodel="V"
    classUrl = Class_Url(oUrl,className)
    res = Model_Url(classUrl,premodel,className,model,postmodel)
    fin = "Here is your URL " + res
    #Makes URL into a JSON file which API.AI can read
    return {
        "speech": res,
        "displayTest": res,
    }


def Class_Url(oUrl, className):
    classUrl="%s%s" %(oUrl, className)
    return classUrl
def Model_Url(classUrl,premodel,className,model,postmodel):
    modelUrl="%s%s%s%s%s" %(classUrl,premodel,className,model,postmodel)
    return modelUrl

if __name__ == "__main__":

    print("main")
    webhook()
    #app.run(debug=True)
    #port = int(os.getenv('PORT',5000))
    #print("Starting app on port %d" % port)
    #app.run()#debug=True, host '0.0.0.0')
