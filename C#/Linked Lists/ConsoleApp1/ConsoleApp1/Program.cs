using System;
using System.Collections.Generic;

var rng = new Random();

LinkedList<int> list1 = new LinkedList<int> (); // input list 1
LinkedList<int> list2 = new LinkedList<int> (); // input list 2
LinkedList<int> list3 = new LinkedList<int>(); // output list

LinkedList<int> list4 = new LinkedList<int> (); // merge sort tester

for (int i = 0; i < 25; i++)
{
    list4.AddLast(rng.Next(0, 255));
}

list1.AddLast(1);
list1.AddLast(2);
list1.AddLast(4);

list2.AddLast(1);
list2.AddLast(3);
list2.AddLast(4);

static LinkedList<int> MergeLists(LinkedList<int> list1, LinkedList<int> list2)
{
    LinkedList<int> finalList = new LinkedList<int>();
    while (true)
    {
        // if either list is empty, append all items in the other list
        if (0 == list1.Count)
        {
            foreach (int n in list2)
            {
                finalList.AddLast(n);
            }
            break;
        }
        if (0 == list2.Count)
        {
            foreach (int n in list1)
            {
                finalList.AddLast(n);
            }
            break;
        }
        // add lowest current element at index 0 in each list
        if (list1.ElementAt(0) <= list2.ElementAt(0))
        {
            finalList.AddLast(list1.ElementAt(0));
            list1.RemoveFirst();
        }
        else
        {
            finalList.AddLast(list2.ElementAt(0));
            list2.RemoveFirst();
        }
    }
    return finalList;
}

static LinkedList<int> MergeSort(LinkedList<int> list)
{
    LinkedList<LinkedList<int>> split = new LinkedList<LinkedList<int>>();
    foreach (int n in list)
    {
        LinkedList<int> temp = new LinkedList<int> ();
        temp.AddLast (n);
        split.AddLast(temp);
    }
    LinkedList<int> final = new LinkedList<int>();
    foreach (LinkedList<int> temp in split)
    {
        final = MergeLists(final, temp);
    }
    return final;
}

static bool CheckSorted(LinkedList<int> list)
{
    bool isSorted = false;
    for (int i = 1; i < list.Count; i++)
    {
        if (list.ElementAt(i) >= list.ElementAt(i-1))
        {
            isSorted = true;
            continue;
        } else
        {
            isSorted = false;
            break;
        }
    }
    return isSorted;
}

list3 = MergeLists(list1, list2);
list4 = MergeSort(list4);

// loop through items of final list and display them
foreach (int n in list4)
{
    Console.WriteLine(n);
}

Console.WriteLine(CheckSorted(list4));
