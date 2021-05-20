from models.event import Event

event1 = Event("10/20/2020", "Shambahala", "5000", "California", "A big ol' fezza", True)
event2 = Event("05/10/2010", "Big Wave Tour", "100", "Hawaii", "Surf fest bruuuu", False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)