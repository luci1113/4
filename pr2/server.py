import Pyro4

@Pyro4.expose
class StringConcatenator(object):
    def concatenate_strings(self, str1, str2):
        return str1 + str2

def main():
    daemon = Pyro4.Daemon() #Daemon object (daemon) which will listen for incoming requests.
    uri = daemon.register(StringConcatenator) #Registers an instance of StringConcatenator with the daemon, obtaining a URI that clients can use to connect to this instance.
    
    print("Server URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
