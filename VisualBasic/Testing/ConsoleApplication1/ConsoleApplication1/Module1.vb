Module Module1
    Public num As Integer
    Public result As Integer
    Sub Main()
        Console.WriteLine("Enter a number: ")
        num = Console.ReadLine()
        Console.WriteLine("Do you want to square or cube the number? (square/cube): ")
        Dim choice As String
        choice = Console.ReadLine()
        If choice = "square" Then
            Square()
        Else
            Cube()
        End If
        Console.WriteLine("The result was: " & result)
        Console.ReadKey()
    End Sub
    Sub Square()
        result = num * num
    End Sub
    Sub Cube()
        result = num * num * num
    End Sub
End Module
