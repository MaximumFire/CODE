Imports System
Public Module Module1
	Public slot As String
	Public number As Integer
	Public Sub Main()
		For i As Integer = 1 To 9
			For j As Integer = 1 To 9
				If j = 9 Then
					number = i * j
					slot = number.ToString("00") & " " & vbCrLf
					Console.Write(slot)
				Else
					number = i * j
					slot = number.ToString("00") & " "
					Console.Write(slot)
				End If
			Next
		Next
	End Sub
End Module