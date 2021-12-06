Module Module1

    Sub Main()
        While True
            Console.WriteLine("Enter the current colour.")
            Dim currentColour As Char = Console.ReadLine()
            If currentColour = "g" Then
                Console.WriteLine("a")
            ElseIf currentColour = "a" Then
                Console.WriteLine("r")
            ElseIf currentColour = "r" Then
                Console.WriteLine("ra")
            ElseIf currentColour = "ra" Then
                Console.WriteLine("g")
            End If
        End While
    End Sub

End Module
