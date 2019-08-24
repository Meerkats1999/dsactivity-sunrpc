import rpyc
class MyService(rpyc.Service):
    def exposed_even(self,a):
        f=open("logs.txt","a")
        print("Connection established to client on port(unassigned): 1025\n")   
        print("The input is: ",a)
        if a>0:
            if a%2:
                f.write('{:00d}\n'.format(a))
                return("Odd")
            else:
                f.write('{:00d}\n'.format(a))
                return("Even")
        else:
            print("Connection terminated from client on port(unassigned): 1025\n")
            return -1
        f.close()
from rpyc.utils.server import ThreadedServer
server = ThreadedServer(MyService, port = 1025)
server.start()