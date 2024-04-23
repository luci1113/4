from xmlrpc.server import SimpleXMLRPCServer #XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact

#Remote Procedure Call (RPC) is a powerful technique for constructing distributed, client-server based applications.
#RPC is kind of similar to REST (REpresentational State Transfer). In RPC, the method is found in the URL itself and the client submits calls that use arguments/parameters to use these methods.
'''ADVANTAGES :

1.RPC provides ABSTRACTION i.e message-passing nature of network communication is hidden from the user.
2.With RPC code re-writing / re-developing effort is minimized. '''
server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)
server.register_function(factorial, "factorial_rpc")
try:
    print("Starting and listening on port 8000...")
    print("Press Ctrl + C to exit.")
    server.serve_forever()
except:
    print("Exit.")

