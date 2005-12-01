from Asterisk.Manager import CoreManager
from Asterisk.Config import Config
import Asterisk.Util

class PedrinhoManager(CoreManager):
    def __init__(self):
        CoreManager.__init__(self, *Config().get_connection())

    
    def on_Event(self, event):
         Asterisk.Util.dump_packet(event)

PDManager = PedrinhoManager()
PDManager.QueueAdd('viaip', 'SIP/pdrucker')
#PDManager.Queues()
#print PDManager.Originate('Zap/35', context='default', extension='30253078', priority=1)
    
