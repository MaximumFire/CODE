using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("No. Iterations: ");
            int iterations = Console.Read();
            int counter = 0;
            int total = 0;
            for (int i = 0; i < iterations; i++)
            {
                Random roll = new Random();
                int rollNumber = roll.Next(1, 7);
                total += rollNumber;
                counter += 1;
            }
            double final = total / counter;
            Console.WriteLine(final);
            Console.ReadKey();
        }
    }
}
