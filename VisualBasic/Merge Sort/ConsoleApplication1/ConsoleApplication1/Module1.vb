Module Module1

    Sub Main()

    End Sub

    Function Merge(left() As Integer, right() As Integer) As Integer()
        Dim result_length As Integer = left.Length() + right.Length()
        Dim result(result_length) As Integer

        Dim left_idx As Integer = 0
        Dim right_idx As Integer = 0
        Dim position As Integer = 0

        While left_idx < left.Length() And right_idx < right.Length()
            If left(left_idx) <= right(right_idx) Then
                result(position) = left(left_idx)
                left_idx = left_idx + 1
                position = position + 1
            Else
                result(position) = right(right_idx)
                right_idx = right_idx + 1
                position = position + 1
            End If
        End While

        If left_idx < left.Length() Then

        End If

        Return result
    End Function

End Module
