Module Module1

    Sub Main()
        Console.WriteLine("Enter number 1")
        Dim numOne As Integer = Console.ReadLine()
        Console.WriteLine("Enter number 2")
        Dim numTwo As Integer = Console.ReadLine()
        Dim result As Integer = Add(numOne, numTwo)
        Console.WriteLine(result)
        Console.ReadKey()
    End Sub

    Function Add(x As Integer, y As Integer)
        Dim res As Integer = x + y
        Return res
    End Function
End Module
