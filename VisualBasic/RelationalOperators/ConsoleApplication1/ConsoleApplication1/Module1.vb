Module Module1

    Sub Main()
        Dim favSubject As String
        Dim favTeacher As String
        Dim age As Integer

        favSubject = input(favSubject, "Enter favourite subject.")


    End Sub

    Function input(variable As String, message As String) As String
        Console.WriteLine(message)
        variable = Console.ReadLine()
        Return variable
    End Function

End Module
