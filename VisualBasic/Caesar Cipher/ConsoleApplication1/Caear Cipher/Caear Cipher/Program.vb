Imports System

Module Program
    Sub Main(args As String())
        Dim text As String = Console.ReadLine()

        Dim encrypted As String = Encrypt(text, 5)

        Console.WriteLine(encrypted)

        Dim decrypted As String = Decrypt(encrypted, 5)

        Console.WriteLine(decrypted)

        Console.ReadKey()
    End Sub

    Function Encrypt(x As String, y As Integer) As String
        Dim encrypted As String = ""

        For i = 0 To x.Length() - 1
            encrypted = encrypted & Chr(Asc(x(i)) + y)
        Next

        Return encrypted
    End Function

    Function Decrypt(x As String, y As Integer) As String
        Dim decrypted As String = ""

        For i = 0 To x.Length() - 1
            decrypted = decrypted & Chr(Asc(x(i)) - y)
        Next

        Return decrypted
    End Function
End Module
