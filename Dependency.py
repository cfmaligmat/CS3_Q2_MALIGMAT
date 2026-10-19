public class FormatUtility 
{
    public string CleanText(string input) => input.Trim();
}

public class ReportGenerator 
{
    // ReportGenerator does NOT store FormatUtility as a field.
    // It only depends on it temporarily inside this method.
    public void GenerateReport(FormatUtility utility, string rawData)
    {
        string processedData = utility.CleanText(rawData);
        Console.WriteLine($"Report: {processedData}");
    }
}
