Imports System

Module Program
    Sub Main()
        Console.WriteLine("How many numbers would you like to enter: ")
        Dim input = Console.ReadLine()
        Convert.ToInt32(input)
        Dim Numlist() As Integer = {}
        For iii = 0 To input - 1
            Console.WriteLine("Enter a number")
            Dim number = Console.ReadLine()
            Convert.ToInt32(number)
            Array.Resize(Numlist, Numlist.Length + 1)
            Numlist(Numlist.Length - 1) = number
        Next
        Dim Count As Integer = 0
        Dim Swapvalue As Integer
        For ii = 0 To Numlist.Length - 2
            For i = 0 To Numlist.Length - 2
                Count += 1
                If Numlist(i) > Numlist(i + 1) Then
                    Swapvalue = Numlist(i)
                    Numlist(i) = Numlist(i + 1)
                    Numlist(i + 1) = Swapvalue
                End If
            Next
        Next
        Console.WriteLine("Number of comparisons: {0}", Count)
        For i = 0 To Numlist.Length - 1
            Console.WriteLine(Numlist(i))
        Next
    End Sub
End Module
