using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testing
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int money, fifty, twenty, ten, five, one;
            Console.WriteLine("Enter a whole amount of money");
            money = Convert.ToInt32(Console.ReadLine());
            if (money % 50 == 0)
            {
                fifty = money / 50;
                Console.WriteLine($"You have {fifty} fifty pound note(s)");
            }
            else
            {
                if (money % 20 == 0)
                {
                    fifty = money / 50;
                    Console.WriteLine($"You have {fifty} fifty pound note(s)");
                    twenty = money / 20;
                    Console.WriteLine($"You have {twenty} twenty pound note(s)");
                }
                else
                {
                    if (money % 10 == 0)
                    {
                        fifty = money / 50;
                        Console.WriteLine($"You have {fifty} fifty pound note(s)");
                        money = money % 50;
                        twenty = money / 20;
                        Console.WriteLine($"You have {twenty} twenty pound note(s)");
                        money = money % 20;
                        ten = money / 10;
                        Console.WriteLine($"You have {ten} twenty pound note(s)");
                    }
                    else
                    {
                        if (money % 5 == 0)
                        {
                            fifty = money / 50;
                            Console.WriteLine($"You have {fifty} fifty pound note(s)");
                            money = money % 50;
                            twenty = money / 20;
                            Console.WriteLine($"You have {twenty} twenty pound note(s)");
                            money = money % 20;
                            ten = money / 10;
                            Console.WriteLine($"You have {ten} twenty pound note(s)");
                            money = money % 10;
                            five = money / 5;
                            Console.WriteLine($"You have {five} twenty pound note(s)");
                            money = money % 5;
                        }
                        else
                        {
                            if (money % 1 == 0)
                            {
                                fifty = money / 50;
                                Console.WriteLine($"You have {fifty} fifty pound note(s)");
                                money = money % 50;
                                twenty = money / 20;
                                Console.WriteLine($"You have {twenty} twenty pound note(s)");
                                money = money % 20;
                                ten = money / 10;
                                Console.WriteLine($"You have {ten} ten pound note(s)");
                                money = money % 10;
                                five = money / 5;
                                Console.WriteLine($"You have {five} five pound note(s)");
                                money = money % 5;
                                one = money / 1;
                                Console.WriteLine($"You have {one} one pound coin(s)");
                                money = money % 1;

                            }
                        }
                    }

                }
            }
            Console.ReadLine();
        }
    }
}
