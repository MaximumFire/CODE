Imports System

Module Program

    Dim foundFood = CreateObject("Scripting.Dictionary")
    Dim rng As New Random

    Structure Creature
        Dim id As Integer
        Dim strength As Integer
        Dim food As Integer
    End Structure

    Function AddToArray(arr() As Creature, value As Creature) As Creature
        Dim tempArr(arr.Length() + 1) As Creature
        For i = 0 To arr.GetUpperBound(0)
            tempArr(i) = arr(i)
        Next
        tempArr(tempArr.GetUpperBound(0)) = value
        Return tempArr(tempArr.Length())
    End Function

    Sub GetRandomFood(foodCount As Integer, creature As Creature)
        Dim randomAmount As Integer = rng.Next(0, foodCount)
        If foundFood.Exists(randomAmount.ToString()) Then
            If foundFood.keys.Length() Then
            End If
        Else
            Dim tempArr(2) As Creature.passport
            foundFood.Add(randomAmount.ToString(),  
        End If

    End Sub

    Sub Main(args As String())

        Console.Write("How many creatures would you like to create? : ")
        Dim creatureCount As Integer = Console.ReadLine()
        Dim creatures(creatureCount) As Creature
        Dim foodCount As Integer = creatureCount - 2
        Dim conflictValue(1) As Creature
        Dim outcome As Integer = 42



        Console.ReadKey()
    End Sub
End Module
