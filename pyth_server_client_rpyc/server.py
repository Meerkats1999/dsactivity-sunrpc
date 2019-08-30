import rpyc
class MyService(rpyc.Service):
    def exposed_even(self,a):
        f=open("logs.txt","a")
        print("The input is: ",a)
        if a>0:
            if a%2:
                f.write('{:00d}\n'.format(a))
                return("Odd")
            else:
                f.write('{:00d}\n'.format(a))
                return("Even")
        else:
            return -1
        f.close()
from rpyc.utils.server import ThreadedServer
server = ThreadedServer(MyService, port = 1025)
server.start()