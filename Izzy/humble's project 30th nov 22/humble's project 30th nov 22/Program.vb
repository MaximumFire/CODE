Imports System
Module Program
    Sub Main(args As String())
        Randomize()
        Dim rng As New Random
        Dim roll1, roll2, p1total, p2total As Integer


        Console.WriteLine("enter player ones name:")
        Dim name1 As String = Console.ReadLine()
        Console.WriteLine("enter player twos name:")
        Dim name2 As String = Console.ReadLine()

        For j = 1 To 5
            For i = 1 To 2
                roll1 = rng.Next(1, 7)
                roll2 = rng.Next(1, 7)
                Console.WriteLine(roll1)
                Console.WriteLine(roll2)

                If i = 1 Then
                    p1total = calculation(roll1, roll2)
                    Console.WriteLine(name1 & " :" & p1total)
                Else
                    p2total = calculation(roll1, roll2)
                    Console.WriteLine(name2 & " :" & p2total)
                End If

            Next
            Console.ReadKey()

        Next

        winner(p1total, p2total, name1, name2)
        If p1total = p2total Then

            For i = 1 To 2
                roll1 = rng.Next(1, 7)
                roll2 = rng.Next(1, 7)
                Console.WriteLine(roll1)
                diceimage(roll1, roll2)
                Console.WriteLine(roll2)
                diceimage(roll1, roll2)

                If i = 1 Then
                    p1total = calculation(roll1, roll2)
                    Console.WriteLine(name1 & " :" & p1total)
                Else
                    p2total = calculation(roll1, roll2)
                    Console.WriteLine(name2 & " :" & p2total)
                End If

            Next
            winner(p1total, p2total, name1, name2)
        End If
        If roll1 = roll2 Then
            Dim extraroll As Integer
            For i = 1 To 1
                extraroll = rng.Next(1, 7)
                Console.WriteLine(extraroll)
                If i = 1 Then
                    If extraroll Mod 2 = 0 Then
                        extraroll = extraroll + 10
                    Else
                        extraroll = extraroll - 5
                    End If
                    If extraroll < 0 Then
                        extraroll = 0
                    End If
                    p1total = p1total + extraroll
                    Console.WriteLine(name1 & " :" & p1total)

                End If

            Next
        End If
    End Sub


    Function calculation(roll1 As Integer, roll2 As Integer) As Integer

        Dim score As Integer = roll1 + roll2
        If score Mod 2 = 0 Then
            score = score + 10
        Else
            score = score - 5
        End If
        If score < 0 Then
            score = 0
        End If

        Return score

    End Function
    Sub winner(p1total As Integer, p2total As Integer, name1 As String, name2 As String)
        If p1total > p2total Then
            Console.WriteLine(name1 & " wins")
        ElseIf p2total > p1total Then
            Console.WriteLine(name2 & " wins")
        ElseIf p1total = p2total Then
            Console.WriteLine("its a draw")

        End If

    End Sub


    Sub diceimage(roll1 As Integer, roll2 As Integer)
        If roll1 = "1" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("|       |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("|       |")
            Console.WriteLine("\-------/")
        ElseIf roll1 = "2" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O     |")
            Console.WriteLine("|       |")
            Console.WriteLine("|     O |")
            Console.WriteLine("\-------/")
        ElseIf roll1 = "3" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O     |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("|     O |")
            Console.WriteLine("\-------/")
        ElseIf roll1 = "4" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("|       |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        ElseIf roll1 = "5" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        ElseIf roll1 = "6" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        End If

        If roll2 = "1" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("|       |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("|       |")
            Console.WriteLine("\-------/")
        ElseIf roll2 = "2" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O     |")
            Console.WriteLine("|       |")
            Console.WriteLine("|     O |")
            Console.WriteLine("\-------/")
        ElseIf roll2 = "3" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O     |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("|     O |")
            Console.WriteLine("\-------/")
        ElseIf roll2 = "4" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("|       |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        ElseIf roll2 = "5" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("|   O   |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        ElseIf roll2 = "6" Then
            Console.WriteLine("/-------\")
            Console.WriteLine("| O   O |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("| O   O |")
            Console.WriteLine("\-------/")
        End If
    End Sub
End Module


