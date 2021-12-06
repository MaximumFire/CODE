Module Module1
    Dim Books(3, 2) As String

    Sub Main()
        InputBooks()
        Console.Clear()
        OutputBooks()

        Console.ReadKey()
    End Sub

    Sub InputBooks()
        For i = 0 To Books.GetUpperBound(0) - 1
            Console.WriteLine("Enter the name for Book " & i + 1)
            Books(i, 0) = Console.ReadLine()
            Console.WriteLine("Enter the author for Book " & i + 1)
            Books(i, 1) = Console.ReadLine()
        Next
    End Sub

    Sub OutputBooks()
        Console.WriteLine("Book    Author")
        For i = 0 To Books.GetUpperBound(0) - 1
            Console.WriteLine(Books(i, 0) & vbTab & Books(i, 1))
        Next
    End Sub

End Module
