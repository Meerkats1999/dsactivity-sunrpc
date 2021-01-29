import rpyc
connect = rpyc.connect("localhost",1025)
a=0
print("Enter a number any number below 0 will shutdown the client\n")
while(True):
    a=int(input())
    x=connect.root.even(a)
    print("Connection established to server on port(unassigned): 1025\n")
    if x==-1:
        print("Connection terminated from server on port(unassigned): 1025\n")
        exit()
    print(x)