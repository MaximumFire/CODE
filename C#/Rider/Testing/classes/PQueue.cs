using System;

namespace Testing.classes
{
    public class PQueue
    {
        public Node Front { get; set; }
        public Node Rear { get; set; }
        
        public PQueue()
        {
            Front = null;
            Rear = null;
        }
        
        public void Enqueue(int value)
        {
            Node node = new Node(value);
            if (Front == null)
            {
                Front = node;
                Rear = node;
            }
            else
            {
                Rear.Next = node;
                Rear = node;
            }
        }
        
        public int Dequeue()
        {
            if (Front == null)
            {
                return -1;
            }
            else
            {
                Node temp = Front;
                Front = Front.Next;
                temp.Next = null;
                return temp.Value;
            }
        }
        
        public int Peek()
        {
            if (Front == null)
            {
                return -1;
            }
            else
            {
                return Front.Value;
            }
        }
        
        public bool IsEmpty()
        {
            if (Front == null)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        
        public void Print()
        {
            Node current = Front;
            while (current != null)
            {
                Console.Write($"{current.Value} -> ");
                current = current.Next;
            }
            Console.WriteLine("NULL");
        }
    }
}