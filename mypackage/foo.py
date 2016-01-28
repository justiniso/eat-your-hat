import mypackage.bar


def dofoo():
    print 'foo'


def dofoobar2():
    dofoo()
    mypackage.bar.dobar()