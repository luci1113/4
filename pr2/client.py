import Pyro4 #Python remote object use establish the remote connection

def main():
    uri = input("Enter the URI of the server: ")
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    concat_server = Pyro4.Proxy(uri)
    concatenated_str = concat_server.concatenate_strings(str1, str2)
    
    print("Concatenated String:", concatenated_str)

if __name__ == "__main__":
    main()

'''Diiference in RPC(Remote Procedure Call) and RMI(Remote Method Invocation) RPC supports procedural programming.	RMI supports object-oriented programming.
RPC is the older version of RMI.	While it is the successor version of RPC.'''