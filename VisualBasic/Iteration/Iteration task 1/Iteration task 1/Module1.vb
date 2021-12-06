Module Module1

    Sub Main()
        Console.WriteLine("Enter number of rows.")
        Dim rowCount As Integer = Console.ReadLine()

        For i = 1 To rowCount
            Console.WriteLine("*********")
        Next
        Console.ReadKey()
    End Sub

End Module
