from multiprocessing import Queue as ProcessQ
from queue import Queue as ThreadQ

class Desk:
    def __init__(self, is_thread):
        if is_thread:
            self.inbox = ThreadQ()
            self.outbox = ThreadQ()
        else:
            self.inbox = ProcessQ()
            self.outbox = ProcessQ()
