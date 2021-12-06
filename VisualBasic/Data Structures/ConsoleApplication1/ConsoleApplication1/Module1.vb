Module Module1
    'Structure that holds info about each player - name, score, rank
    Structure Player
        Dim name As String
        Dim score As Integer
        Dim rank As Integer
    End Structure

    'Global Variables for generating random numbers and for holding each player.
    Dim rng As New Random
    Dim players(1) As Player

    Sub Main()

        'Asks the user to enter the name for player 1 and takes it as an input, saves it to the name value in the structure.
        Console.WriteLine("Enter a name for player 1.")
        players(0).name = Console.ReadLine()

        'Asks the user to enter the name for player 2 and takes it as an input, saves it to the name value in the structure.
        Console.WriteLine("Enter a name for player 2.")
        players(1).name = Console.ReadLine()

        'Makes sure that each player has been given a valid rank
        For i = 0 To players.Length() - 1

            While players(i).rank = Nothing

                Console.WriteLine("Please enter a rank for : " & players(i).name)
                Dim player1Rank As Integer = Console.ReadLine()

                If player1Rank <> 0 Or player1Rank < players.Length() Then
                    players(i).rank = player1Rank
                End If

            End While

        Next

        'Calls the subroutine for flipping the coin
        FlipCoin()

        Console.ReadKey()

    End Sub

    Sub FlipCoin()

        Dim randomNumber As Integer = rng.Next(0, players.Length())

        If players(randomNumber).rank > players.Length() - 1 Or players(randomNumber).rank = 0 Then
            Console.WriteLine(players(randomNumber).name & " is already at the highest/lowest rank!")
        Else
            players(randomNumber).rank = players(randomNumber).rank - 1
            Console.WriteLine(players(randomNumber).name & " had their rank changed from " & players(randomNumber).rank + 1 & " to " & players(randomNumber).rank)
        End If

    End Sub

End Module
