from twisted.web.static import File
from klein import Klein

app = Klein()

@app.route('/', branch=True)
def pg_root(request):
    return File('./')
    #d = treq.get()

@app.route('/user/<username>')
def pg_user(request, username):
    return 'Hi %s, here is a list of all the bluetooth devices around you' % (username,)

@app.route('/<string:arg>')
def pg_string(request, arg):
    return '%s devices:' % (arg,)

@app.route('/scan')
def pg_scan(request):
    return 'Scanning...'

app.run("0.0.0.0", 24180)
