from flask import Blueprint, render_template, url_for

from app.model.model_readings import read_readings

from flask import session as login_session

from . import mod
# Import module models (i.e. User)
# from app.mod_site.models import Users

# # Our sample helperfunction
# from app.mod_site.maths import add
# from app.common.common import sayhello

print "Running site controller.."

@mod.route('/dashboard')
def dashboard():
    print "user logged in with user id: "
    print login_session['user_id']
    temp = read_readings("temp")
    print "temp is" + temp
    pressure = read_readings("pressure")
    humidity = read_readings("humidity")
    co2 = read_readings("co2")
    return render_template('private/dashboard.html', temperature=temp,
                                                     pressure=pressure,
                                                     humidity=humidity,
                                                     co2=co2)

@mod.route('/dbtest')
def dbtest():
    rlist = read_readings("1")
    print "rlist returned is: "
    print rlist
    return rlist
