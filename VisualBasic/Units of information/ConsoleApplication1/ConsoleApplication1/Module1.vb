Module Module1
    Sub Main()
        While True
            Console.WriteLine("1. Dispaly Binary")
            Console.WriteLine("2. Display Hexadecimal")

            Console.Write("Select option: ")
            Dim choice As String = Console.ReadLine()

            If choice = "1" Then ' Binary
                Console.Write("Enter a denary digit: ")
                Dim digit As Integer = Console.ReadLine()
                Console.WriteLine(GetBinary(digit))

            ElseIf choice = "2" Then ' Hexadecimal
                Console.Write("Enter a denary digit: ")
                Dim digit As Integer = Console.ReadLine()
                Console.WriteLine(GetHex(digit))
            End If
        End While
        Console.ReadKey()
    End Sub

    Function GetHex(digit As Integer) As String
        Dim binary As String = GetBinary(digit)
        Dim nib1 As String = binary.Substring(0, 4)
        Dim nib2 As String = binary.Substring(3, 4)
        Console.WriteLine(nib1)
        Console.WriteLine(nib2)
        Dim answer As String = ""
        Dim denary As Integer = 0
        Dim denary2 As Integer = 0

        If (nib1.Substring(0, 1) = "1") Then
            denary = denary + 8
        ElseIf (nib1.Substring(1, 1) = "1") Then
            denary = denary + 4
        ElseIf (nib1.Substring(2, 1) = "1") Then
            denary = denary + 2
        ElseIf (nib1.Substring(3, 1) = "1") Then
            denary = denary + 1
        End If

        If (nib2.Substring(0, 1) = "1") Then
            denary2 = denary2 + 8
        ElseIf (nib2.Substring(1, 1) = "1") Then
            denary2 = denary2 + 4
        ElseIf (nib2.Substring(2, 1) = "1") Then
            denary2 = denary2 + 2
        ElseIf (nib2.Substring(3, 1) = "1") Then
            denary2 = denary2 + 1
        End If

        If denary = 1 Then
            answer = answer & "1"
        End If
        If denary = 2 Then
            answer = answer & "2"
        End If
        If denary = 3 Then
            answer = answer & "3"
        End If
        If denary = 4 Then
            answer = answer & "4"
        End If
        If denary = 5 Then
            answer = answer & "5"
        End If
        If denary = 6 Then
            answer = answer & "6"
        End If
        If denary = 7 Then
            answer = answer & "7"
        End If
        If denary = 8 Then
            answer = answer & "8"
        End If
        If denary = 9 Then
            answer = answer & "A"
        End If
        If denary = 10 Then
            answer = answer & "A"
        End If
        If denary = 11 Then
            answer = answer & "B"
        End If
        If denary = 12 Then
            answer = answer & "C"
        End If
        If denary = 13 Then
            answer = answer & "D"
        End If
        If denary = 14 Then
            answer = answer & "E"
        End If
        If denary = 15 Then
            answer = answer & "F"
        End If

        If denary2 = 1 Then
            answer = answer & "1"
        End If
        If denary2 = 2 Then
            answer = answer & "2"
        End If
        If denary2 = 3 Then
            answer = answer & "3"
        End If
        If denary2 = 4 Then
            answer = answer & "4"
        End If
        If denary2 = 5 Then
            answer = answer & "5"
        End If
        If denary2 = 6 Then
            answer = answer & "6"
        End If
        If denary2 = 7 Then
            answer = answer & "7"
        End If
        If denary2 = 8 Then
            answer = answer & "8"
        End If
        If denary2 = 9 Then
            answer = answer & "A"
        End If
        If denary2 = 10 Then
            answer = answer & "A"
        End If
        If denary2 = 11 Then
            answer = answer & "B"
        End If
        If denary2 = 12 Then
            answer = answer & "C"
        End If
        If denary2 = 13 Then
            answer = answer & "D"
        End If
        If denary2 = 14 Then
            answer = answer & "E"
        End If
        If denary2 = 15 Then
            answer = answer & "F"
        End If

        Return answer
    End Function

    Function GetBinary(digit As Integer) As String
        If digit > 255 Or digit < 0 Then
            Console.WriteLine("Please enter a number between 0 and 255")
            Return "failed"
        End If

        Dim binary As String = ""

        If 0 <= digit <= 255 Then
            While digit <> 0
                If digit >= 128 Then
                    binary = binary & "1"
                    digit = digit - 128
                Else
                    binary = binary & "0"
                End If
                If digit >= 64 Then
                    binary = binary & "1"
                    digit = digit - 64
                Else
                    binary = binary & "0"
                End If
                If digit >= 32 Then
                    binary = binary & "1"
                    digit = digit - 32
                Else
                    binary = binary & "0"
                End If
                If digit >= 16 Then
                    binary = binary & "1"
                    digit = digit - 16
                Else
                    binary = binary & "0"
                End If
                If digit >= 8 Then
                    binary = binary & "1"
                    digit = digit - 8
                Else
                    binary = binary & "0"
                End If
                If digit >= 4 Then
                    binary = binary & "1"
                    digit = digit - 4
                Else
                    binary = binary & "0"
                End If
                If digit >= 2 Then
                    binary = binary & "1"
                    digit = digit - 2
                Else
                    binary = binary & "0"
                End If
                If digit >= 1 Then
                    binary = binary & "1"
                    digit = digit - 1
                Else
                    binary = binary & "0"
                End If
                If digit = 0 Then
                    Exit While
                End If
            End While
            Return binary
        End If
        Return "failed"
    End Function
End Module
