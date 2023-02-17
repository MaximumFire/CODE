Imports System.IO
Module Program
    Function LibraryCode(title As String, year As String) As String
        Dim parta As String = title.Substring(0, 3)
        Dim partb As String = year.Substring(2, 2)
        Return parta.ToUpper() & partb
    End Function

    Sub Main(args As String())
        Console.Write("Please enter the title of the book. $ ")
        Dim title As String = Console.ReadLine()
        Console.Write("Please enter the year of the book's publication. $ ")
        Dim year As String = Console.ReadLine()
        Dim code As String = LibraryCode(title, year)

        Dim file As New StreamWriter("C:/Users/conno/OneDrive/Documents/GitHub/CODE/VisualBasic/Testing/ConsoleApp1/bookcodes.txt", True)
        file.WriteLine(code)
        file.Close()

        Console.WriteLine("Your code for the specified book: " & code)
    End Sub
End Module
