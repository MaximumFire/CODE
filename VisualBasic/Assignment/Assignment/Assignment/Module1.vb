Module Module1

    Structure student
        Dim name As String
        Dim year As Integer
        Dim ATL As Decimal
    End Structure

    Sub Main()
        Dim classTenXOne(30) As student
        For i = 1 To 30
            classTenXOne(i).name = i & ": Connor"
            classTenXOne(i).year = i
            classTenXOne(i).ATL = 10.1001836
        Next
        For i = 0 To classTenXOne.Length - 1
            Console.WriteLine(classTenXOne(i).name & classTenXOne(i).year & classTenXOne(i).ATL)
        Next
        Console.ReadKey()
    End Sub

End Module
