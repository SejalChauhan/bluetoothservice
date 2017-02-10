from twisted.web.static import File
from klein import Klein
import bluetooth
import json

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

@app.route('/scan',branch=True)
def pg_scan(request):
    devices_nearby=bluetooth.discover_devices(lookup_names=True)
    request.setHeader('Content-Type', 'application/json')
    return json.dumps(devices_nearby)
    #return File('./')

app.run("0.0.0.0", 24180)

