Module Module1

    Function SumValues(a As Integer, b As Integer) As Integer
        Dim result As Integer
        result = a + b
        Return result
    End Function

    Function IsBigger(num1 As Integer, num2 As Integer) As Boolean
        If num1 > num2 Then
            Return True
        Else
            Return False
        End If
    End Function

    Function IsNegative(num As Integer) As Boolean
        If 0 > num Then
            Return True
        Else
            Return False
        End If
    End Function

    Function IsDivisableBy2(num As Integer) As Boolean
        If (num Mod 2) = 0 Then
            Return True
        Else
            Return False
        End If
    End Function

    Sub Main()
        Dim answer As Boolean
        Console.WriteLine("Enter the number (integer)")
        Dim firstNum As Integer = Console.ReadLine()
        answer = IsDivisableBy2(firstNum)
        If answer Then
            Console.WriteLine("number is divisable by 2")
        Else
            Console.WriteLine("number is not divisable by 2")
        End If
        Console.ReadKey()
    End Sub


End Module
