from sqlobject import *
from connection import conn

class Queue(SQLObject):
    _connection = conn
    name = StringCol(length=128, unique=True, alternateID=True)
    musiconhold = StringCol(length=128, default='default')
    monitor_join = BoolCol(default=True)
    monitor_format = StringCol(length=128, default='gsm')
    context = StringCol(length=128, default='context')
    strategy = StringCol(length=128, default='ringall')
Queue.createTable(ifNotExists=True)

class Agent(SQLObject):
    _connection = conn
    queue_name = StringCol(length=128)
    interface = StringCol(length=128)
    penalty = IntCol()
Agent.createTable(ifNotExists=True)

class AgentAction(SQLObject):
    _connection = conn
    queue_id = IntCol()
    agent_id = IntCol()
    action = StringCol(length=128)
    info1 = StringCol(length=128)
    info2 = StringCol(length=128)
    info3 = StringCol(length=128)
    time_stamp = IntCol()
AgentAction.createTable(ifNotExists=True)
    
class SipUser(SQLObject):
    _connection = conn
    name = StringCol(length=80, notNone=True, unique=True)
    username = StringCol(length=80, notNone=True)
    context = StringCol(length=80, default='default')
    callgroup = StringCol(length=10)
    callerid = StringCol(length=80)
    host = StringCol(length=31, default='dynamic')
    ipaddr = StringCol(length=31, default='')
    port = StringCol(length=5, default='')
    mailbox = StringCol(length=50)
    pickupgroup = StringCol(length=10)
    secret = StringCol(length=80)
    allow = StringCol(length=100, default='g729;ilbc;gsm;ulaw;alaw')
    type = StringCol(length=7, default='friend')
    qualify = StringCol(length=3, default='yes')
    regseconds = IntCol(default=0)
SipUser.createTable(ifNotExists=True)
  
class IAXUser(SQLObject):
    _connection = conn
    name = StringCol(length=80, notNone=True, unique=True)
    username = StringCol(length=80, notNone=True)
    context = StringCol(length=80, default='default')
    callgroup = StringCol(length=10)
    callerid = StringCol(length=80)
    host = StringCol(length=31, default='dynamic')
    mailbox = StringCol(length=50)
    pickupgroup = StringCol(length=10)
    secret = StringCol(length=80)
    allow = StringCol(length=100, default='g729;ilbc;gsm;ulaw;alaw')
    type = StringCol(length=7, default='friend')
    qualify = StringCol(length=3, default='yes')
IAXUser.createTable(ifNotExists=True)

class Attendant(SQLObject):
    _connection = conn
    name = StringCol(length=80, notNone=True, unique=True)
    username = StringCol(length=80, notNone=True)
    context = StringCol(length=80, default='default')
    callgroup = StringCol(length=10)
    callerid = StringCol(length=80)
    mailbox = StringCol(length=50)
    secret = StringCol(length=80)
    sipId = ForeignKey('SipUser')
    iaxId = ForeignKey('IAXUser')
    agentId = ForeignKey('Agent')
Attendant.createTable(ifNotExists=True)
