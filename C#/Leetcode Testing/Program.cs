using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode_Testing
{
    public class MyQueue
    {
        public List<int> data = new List<int>();

        public MyQueue()
        {

        }

        public void Push(int x)
        {
            data.Add(x);
        }

        public int Pop()
        {
            int temp = data[0];
            data.RemoveAt(0);
            return temp;
        }

        public int Peek()
        {
            return data[0];
        }

        public bool Empty()
        {
            if (data.Count == 0)
            {
                return true;
            }
            return false;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            MyQueue queue = new MyQueue();
            queue.Push(1);
            int x = queue.Pop();
            Console.WriteLine(queue.Empty());
            Console.WriteLine(queue.data.Count);
        }
    }
}
