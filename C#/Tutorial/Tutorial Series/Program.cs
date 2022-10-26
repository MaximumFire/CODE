using System;

namespace Tutorial_Series
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter value for number: ");
            int number = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter value for line: ");
            string line = Console.ReadLine();
            Console.Clear();
            for (int i = 1; i < number+1; i++)
            {
                Console.WriteLine(line);
            }
        }
    }
}
