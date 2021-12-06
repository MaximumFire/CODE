Module Module1
    ' This is a global constant
    Const PI As Decimal = 3.1415926535897931
    Sub Main()
        ' This is a local variable
        Dim IsRunning As Boolean = True
        While IsRunning = True
            Console.Write("Do you want area (1) or circumference (2)? : ")
            ' Local Variable
            Dim userChoice As String = Console.ReadLine()
            If userChoice = 1 Then
                Console.Write("Please enter radius : ")
                ' Local Variable
                Dim radius As Decimal = Console.ReadLine()
                Console.WriteLine("The area for a circle with radius : " & radius & " would be : " & GetArea(radius))
            ElseIf userChoice = 2 Then
                Console.Write("Please enter radius : ")
                ' Local Variable
                Dim radius As Decimal = Console.ReadLine()
                Console.WriteLine("The circumferencefor a circle with radius : " & radius & " would be : " & GetCircumference(radius))
            End If
            Console.Write("Do you want to calculate another? (y/n) : ")
            ' Local Variable
            userChoice = Console.ReadLine()
            If userChoice.ToLower() = "n" Then
                ' Local Variable
                IsRunning = False
            End If
        End While

    End Sub

    Function GetArea(radius As Decimal) As Decimal
        ' Uses the global constant - PI to calculate the answer with the parameter provided.
        Return (PI * radius * radius)
    End Function

    Function GetCircumference(radius As Decimal) As Decimal
        ' Uses the global constant - PI to calculate the answer with the parameter provided.
        Return (PI * 2 * radius)
    End Function
End Module
