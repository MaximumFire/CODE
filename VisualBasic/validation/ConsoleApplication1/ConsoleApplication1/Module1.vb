Module Module1

    Sub Main()
        Dim isValid As Boolean = False

        While Not isValid
            Console.Write("Enter your username: ")
            Dim username As String = Console.ReadLine()

            Console.Write("Enter your password: ")
            Dim password As String = Console.ReadLine()

            isValid = ValidateUser(username, password)

            If isValid Then
                Console.WriteLine("Login Success!")
            Else
                Console.WriteLine("Login Failure!")
            End If

        End While

        Console.ReadKey()
    End Sub

    Function ValidateUser(username As String, password As String) As Boolean
        If username = "" Or password = "" Then
            Console.WriteLine("Your password or username was empty. Please enter a username and a password.")
            Return False
        ElseIf username.Length() < 8 Or password.Length() < 8 Then
            Console.WriteLine("Your password or username was less than 8 characters. Enter a username and a password at least 8 characters in length.")
            Return False
        ElseIf ContainsNumber(username) = False Or ContainsNumber(password) = False Then
            Console.WriteLine("Your password or username does not contain a number. Please include numbers.")
            Return False
        End If
        Return True
    End Function

    Function ContainsNumber(value As String) As Boolean
        Dim asciiValue As Integer
        For i = 0 To value.Length - 1
            asciiValue = Asc(value.Substring(i, 1))
            If 48 <= asciiValue And asciiValue <= 57 Then
                Return True
            End If
        Next
        Return False
    End Function

End Module
