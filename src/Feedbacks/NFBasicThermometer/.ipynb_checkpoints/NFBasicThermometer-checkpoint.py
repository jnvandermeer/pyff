import random
import sys
import math
import random
import os
import time


# in * is also: from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
# visual, sound, core, data, event and logging are the crucial ones.
import pygame
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging # I guess this is the best way?

# we use the Dirty Programming Method (*) to import all of psychopy's utlilities and tricks
from FeedbackBase.PsychopyFeedback import PsychopyFeedback
# we need this additional line - this is how we import psychopy -- why we need to write this multiple times?
# "The downside of having to write a couple import statements per module does not outweigh the potential problems introduced by trying to get around writing them." (PEP20).


class NFBasicThermometer(PsychopyFeedback):
    
    # constants to be used throughout the DEFs.
    # TRIGGER VALUES FOR THE PARALLEL PORT (MARKERS)
    START_EXP, END_EXP = 252, 253
    COUNTDOWN_START = 0
    START_TRIAL_ANIMATION = 36

    # anything you write in INIT, in terms of variables, will/can be sent and changed...
    def init(self):
        PsychopyFeedback.init(self)
        self.caption="Neurofeedback Thermometer"
        self.color=[0, 0, 0]
        self.fontheight=200
        #logFile = logging.LogFile('LastRun'+'.log', level=logging.EXP, filemode='w')
        #logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
        #centralLog = logging.LogFile("C:\\psychopyExps.log", level=logging.WARNING, filemode='a')

        
    # this is called BEFORE the main experiment (i.e. before 'play')
    def pre_mainloop(self):
        
        PsychopyFeedback.pre_mainloop(self)
        
        # so.. now you should have self.win, which is the window -- draw stuff on that, etc.
        # THIS ... is where we could 'draw' all kinds of stuff onto the window.
        # we COULD also, define a 'text output' window placed somewhere else, right?
        msg=visual.TextStim(self.win, text="Hallo!!")
        
        polygon = visual.Rect(win=self.win, name='polygon', width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],\
                              ori=0, pos=(0.5, 0.5),\
                              lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',\
                              fillColor=[1,1,1], fillColorSpace='rgb',\
                              opacity=1, depth=0.0, interpolate=True)
        
        polygon.draw()
        msg.draw()
        self.win.flip()
        
        # i want it to stop here so I can debug?
        import pdb
        pdb.set_trace()

    # this is called AFTER main loop...
    def post_mainloop(self):
        PsychopyFeedback.post_mainloop(self)

    #this always gets called, even paused.. -- UNTIL self.on_stop() is called. this will exit the main loop.
    # a 'tick' == ONE passage through the main loop (which is a 'while True' loop, basically...)
    def tick(self):
        core.wait(3)
        
        core.wait(3)
        
        self.on_stop()

    # this gets called ONLY -- while on play mode
    def play_tick(self):
        pass
    
    # this gets called ONLY -- while on pause mode
    def pause_tick(self):
        pass
    
    # one could define several other tick methods for different kinds of behaviours.
    
    
    # this function WILL get called whenever I send over a 'control' event -- which is..
    # f.e. the NF data (whatever variable it is!)
    def on_control_event(self, data):
        #self.logger.debug("on_control_event: %s" % str(data))
        self.f = data["data"][ - 1]

        
    # this function WILL get called whenever I do anything like 'play','pause','quit', etc.
    # and this ALSO can contain some data (for example some init data...)
    #def on_interaction_event(self, data):
    #    print(data)
    #    pass
    
    

