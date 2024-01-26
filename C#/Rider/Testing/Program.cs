using System;
using Testing.classes;

namespace Testing
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            PQueue queue = new PQueue();
            queue.Enqueue(1);
            queue.Enqueue(2);
            queue.Enqueue(3);
            queue.Enqueue(4);
            queue.Enqueue(5);
            
            Console.WriteLine(queue.Dequeue());

            queue.Print();
        }
    }
}