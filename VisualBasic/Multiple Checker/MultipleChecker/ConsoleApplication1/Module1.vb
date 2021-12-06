Module Module1
    Public result As Boolean = False
    Public input1 As Integer
    Sub Main()
        Console.WriteLine("Enter a number to see if it is a multiple of 3")
        input1 = Console.Read()
        If (input1 Mod 3) = 0 Then
            Console.WriteLine("That is a multiple of 3")
        Else
            Console.WriteLine("That is not a multiple of 3")
        End If
        Console.ReadKey()
    End Sub

End Module
