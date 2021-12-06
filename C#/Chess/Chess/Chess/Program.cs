using System;
using System.Collections.Generic;
using System.Linq;

namespace Chess
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            GameState gs = new GameState();
            DisplayBoard(gs);
        }

        static void DisplayBoard(GameState gs)
        {
            string text = "";
            for (int i = 0; i < gs.board.GetLength(0); i++)
            {
                for (int j = 0; j < gs.board.GetLength(1); j++)
                {
                    text += Convert.ToString(gs.board[i, j]) + " ";
                }
                text += "\n";
            }
            Console.WriteLine(text);
        }
    }
}