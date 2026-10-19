public class Doctor 
{
    // Doctor knows about their Patients
    public List<Patient> Patients { get; set; } = new List<Patient>();
}

public class Patient 
{
    // Patient knows about their Doctor
    public Doctor PrimaryDoctor { get; set; }
}
