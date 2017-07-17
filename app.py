import json
#import os

import gevent

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

from flask import copy_current_request_context

app = Flask(__name__)

@app.route('/')

@copy_current_request_context
def webhook():
    print("Request: ")
    #json.loads(url.read().decode()) possibly
    #with open ('test.json') as json_data:
        #req=json.load(json_data)
        #print (req)
    req = request.get_json()
    print("Request Success")
    processRequest(req)
    #print(json.dumps(req, indent=4))

    #res = json.dumps(res, indent=4)
    #r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'

    gevent.spawn(webhook)

    return req

#https://www.mbusa.com/mercedes/vehicles/build/class-C/model-C300WB
#https://www.mbusa.com/mercedes/vehicles/build/class-C/model-C300V

def processRequest(req):
    #if req.get("result").get("action") != "getUrl"
        #return {"speech": "Did not function",
                #"displayText": "Did not function"}
    print("processRequest")
    #data = json.loads(result)
    res = makeWebhookResult(req)
    return res

def makeWebhookResult(req):
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
    postmodel="WB"
    classUrl = Class_Url(oUrl,className)
    res = Model_Url(classUrl,premodel,className,model,postmodel)
    fin = "Here is your URL " + res
    print(fin)
    #Makes URL into a JSON file which API.AI can read
    return {
        "speech": res,
        "displayText": res,
    }


def Class_Url(oUrl, className):
    classUrl="%s%s" %(oUrl, className)
    return classUrl
def Model_Url(classUrl,premodel,className,model,postmodel):
    modelUrl="%s%s%s%s%s" %(classUrl,premodel,className,model,postmodel)
    return modelUrl

if __name__ == "__main__":
    print("main")
    #app.run()
    webhook()
    #app.run(debug=True)
    #port = int(os.getenv('PORT',5000))
    #print("Starting app on port %d" % port)
    #app.run()#debug=True, host '0.0.0.0')
