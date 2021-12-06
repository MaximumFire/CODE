Module Module1

    Sub Main()
        Console.WriteLine("How long would you like the line to be?")
        Dim lineLength As Integer = Console.ReadLine()
        For i = 1 To lineLength
            Console.Write("-")
        Next
        Console.ReadKey()
    End Sub

End Module
