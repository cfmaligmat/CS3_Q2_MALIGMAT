public class Engine 
{
    // Engine lifecycle is strictly bound to the Car
}

public class Car 
{
    private Engine _engine;

    public Car()
    {
        // The Car creates and completely owns the Engine instance
        _engine = new Engine(); 
    }
}
