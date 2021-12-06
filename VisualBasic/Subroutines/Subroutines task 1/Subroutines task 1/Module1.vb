Module Module1

    Sub Main()

        WriteTimesTables()

        Console.ReadKey()
    End Sub

    Sub WriteTimesTables()
        Dim currentCell As String
        Dim col As Integer = 0
        Dim row As Integer = 0
        For i = 1 To 12
            col = 0
            For j = 1 To 12
                If i = j Then
                    Console.ForegroundColor = ConsoleColor.Green
                End If

                If row = 0 Or col = 0 Then
                    Console.ForegroundColor = ConsoleColor.Red
                End If
                currentCell = (i * j)
                While currentCell.Length <> 3
                    currentCell = "0" & currentCell
                End While

                Console.Write(" " & currentCell & " ")
                col = col + 1
                Console.ForegroundColor = ConsoleColor.White
            Next
            Console.WriteLine("")
            row = row + 1
        Next
    End Sub

End Module
