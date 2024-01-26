namespace Testing.classes
{
    public class Node
    {
        public Node Next { get; set; }
        public int Value { get; set; }
        
        public Node(int value)
        {
            Value = value;
            Next = null;
        }
    }
}