Module Module1

    Sub Main()
        Console.WriteLine("Height?")
        Dim height As Integer = Console.ReadLine()

        Console.WriteLine("Length?")
        Dim length As Integer = Console.ReadLine()

        For i = 1 To height
            For j = 1 To length
                Console.Write("#")
            Next
            Console.WriteLine("")
        Next

        Console.ReadKey()
    End Sub

End Module
