from classes import *
from SimpleXMLRPCServer import SimpleXMLRPCServer

class Pedrinho:
    
    def __init__(self):
        self.server = SimpleXMLRPCServer(("0.0.0.0", 8086))
        self.server.register_instance(self)
        self.server.serve_forever()
 
    def getQueuesNames(self):
        queues = {}
        all = Queue.select()
	for item in all:
	queues[item.id] = item.name
	return names

    def

    def addQueue(self, name):
        newQ = Queue(name=name)
	return newQ

p = Pedrinho()
