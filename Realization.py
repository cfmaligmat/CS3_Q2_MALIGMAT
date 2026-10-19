public interface IVehicle 
{
    void StartEngine();
}

// Car realizes (implements) the IVehicle contract
public class Car : IVehicle 
{
    public void StartEngine() => Console.WriteLine("Engine started.");
}
