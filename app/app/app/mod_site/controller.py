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
    # print "user logged in with user id: "
    # print login_session['user_id']
    distance = read_readings("1")
    print "distance is" + distance
    return render_template('private/dashboard.html', distance=distance)

@mod.route('/dbtest')
def dbtest():
    rlist = read_readings("1")
    print "rlist returned is: "
    print rlist
    return rlist
