Imports System

Module Program
    Sub Main(args As String())
        'password checker

        Console.WriteLine("enter your new password:")
        Dim Userpassword As String
        Dim correct As Boolean
        Userpassword = Console.ReadLine()
        Dim UpperCase As Boolean
        Dim LowerCase As Boolean
        Dim specialchar As Boolean
        Dim nums As Boolean

        ' Connor: you made it print out the correct/incorrect messages each time a character was checked, not the whole password
        ' In order to fix this I am going to change the code so that the code only sets each boolean to False if the entire password fails the check, not just the characters.

        If Userpassword.Length - 1 < 8 Then
            correct = False
            Console.WriteLine("invalid password")
        ElseIf Userpassword.Length - 1 >= 8 Then
            correct = True
            Console.WriteLine("valid password length")
        End If

        If correct = True Then
            UpperCase = False
            For i = 0 To Userpassword.Length - 1
                If Asc(Userpassword(i)) >= 65 And Asc(Userpassword(i)) <= 90 Then
                    UpperCase = True
                End If
            Next
        End If

        If correct = True And UpperCase = True Then
            LowerCase = False
            For i = 0 To Userpassword.Length - 1
                If Asc(Userpassword(i)) >= 97 And Asc(Userpassword(i)) <= 122 Then
                    LowerCase = True
                End If
            Next
        End If

        If correct = True And UpperCase = True And LowerCase = True Then
            specialchar = False
            For i = 0 To Userpassword.Length - 1
                If (Asc(Userpassword(i)) >= 33 And Asc(Userpassword(i)) <= 47) Or (Asc(Userpassword(i)) >= 58 And Asc(Userpassword(i)) <= 64) Or (Asc(Userpassword(i)) >= 91 And Asc(Userpassword(i)) <= 96) Or (Asc(Userpassword(i)) >= 123 And Asc(Userpassword(i)) <= 126) Then
                    specialchar = True
                End If
            Next
        End If

        If correct = True And UpperCase = True And LowerCase = True And specialchar = True Then
            nums = False
            For i = 0 To Userpassword.Length - 1
                If Asc(Userpassword(i)) >= 48 And Asc(Userpassword(i)) <= 57 Then
                    nums = True
                End If
            Next
        End If


        If correct = True And UpperCase = True And LowerCase = True And specialchar = True And nums = True Then
            Console.WriteLine("valid password")
            Console.WriteLine("has capitals")
            Console.WriteLine("has lower case")
            Console.WriteLine("has special characters")
            Console.WriteLine("has numbers")

            Console.WriteLine("confirm password....")
            Dim password2 As String = Console.ReadLine()
            If Userpassword = password2 Then
                Console.WriteLine("New password saved")
            Else
                Console.WriteLine("incorrect password, try again later")
            End If
        ElseIf correct = False Then
            Console.WriteLine("Password too short.")
        ElseIf UpperCase = False Then
            Console.WriteLine("Password doesn't contain any uppercase letters.")
        ElseIf LowerCase = False Then
            Console.WriteLine("Password doesn't contain any lowercase letters.")
        ElseIf specialchar = False Then
            Console.WriteLine("Password doesn't contain any special characters.")
        ElseIf nums = False Then
            Console.WriteLine("Password doesn't contain any numbers.")
        End If

    End Sub
End Module