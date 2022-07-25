Module Program
    Sub Main(args As String())
        Dim name As String
        Dim valued As Integer
        Dim inspired As Integer
        Dim empowered As Integer
        Dim postcard As Boolean
        Dim certificate As Boolean
        Dim badge As Boolean
        Dim award As Boolean
        While True
            postcard = False
            certificate = False
            badge = False
            award = False

            Console.WriteLine("Please enter the student's name : ")
            name = Console.ReadLine()

            Console.Write("Please enter the number of Valued points : ")
            valued = Console.ReadLine()
            Console.Write("Please enter the number of Inspired points : ")
            inspired = Console.ReadLine()
            Console.Write("Please enter the number of Empowered points : ")
            empowered = Console.ReadLine()

            If (valued + inspired + empowered) >= 20 Then
                postcard = True
            End If
            If (valued + inspired + empowered) >= 50 Then
                certificate = True
            End If
            If valued >= 100 Or inspired >= 100 Or empowered >= 100 Then
                badge = True
            End If
            If valued >= 100 And inspired >= 100 And empowered >= 100 Then
                award = True
            End If

            If award Then
                Console.WriteLine("headteacher's award")
            ElseIf badge Then
                Console.WriteLine("dolphin badge")
            ElseIf certificate Then
                Console.WriteLine("certificate")
            ElseIf postcard Then
                Console.WriteLine("postcard")
            End If
        End While
    End Sub
End Module
