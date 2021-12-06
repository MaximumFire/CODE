Module Module1

    Sub Main()
        Dim randomGen As New Random()
        Dim randomNumber As Integer
        randomNumber = randomGen.Next(1, 3)
        If randomNumber = 1 Then
            Console.WriteLine("Heads")
        ElseIf randomNumber = 2 Then
            Console.WriteLine("Tails")
        End If
        Console.ReadKey()
    End Sub

End Module
