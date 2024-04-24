import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") #A ServerProxy instance is an object that manages communication with a remote XML-RPC server
n=int(input("Enter the number: "))
print("factorial of given number is : %s" % str(proxy.factorial_rpc(n)))
'''RPC supports procedural programming.	RMI supports object-oriented programming.
RPC is the older version of RMI.	While it is the successor version of RPC.
RPC architecture 
client
client strub
RPC runtime
server stub 
server

advantages:-
it helps client to communicate with server 
disadvantage:- 
not flexible for hardware architecture'''


