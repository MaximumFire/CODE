Module Module1
    Structure Card
        Dim card As String
        Dim suit As String
    End Structure

    Dim Suits(4) As String
    Dim Cards(13) As String
    Dim RNG As New Random

    Sub Main()
        Suits(0) = "Hearts"
        Suits(1) = "Diamonds"
        Suits(2) = "Clubs"
        Suits(3) = "Spades"

        Cards(0) = "2"
        Cards(1) = "3"
        Cards(2) = "4"
        Cards(3) = "5"
        Cards(4) = "6"
        Cards(5) = "7"
        Cards(6) = "8"
        Cards(7) = "9"
        Cards(8) = "10"
        Cards(9) = "Jack"
        Cards(10) = "Queen"
        Cards(11) = "King"
        Cards(12) = "Ace"

        Dim isPlaying As Boolean = True
        Dim randomCard1 As String
        Dim randomSuit1 As String
        Dim randomCard2 As String
        Dim randomSuit2 As String

        Dim points As Integer = 0
        Dim totalCards As Integer = 52
        Dim roundCount As Integer = 0
        Dim usedCards(52) As Card
        Dim isCardValid As Boolean = False

        While isPlaying = True
            While Not isCardValid
                randomCard1 = Cards(RNG.Next(0, 13))
                randomSuit1 = Suits(RNG.Next(0, 4))

                randomCard2 = Cards(RNG.Next(0, 13))
                randomSuit2 = Suits(RNG.Next(0, 4))

                For y = 0 To usedCards.GetUpperBound(0)
                    If usedCards(y).card = randomCard1 And usedCards(y).suit = randomSuit1 Then
                        isCardValid = False
                    ElseIf usedCards(y).card = randomCard2 And usedCards(y).suit = randomSuit2 Then
                        isCardValid = False
                    Else
                        isCardValid = True
                        usedCards(roundCount).card = randomCard1
                        usedCards(roundCount).suit = randomSuit1


                        usedCards(roundCount + 1).card = randomCard2
                        usedCards(roundCount + 1).suit = randomSuit2
                    End If
                Next
            End While

            totalCards = totalCards - 2

            Console.WriteLine(randomCard1 & " of " & randomSuit1)
            Console.WriteLine(randomCard2 & " of " & randomSuit2)

            Console.WriteLine("You have : " & totalCards & " cards left.")

            If randomCard1 = randomCard2 Then
                Console.WriteLine("The cards have the same value! (+3 points)")
                points = points + 3
            ElseIf randomSuit1 = randomSuit2 Then
                Console.WriteLine("The cards have the same suit! (+1 point)")
                points = points + 1
            End If

            Console.WriteLine("You have : " & points & " points!")
            roundCount = roundCount + 2

            Console.WriteLine("Do you want to continue playing (y/n)?")
            Dim answer As String = Console.ReadLine()
            If answer.ToLower() = "n" Then
                isPlaying = False
            Else
                If roundCount = 52 Then
                    isPlaying = False
                Else
                    isPlaying = True
                End If
            End If
            isCardValid = False
        End While

        Console.ReadKey()
    End Sub

End Module
