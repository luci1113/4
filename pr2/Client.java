import java.rmi.*;
import java.net.*;
import java.io.*;
import java.util.*;
public class Client {

    public static void main(String[] args) {
        String host="localhost";
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter 1st number: ");
        int a=sc.nextInt();
        System.out.println("Enter 2st number: ");
        int b=sc.nextInt();
        try{
            AddRem remoobj=(AddRem)Naming.lookup("rmi://"+host+"/AddRem");

            System.out.println(remoobj.addNum(a,b));
        }
        catch (RemoteException re)
        {
            re.printStackTrace();
        }
        catch (NotBoundException nbe)
        {
            nbe.printStackTrace();
        }
        catch (MalformedURLException mfe)
        {
            mfe.printStackTrace();
        }
    }
}
