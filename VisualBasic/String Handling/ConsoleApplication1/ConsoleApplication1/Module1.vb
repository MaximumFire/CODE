Module Module1

    Sub Main()
        Console.WriteLine("Please select an option:")
        Console.WriteLine("1. Calculate Length")
        Console.WriteLine("2. Convert to ASCII")
        Console.WriteLine("3. Concatenate")
        Console.WriteLine("4. Convert ToUpper")
        Console.WriteLine("5. Convert ToLower")
        Console.WriteLine("6. Find Character In string")
        Console.WriteLine("7. Get SubString")

        Dim userChoice As Integer = Console.ReadLine()

        If userChoice = 1 Then
            CalculateLength()
        ElseIf userChoice = 2 Then
            ToAscii()
        ElseIf userChoice = 3 Then
            Concatenate()
        ElseIf userChoice = 4 Then
            ConToUpper()
        ElseIf userChoice = 5 Then
            ConToLower()
        ElseIf userChoice = 6 Then
            FindCharacter()
        ElseIf userChoice = 7 Then
            SubString()
        End If
    End Sub

    Sub CalculateLength()
        Console.WriteLine("Enter a string.")
        Dim len As Integer = Console.ReadLine().Length()
        Console.WriteLine("The string was " & len & " characters long.")
    End Sub

    Sub ToAscii()
        Console.WriteLine("Enter a character.")
        Dim val As Integer = Asc(Console.ReadLine())
        Console.WriteLine("That character has the ascii value: " & val)
    End Sub

    Sub Concatenate()
        Console.WriteLine("Enter string 1.")
        Dim str1 As String = Console.ReadLine()
        Console.WriteLine("Enter string 2")
        Dim str2 As String = Console.ReadLine()

        Console.WriteLine(str1 & str2)
    End Sub

    Sub ConToUpper()
        Console.WriteLine("Enter a string.")
        Dim str As String = Console.ReadLine()
        Console.WriteLine(str.ToUpper())
    End Sub

    Sub ConToLower()
        Console.WriteLine("Enter a string.")
        Dim str As String = Console.ReadLine()
        Console.WriteLine(str.ToLower())
    End Sub

    Sub FindCharacter()
        Console.WriteLine("Enter a string.")
        Dim str As String = Console.ReadLine()
        Console.WriteLine("Enter a character to find.")
        Dim chr As String = Console.ReadLine()
        Console.WriteLine("The character was at index " & str.IndexOf(chr))
    End Sub

    Sub SubString()
        Console.WriteLine("Enter a string.")
        Dim str As String = Console.ReadLine()
        Console.WriteLine("Enter the index of the starting character.")
        Dim start As Integer = Console.ReadLine()
        Console.WriteLine("Enter the number of characters.")
        Dim chars As Integer = Console.ReadLine()
        Console.WriteLine(str.Substring(start, chars))
    End Sub

End Module
