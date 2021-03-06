#!/usr/bin/env python

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
	

    def add_state(self, name, handler, end_state=0):    	
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)
	
    def set_start(self, state):
        self.startState = state
	
    def run(self, cargo):
	check = True
	
        try:
            handler = self.handlers[self.startState]	    
        except:
            print "must call .set_start() before .run()"
        if not self.endStates:
            print "at least one state must be an end_state"
	if self.startState == 'e_stop':
	    print "Do Nothing"
	    check = False

        while check:	    
            (newState, cargo) = handler(cargo)
            if newState in self.endStates:
                print"Stop Processing "
                break 
            else:
                handler = self.handlers[newState]   



