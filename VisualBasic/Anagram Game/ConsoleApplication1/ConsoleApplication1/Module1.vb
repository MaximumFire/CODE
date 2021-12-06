Imports System.Console
Module Module1
    Dim Random As New Random
    Dim Random1, Random2, Length, Numincorrect As Integer
    Dim temp, wordtogeuss, guess As String
    Dim gameover, win As Boolean
    Sub Main()
        WriteLine("Enter a word to guess:")
        wordtogeuss = ReadLine().ToLower
        Length = wordtogeuss.Length
        Dim Letter(Length) As String
        For i = 0 To Length - 1
            Letter(i) = wordtogeuss(i)
        Next
        Clear()
        For i = 1 To 50
            Random1 = Random.Next(1, Length)
            Random2 = Random.Next(1, Length)
            temp = Letter(Random1)
            Letter(Random1) = Letter(Random2)
            Letter(Random2) = temp
        Next
        While gameover = False
            WriteLine()
            For i = 0 To Length - 1
                Write(Letter(i))
            Next
            WriteLine()
            WriteLine()
            WriteLine("Please guess the word:")
            guess = ReadLine().ToLower
            If guess = wordtogeuss Then
                win = True
                gameover = True
            Else
                Numincorrect += 1
                WriteLine("Nunber of guesses left: " & 5 - Numincorrect)
            End If
            If Numincorrect = 5 Then
                gameover = True
                win = False
            End If
        End While
        If win = True Then
            WriteLine("YOU WIN!")
        ElseIf gameover = True Then
            WriteLine("YOU LOSE! The word was " & wordtogeuss)
        End If
        ReadLine()
    End Sub
End Module
