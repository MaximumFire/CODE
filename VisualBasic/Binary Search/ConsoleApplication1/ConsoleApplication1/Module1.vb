Module Module1

    Sub Main()
        Dim array(10) As Integer
        For i = 1 To 10
            array(i - 1) = i
        Next

        Dim find As Integer = 100
        Dim Found As Boolean = False
        Dim start As Integer = 0
        Dim finish As Integer = array.Length()

        While Found = False
            Dim mid As Integer = (start + finish) / 2

            If array.GetLowerBound(0) < mid > array.GetUpperBound(0) Then
                Found = False
                Exit While
            End If

            If array(mid) = find Then
                Console.WriteLine("Found at " & mid.ToString())
                Found = True
            Else
                If array(mid) > find Then
                    finish = mid - 1
                Else
                    start = mid + 1
                End If
            End If
        End While

        If Found = False Then
            Console.WriteLine("Not found")
        End If

        Console.ReadKey()
    End Sub

End Module
