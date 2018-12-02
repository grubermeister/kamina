#!/usr/bin/env python
import secretary
from desk import Desk
from worker import Worker


class Manager:
    def __init__(self, debug=False, desk=None):
        self.staff = []
        #self.office = [Desk(True)]
        _desk = desk or Desk(False)
        self.inbox = _desk.inbox
        self.outbox = _desk.outbox
        self.result = None
        
    def join(self):
        for w in self.staff:  w.join()
        
        return self.result or False
        
    def run(self):
        worker = Worker(debug=True)      
        self.staff.append(worker)
        for w in self.staff:  w.start()
        
        msg = self.inbox.get()
        print("This passed my desk - " + str(msg))
        worker.inbox.put(msg)
        
        return self.join()
