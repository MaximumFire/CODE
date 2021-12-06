Module Module1

    Dim questions(1, 5) As String

    Sub Main()

        AddQuestion("Question", "Answer1", "Answer2", "Answer3", "Answer4")

        DisplayArray(questions)

        'AskQuestion(1)

        Console.ReadKey()
    End Sub

    Sub DisplayArray(array(,) As String)

        For i = 1 To array.GetUpperBound(0)
            Console.WriteLine(array(i - 1, 0) & array(i - 1, 1) & array(i - 1, 2) & array(i - 1, 3) & array(i - 1, 4))
        Next

    End Sub

    Function IsAnswerCorrect(answer As String, questionNumber As Integer) As Boolean

        For j = 1 To 4
            If questions(questionNumber, j) = answer Then
                Return True
            End If
        Next

        Return False
    End Function

    Sub AskQuestion(questionNumber As Integer)

        Console.WriteLine(questions(questionNumber, 0))
        Dim answer As String = Console.ReadLine()

        If IsAnswerCorrect(answer, questionNumber) Then
            Console.WriteLine("Correct")
        ElseIf Not IsAnswerCorrect(answer, questionNumber) Then
            Console.WriteLine("Incorrect")
        Else
            Console.WriteLine("Error")
        End If

    End Sub

    Sub AddQuestion(question As String, answer1 As String, answer2 As String, answer3 As String, answer4 As String)
        Dim newQuestions(questions.GetUpperBound(0) + 1, 5) As String

        For i = 0 To questions.GetUpperBound(0) - 1
            For j = 0 To questions.GetUpperBound(1) - 1
                newQuestions(i, j) = questions(i, j)
            Next
        Next

        questions = newQuestions

    End Sub



End Module
