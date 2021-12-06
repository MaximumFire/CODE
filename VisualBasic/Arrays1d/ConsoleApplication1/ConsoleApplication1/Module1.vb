Module Module1
    Dim films(10) As String
    Dim ratings(10) As Integer

    Sub Main()
        Console.WriteLine("Enter the first favourite film.")
        films(0) = Console.ReadLine()
        Console.WriteLine("Enter the rating (1 - 5) for the first film.")
        ratings(0) = Console.ReadLine()

        For i = 1 To 2
            Console.WriteLine("Enter another favourite film.")
            films(i) = Console.ReadLine()
            Console.WriteLine("Enter the rating for that film")
            ratings(i) = Console.ReadLine()
        Next

        Console.Write(films(0) & ", ")
        Console.WriteLine(ratings(0))

        For i = 1 To 2
            Console.Write(films(i) & ", ")
            Console.WriteLine(ratings(i))
        Next

        Console.ReadKey()
    End Sub

    Sub AddFilm(index As Integer)
        Console.WriteLine("Enter a film name.")
        Dim film As String = Console.ReadLine()
        films(index) = film
    End Sub

    Sub AddRating(index As Integer)
        Console.WriteLine("Enter a rating")
    End Sub

End Module
