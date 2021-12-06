Module Module1

    Sub Main()
        Dim score As Integer

        While True
            Console.WriteLine("Enter your test score as a percentage (0-100).")
            score = Console.ReadLine()

            If Not (-1 < score < 101) Then
                Console.WriteLine("Value not 0-100")
                Exit While
            End If
            If score > 96 Then
                Console.WriteLine("Grade A*")
            ElseIf score > 94 Then
                Console.WriteLine("Grade A+")
            ElseIf score > 92 Then
                Console.WriteLine("Grade A")
            ElseIf score > 89 Then
                Console.WriteLine("Grade A-")
            ElseIf score > 85 Then
                Console.WriteLine("Grade B+")
            ElseIf score > 82 Then
                Console.WriteLine("Grade B")
            ElseIf score > 79 Then
                Console.WriteLine("Grade B-")
            ElseIf score > 75 Then
                Console.WriteLine("Grade C+")
            ElseIf score > 72 Then
                Console.WriteLine("Grade C")
            ElseIf score > 69 Then
                Console.WriteLine("Grade C-")
            Else
                Console.WriteLine("Grade U")
            End If
            Console.ReadKey()
        End While
    End Sub

End Module
