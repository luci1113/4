
import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;

public class AddRemImpl extends UnicastRemoteObject implements AddRem {

    public AddRemImpl() throws  RemoteException{}
    public  int addNum(int a,int b)
    {
System.out.print("Nirmal Roll No:-");
        return(a+b);
    }
}
