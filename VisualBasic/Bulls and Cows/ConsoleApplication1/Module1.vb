Module Module1
    Public random_number(3) As Integer
    Public random_string As String
    Public used_numbers(3) As Integer
    Public player_numbers(3) As Integer
    Public choice_list(3) As Integer
    Public failed As Boolean = False
    Public won As Boolean = False
    Public number_for_slot As Integer
    Public choice As String
    Dim rng As New Random
    Sub Main()
        Randomize()
        For i = 0 To 3
            number_for_slot = rng.Next(0, 9)
            Dim index1 As Integer = Array.IndexOf(used_numbers, number_for_slot)
            While index1 <> -1
                number_for_slot = rng.Next(0, 9)
                Dim index1 As Integer = Array.IndexOf(used_numbers, number_for_slot)
            End While
            random_number(i) = number_for_slot
            used_numbers(i) = number_for_slot
        Next
        For l = 0 To random_number.Length() - 1
            Dim current_item As Integer
            current_item = random_number(l)
            random_string = random_string & current_item
        Next
        While True
            Console.WriteLine(random_string)
            Dim cows As Integer
            Dim bulls As Integer
            Array.Clear(player_numbers, 0, player_numbers.Length)
            Array.Clear(choice_list, 0, choice_list.Length)
            failed = False
            Console.WriteLine("Enter 'exit' if you want to stop playing or enter a guess to continue.")
            choice = Console.Read()
            If choice = 'exit' Then
                Exit While
            ElseIf choice = random_string Then
                won = True
                Exit While
            End If
            Dim valid_answer As Boolean = choice Like "[0-9][0-9][0-9][0-9]"
            If valid_answer Then
                For j = 0 To choice.Length() - 1
                    Dim current_item As Integer
                    current_item = Val(choice(j))
                    Dim index2 As Integer = Array.IndexOf(player_numbers, current_item)
                    If index2 <> -1 Then
                        failed = True
                    End If
                    player_numbers(j) = current_item

                Next
            End If
        End While
    End Sub

End Module
