using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingVisualiser
{
    internal interface iSortEngine
    {
        void DoWork(int[] TheArray, Graphics g, int MaxVal);
    }
}
