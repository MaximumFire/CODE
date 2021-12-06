Module Module1

    Structure Card
        Dim Suit As String
        Dim Value As String
    End Structure

    Dim rng As New Random()


    Dim DeckOfCards(52) As Card
    Dim topOfDeckIndex As Integer = 0
    Dim favouriteSuit As String
    Dim favouriteCard As String

    Sub Main()
        SetupCards("Hearts")
        SetupCards("Diamonds")
        SetupCards("Clubs")
        SetupCards("Spades")

        Console.Write("Please enter your favourite suit: ")
        Dim favouriteSuit As String = Console.ReadLine().ToLower()
        Dim isInvalid As Boolean

        If favouriteSuit = "hearts" Or favouriteSuit = "diamonds" Or favouriteSuit = "clubs" Or favouriteSuit = "spades" Then
            isInvalid = False
        Else
            isInvalid = True
        End If

        While isInvalid
            Console.WriteLine("The entered suit was not valid.")
            Console.Write("Please enter your favourite suit: ")
            favouriteSuit = Console.ReadLine().ToLower()
            If favouriteSuit <> "hearts" Or favouriteSuit <> "diamonds" Or favouriteSuit <> "clubs" Or favouriteSuit <> "spades" Then
                isInvalid = True
            Else
                isInvalid = False
            End If
        End While

        Console.Write("Please enter the name of your favourite card value: ")
        favouriteCard = Console.ReadLine().ToLower()
        Dim validCards(14) As String

        For i = 2 To 16
            validCards(i - 2) = i.ToString()
            If i > 10 Then
                If i = 11 Then
                    validCards(i - 2) = "Jack"
                ElseIf i = 12 Then
                    validCards(i - 2) = "Queen"
                ElseIf i = 13 Then
                    validCards(i - 2) = "King"
                ElseIf i = 14 Then
                    validCards(i - 2) = "Ace"
                End If
            End If
        Next

        For j = 0 To validCards.GetUpperBound(0)
            If favouriteCard = validCards(j).ToLower() Then
                isInvalid = False
            Else
                isInvalid = True
            End If
            ''Console.WriteLine(validCards(j))
        Next

        While isInvalid
            Console.WriteLine("The entered card was not a valid value.")
            Console.Write("Please enter the name of your favourite card value: ")
            favouriteCard = Console.ReadLine().ToLower()
            For j = 0 To validCards.GetUpperBound(0)
                If favouriteCard = validCards(j).ToLower() Then
                    isInvalid = False
                Else
                    isInvalid = True
                End If
            Next
        End While

        While True
            DisplayRandomCard()
            Console.ReadKey()
        End While

    End Sub

    Sub SetupCards(suit As String)
        For i = 2 To 14
            Dim newCard As New Card
            newCard.Suit = suit
            newCard.Value = i

            If i > 10 Then
                If i = 11 Then
                    newCard.Value = "Jack"
                ElseIf i = 12 Then
                    newCard.Value = "Queen"
                ElseIf i = 13 Then
                    newCard.Value = "King"
                ElseIf i = 14 Then
                    newCard.Value = "Ace"
                End If
            End If

            If topOfDeckIndex > DeckOfCards.GetUpperBound(0) Then
                Exit Sub
            End If

            DeckOfCards(topOfDeckIndex) = newCard
            topOfDeckIndex = topOfDeckIndex + 1
        Next

    End Sub

    Sub DisplayRandomCard()

        Dim randomNumber As Integer = rng.Next(52)
        Dim randomCard As Card = DeckOfCards(randomNumber)
        Console.WriteLine(randomCard.Value & " of " & randomCard.Suit)
    End Sub

End Module
