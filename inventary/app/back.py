import reflex as rx

class State(rx.State):
    count: int = 0

    # Event Handlers
    @rx.event
    def increment(self):
        self.count +=1
    
    @rx.event
    def decrement(self):
        self.count -= 1
    