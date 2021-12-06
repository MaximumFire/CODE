Module Module1

    Sub Main()
        Dim names(5, 2) As String
        Dim randomGen As New Random()
        Dim randomInt As Integer = randomGen.Next(0, 5)

        Dim fruits(5) As String
        fruits(0) = "Apple"
        fruits(1) = "Banana"
        fruits(2) = "Mango"
        fruits(3) = "Pineapple"
        fruits(4) = "Melon"

        For i = 0 To 4
            Console.WriteLine("Enter the name.")
            names(i, 0) = Console.ReadLine()
            names(i, 1) = fruits(randomInt)
        Next

        While True
            Console.WriteLine("Name: " & names(randomInt, 0) & "Fruit: " & names(randomInt, 1))
            randomInt = randomGen.Next(0, 5)
            Console.ReadKey()
        End While

        Console.ReadKey()
    End Sub

End Module
