from os import name
from flask import render_template, request, redirect
from app import app
from models.event import Event
from models.event_list import events, add_new_event, remove_event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/events/new')
def new_event_form():
    return render_template('new_event.html', title='New Event')

@app.route('/events', methods=['POST'])
def add_new_event_from_form():
    event_date = request.form['date']
    event_name = request.form['name']
    no_guests = request.form['no_guests']
    location = request.form['location']
    description = request.form['description']

    
    if 'recurring' in request.form.keys():
        recurring = True
    else: recurring = False

    add_new_event(Event(event_date, event_name, no_guests, location, description, recurring))
    return redirect('/events')


@app.route("/events/delete/<index>")
def delete_event_button(index):
    remove_event(events[int(index)])


    # for event in events:
    #     if event.name == 
  
    return redirect('/events')




    #if request.form['recurring'] == True:

    #     recurring = False
    # else: recurring = True
    
   
    
  