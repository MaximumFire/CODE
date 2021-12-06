Module Module1

    Sub Main()
        Const numColours As Integer = 3
        Dim favColours(numColours) As String

        Console.Write("Enter your first favourite colour: ")
        favColours(0) = Console.ReadLine()
        Console.Write("Enter your second favourite colour: ")
        favColours(1) = Console.ReadLine()
        Console.Write("Enter your third favourite colour: ")
        favColours(2) = Console.ReadLine()

        Console.WriteLine("Your second favourite colour is: " & favColours(1))

        Console.ReadKey()
    End Sub

End Module
