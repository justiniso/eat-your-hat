import mypackage.foo

def dobar():
    print 'bar'


def dofoobar1():
    mypackage.foo.dofoo()
    dobar()