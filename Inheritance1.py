public class Animal 
{
    public void Eat() => Console.WriteLine("Eating...");
}

// Dog IS-A Animal
public class Dog : Animal 
{
    public void Bark() => Console.WriteLine("Barking...");
}
