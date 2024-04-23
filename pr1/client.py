import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") #A ServerProxy instance is an object that manages communication with a remote XML-RPC server
n=int(input("Enter the number: "))
print("factorial of given number is : %s" % str(proxy.factorial_rpc(n)))



