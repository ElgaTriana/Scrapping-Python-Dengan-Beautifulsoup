import scheduler

def test_1():
    print('test1')

def test_2(name):
    print('test2: ' + name)

def test_3(name, lname):
    print('test3: ' + name + ' ' + lname)

scheduler = Scheduler(60)
scheduler.add('foo', '* * * * *', test_1)
scheduler.add('bar', '0/2 * * * *', test_2, ('mehrdad',))
scheduler.add('bas', '0/3 * * * *', test_3, ('behzad', 'mahmoudi'))
scheduler.add('zoo', '0/4 * * * *', test_3, ('reza', 'mahmoudi'))
scheduler.start()