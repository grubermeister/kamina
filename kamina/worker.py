#!/usr/bin/env python
from threading import Thread

import secretary
from desk import Desk


class Worker(Thread):
    def __init__(self, debug=False, desk=None):
        super().__init__()
        
        _desk = desk or Desk(True)
        self.inbox = _desk.inbox
        self.outbox = _desk.outbox
        self.result = None
        
    def run(self):
        msg = self.inbox.get()
        
        if msg:
            self.result = True
            print("This came down from my Manager -" + str(msg))
        
        return self.result or False



