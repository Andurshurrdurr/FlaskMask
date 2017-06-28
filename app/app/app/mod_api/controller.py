"""Controller for the api/ endpoint, test with api/getstuff"""

from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getstuff')
def getstuff():
    return '{"result" : "You are accessing the api"}'


@mod.route('/device/<int:device_id>/data')
@mod.route('/registry/<int:reg_id>/data/<int:device_id>')
def getjsondata(device_id=False, reg_id=False):
    print "got json request!"
    if device_id == False:
        jsonfied = listmenujson(reg_id)
        return jsonfied
    else:
        jsonfied = getitemjson(reg_id, device_id)
        return jsonfied
