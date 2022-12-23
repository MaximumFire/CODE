Imports System
Imports System.IO
Module Program
    Sub Main(args As String())
        Dim lines() As String = File.ReadAllLines("C:\Users\conno\OneDrive\Documents\project.txt")

        For i = 0 To 10
            Console.WriteLine(lines(i))
        Next
    End Sub
End Module
