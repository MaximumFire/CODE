static double Generate(double iterations)
{
    double k = 1;
    double sum = 0.0;
    for (int i = 0; i < iterations; i++)
    {
        if (i % 2.0 == 0.0)
        {
            sum = sum + (4.0 / k);
        } else
        {
            sum = sum - (4.0 / k);
        }
        k += 2.0;
    }
    return sum;
}

for (double j = 0; j < 10000000000000000000; j = j + 10000000)
{
    Console.WriteLine(Generate(j));
}
