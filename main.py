"""
This file is the main entry of the front end website. It launches a simple search engine at http://localhost:8080
and upong form submission, it displays the frequency of each word in the latest query as well as culmulative
frequency of all keywords since the website is launched.
"""
from bottle import route, run, get, request, static_file, redirect, error, view
import bottle
import operator
import random
import os
import datetime
from math import *
from beaker.middleware import SessionMiddleware
# DEPLOYMENT(TODO): Change this to the following line when deploying to AWS
# from gevent import monkey; monkey.patch_all()

################################################################################
#                       GLOBAL SETTINGS / CONSTANTS
################################################################################
session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

################################################################################
#                      WEBPAGES FROM BOTTLE FRAMEWORK
################################################################################
@route('/img/<filename>')
def image(filename):
    return static_file(filename, root='img/')

@route('/css/<filename>')
def image(filename):
    return static_file(filename, root='css/')

@route('/js/<filename>')
def image(filename):
    return static_file(filename, root='js/')

@route('/add_lunch_choice', method='POST')
def display():
    restaurant = request.forms.get("restaurant")
    print "restaurant is: "+restaurant
    lunch_choices = []
    with open('lunch_choices.txt', 'r') as f:
        for line in f:
            lunch_choices.append(line)
    lunch_choices.append(restaurant)

    with open('lunch_choices.txt', 'w+') as f:
        for c in lunch_choices:
            f.write(c)
    bottle.redirect('/lunch_choice')

@route('/delete_lunch_choice')
def display():
    id = request.query['id']
    print "id is: "+id
    lunch_choices = []
    with open('lunch_choices.txt', 'r') as f:
        for line in f:
            lunch_choices.append(line)
    del lunch_choices[int(id)]

    with open('lunch_choices.txt', 'w+') as f:
        for c in lunch_choices:
            f.write(c)
    bottle.redirect('/lunch_choice')

@route('/lunch_choice_maker')
def display():
    today = datetime.datetime.today()
    today_time_tuple = today.timetuple()
    secrete_num = today_time_tuple.tm_year*366+today_time_tuple.tm_yday
    secrete_file_name = './random_gens/'+str(secrete_num)

    lunch = ''
    # If lunch has already been decided for this day.
    if os.path.isfile(secrete_file_name):
        with open(secrete_file_name, 'r') as f:
            lunch = f.read().strip()
    else:
        lunch_choices = []
        with open('lunch_choices.txt', 'r') as f:
            for line in f:
                if "disable" in line.lower():
                    continue
                lunch_choices.append(line)

        if today.weekday() == 3:
            choice = 0
        else:
            choice = (secrete_num) % (len(lunch_choices)-1)+1
            random_num = random.randint(0,2)
            choice += random_num

        lunch = lunch_choices[choice]
        with open(secrete_file_name, 'w+') as f:
            f.write(lunch)

    return "Quay is going to "+lunch+" for lunch today."

@route('/')
@route('/lunch_choice')
@view('index')
def display():
    lunch_choices = "<table class='table table-striped' style='width:80%; margin:0 auto'>"
    with open('lunch_choices.txt', 'r') as f:
        i = 0
        for line in f:
            lunch_choices += "<tr><td>"+line+"</td>"
            lunch_choices += "<td><a href='delete_lunch_choice?id="+str(i)+"'>Delete</a></td></tr>"
            i+=1
    lunch_choices += "</table>"

    return dict(lunch_options = lunch_choices)

@error(404)
@error(500)
@view('error')
def error_page(error):
    return {}

################################################################################
#                            MAIN FUNCTION
################################################################################
# Start the website on http://0.0.0.0:8080
if __name__ == "__main__":
    # DEPLOYMENT(TODO): Change this to the following line when deploying to AWS
    # run(app=app, host='0.0.0.0', port=8080, server='gevent', debug=True)
    run(app=app, host='0.0.0.0', port=8080, debug=True)
    # run(app=app, host='localhost', port=8080, debug=True)
