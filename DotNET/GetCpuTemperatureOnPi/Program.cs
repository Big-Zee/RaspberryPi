using System;
using System.Threading;
using Iot.Device.CpuTemperature;
 
using CpuTemperature cpuTemperature = new CpuTemperature();
Console.WriteLine("Press any key to quit");
var counter = 0;

while (!Console.KeyAvailable)
{
    counter++;
    if (cpuTemperature.IsAvailable)
    {
        var temperature = cpuTemperature.ReadTemperatures();
        foreach (var entry in temperature)
        {
            if (!double.IsNaN(entry.Temperature.DegreesCelsius))
            {
                Console.WriteLine(string.Format("{0:#,0.000} °C",entry.Temperature.DegreesCelsius));
                Console.WriteLine($"Temperature from {entry.Sensor.ToString()}: {  entry.Temperature.DegreesCelsius} °C");
                Console.WriteLine("-----");
            }
            else
            {
                Console.WriteLine("Unable to read Temperature.");
            }
        }
    }
    else
    {
        Console.WriteLine($"CPU temperature is not available");
    }

    if (counter >= 5) break;
 
    Thread.Sleep(1000);
}

/*double[] Parse(string s)
{
    var valueStrings = s.Split(new string[] { " ", "°C" }, 
        System.StringSplitOptions.RemoveEmptyEntries);
    return valueStrings.Select(xs => System.Double.Parse(xs)).ToArray();
}*/