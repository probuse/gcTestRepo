import web
from . import render

class Hello:
    
    def GET(self):
        "Controls get requests to hello url"
        name = 'Test Site'
        l = locals()
        del l['self']
        return render.hello(**l)

    def POST(self):
        "Controls post requests to hello url"
        result = web.input()
        name = result.myText
        print name
        l = locals()
        del l['self']
        return render.hello(**l) 
