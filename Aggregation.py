public class Wheel 
{
    // A Wheel can exist on its own (e.g., in a warehouse)
}

public class Car 
{
    private List<Wheel> _wheels;

    // The wheels are passed into the Car (Dependency Injection)
    public Car(List<Wheel> wheels) 
    {
        _wheels = wheels; 
    }
}
