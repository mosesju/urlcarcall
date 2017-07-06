import json
import os

def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    data = json.loads(result)
    res = makeWebhookResult
    return res

def makeWebhookResult(data):
    queryClass()
    queryModel()
    oUrl = "https://www.mbusa.com/mercedes/vehicles/build/class-"
    premodel="/model-"
    postmodel="V"
    classUrl = Class_Url(oUrl,className)
    modelUrl = Model_Url(classUrl,premodel,className,model,postmodel)
    print (modelUrl)
    return{
        "text": text,
        "displayText": text,
        "source": "api.ai car call"
    }


def queryClass(req):
    result = req.get("result")
    parameters = result.get("parameters")
    className = parameters.get("Class")
    className = className.upper()
    return className

def queryModel(req):
    result = req.get("result")
    parameters = result.get("parameters")
    model = parameters.get("Model")
    return model

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
    webhook()
