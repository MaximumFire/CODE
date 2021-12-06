using System;
using System.Collections.Generic;
using System.Linq;

namespace Happy_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number to check if it is happy or not:");
            string userNumber = Console.ReadLine();
            List<int> nums = new List<int>();
            int counter = 0;
            for(int i = 0; i < userNumber.Length; i++)
            {
                nums.Add(userNumber[i]);
            }
            while(1==1)
            {
                int tempSquare = 0;
                int total = 0;
                List<char> tempList = new List<char>();
                counter++;
                for(int j = 0; j < nums.Count; j++)
                {
                    int tempNumber = Convert.ToInt32(nums[j]);
                    tempSquare = tempNumber * tempNumber;
                    total = total + tempSquare;
                }
                string tempString = total.ToString();
                for(int x = 0; x < tempString.Length; x++)
                {
                    tempList.Add(tempString[x]);
                }
                
            }
        }
    }
}
