Module Module1
    Public input1 As Integer
    Sub Main()
        Console.WriteLine("Enter a time (eg 12 for 12 o clock)")
        input1 = Console.ReadLine()
        If input1 = 12 Then
            Console.WriteLine("That time is: " & input1 & "PM")
        ElseIf input1 = 24 Then
            input1 = input1 - 12
            Console.WriteLine("That time is: " & input1 & "AM")
        ElseIf input1 > 12 Then
            input1 = input1 - 12
            Console.WriteLine("That time is: " & input1 & "PM")
        Else
            Console.WriteLine("That time is: " & input1 & "AM")
        End If
        Console.ReadKey()
    End Sub

End Module
