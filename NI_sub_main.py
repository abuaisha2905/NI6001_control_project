
import NI_main as ni
wave1 = ni.NI('ai1')
def fun1():
    wave1.read()


def fun2():
    wave1.graph()





t1 = ni.threading.Thread(target=fun1)
t2 = ni.threading.Thread(target=fun2)

t1.start()
t2.start()
t1.join()
t2.join()


