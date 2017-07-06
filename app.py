import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("result").get("action") != "getUrl"
        return {}

    data = json.loads(result)
    res = makeWebhookResult
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

    oUrl = "https://www.mbusa.com/mercedes/vehicles/build/class-"
    premodel="/model-"
    postmodel="V"
    classUrl = Class_Url(oUrl,className)
    modelUrl = Model_Url(classUrl,premodel,className,model,postmodel)
    print (modelUrl)
    return{
        "speech": modelUrl,
        "displayText": modelUrl,
        "source": "getUrl"
    }


def Class_Url(oUrl, className):
    classUrl="%s%s" %(oUrl, className)
    return classUrl
def Model_Url(classUrl,premodel,className,model,postmodel):
    modelUrl="%s%s%s%s%s" %(classUrl,premodel,className,model,postmodel)
    return modelUrl

if __name__ == "__main__":
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host '0.0.0.0')
