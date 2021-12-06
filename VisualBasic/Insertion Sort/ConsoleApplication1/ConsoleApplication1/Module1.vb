Module Module1

    Dim arr(9) As Integer
    Dim rng As New Random
    Sub Sort()
        For s = 1 To arr.Length() - 1
            Dim quay As Integer = arr(s)
            Dim j As Integer = s - 1

            While j >= 0 And quay < arr(j)
                arr(j + 1) = arr(j)
                j = j - 1
                If j = -1 Then
                    Exit While
                End If
            End While

            arr(j + 1) = quay
        Next
    End Sub

    Sub printArr()
        Dim result As String = "["
        For i = 0 To arr.GetUpperBound(0)
            result = result + arr(i).ToString() + ", "
        Next
        result = result & "]"
        Console.WriteLine(result)
    End Sub

    Sub Main()
        For i = 1 To arr.Length()
            arr(i - 1) = rng.Next(0, 1000)
        Next

        printArr()

        Sort()

        printArr()

        Console.ReadKey()
    End Sub

End Module
