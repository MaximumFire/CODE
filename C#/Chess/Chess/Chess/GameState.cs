using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chess
{
    internal class GameState
    {
        public string[,] board = new string[8, 8] { { "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR" }, 
                                                    { "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP" }, 
                                                    { "--", "--", "--", "--", "--", "--", "--", "--" },
                                                    { "--", "--", "--", "--", "--", "--", "--", "--" },
                                                    { "--", "--", "--", "--", "--", "--", "--", "--" },
                                                    { "--", "--", "--", "--", "--", "--", "--", "--" },
                                                    { "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP" },
                                                    { "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR" } };
        public bool whiteToMove = true;
        List<Move> moveLog = new List<Move>();
        List<int> whiteKingLocation = new List<int>();
        List<int> blackKingLocation = new List<int>();
        public bool inCheck = false;

    }

    internal class Move
    {
        public int x;
    }
}
