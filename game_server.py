import rpyc
player_size=50
enemy_size=50
class MyService(rpyc.Service):
    def exposed_set_level(self,score, SPEED):
	    if score < 20:
		    SPEED = 5
	    elif score < 40:
		    SPEED = 8
	    elif score < 60:
		    SPEED = 12
	    else:
		    SPEED = 15
	    return SPEED
    def exposed_send_score(self,score):
        f=open("scores.txt","a")
        print("Score: " + str(score))
        f.write('{:00d}\n'.format(score))
        f.close
    def exposed_high_score(self):
        with open("scores.txt") as f:
            x=[int(x) for x in f]
        return(max(x))
from rpyc.utils.server import ThreadedServer
server = ThreadedServer(MyService, port = 1025)
server.start()