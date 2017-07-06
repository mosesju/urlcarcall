
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

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
    
"""

def makeWebhookResultForGetJoke(data):
    valueString = data.get('value')
    joke = valueString.get('joke')
    speechText = joke
    displayText = joke
    return {
        "speech": speechText,
        "displayText": displayText,
        # "data": data,
        # "contextOut": [],
        "source": "Call Car"
    }

"""
def Class_Url(oUrl, className):
    classUrl="%s%s" %(oUrl, className)
    return classUrl
def Model_Url(classUrl,premodel,className,model,postmodel):
    modelUrl="%s%s%s%s%s" %(classUrl,premodel,className,model,postmodel)
    return modelUrl

if __name__ == "__main__":
    webhook()
    queryClass()
    queryModel()
    oUrl = "https://www.mbusa.com/mercedes/vehicles/build/class-"
    premodel="/model-"
    postmodel="V"
    classUrl = Class_Url(oUrl,className)
    modelUrl = Model_Url(classUrl,premodel,className,model,postmodel)
    print (modelUrl)
