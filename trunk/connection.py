import sqlobject
from sqlobject.mysql import builder
conn = builder()(user='pedrinho', passwd='segredo',
                 host='localhost', db='pedrinho')

