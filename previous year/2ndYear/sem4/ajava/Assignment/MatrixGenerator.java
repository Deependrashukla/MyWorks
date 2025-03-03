{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2548669464.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[2], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    public class MagicSquare {\u001b[0m\n\u001b[0m           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "public class MagicSquare {\n",
    "\n",
    "    private static int[][] matrix = new int[3][3];\n",
    "    private static boolean[] used = new boolean[10]; // To keep track of used numbers\n",
    "\n",
    "    public static void main(String[] args) {\n",
    "        generateMagicSquare(0, 0);\n",
    "        printMatrix();\n",
    "    }\n",
    "\n",
    "    private static void generateMagicSquare(int row, int col) {\n",
    "        if (row == 3) {\n",
    "            return; // Base case: all rows filled\n",
    "        }\n",
    "\n",
    "        for (int num = 1; num <= 9; num++) {\n",
    "            if (!used[num]) {\n",
    "                // Check if placing num in current position maintains the sum constraint\n",
    "                if (isValid(row, col, num)) {\n",
    "                    matrix[row][col] = num;\n",
    "                    used[num] = true;\n",
    "\n",
    "                    // Move to the next cell\n",
    "                    int nextRow = row;\n",
    "                    int nextCol = col + 1;\n",
    "                    if (nextCol == 3) {\n",
    "                        nextRow++;\n",
    "                        nextCol = 0;\n",
    "                    }\n",
    "\n",
    "                    generateMagicSquare(nextRow, nextCol);\n",
    "\n",
    "                    // Backtrack\n",
    "                    matrix[row][col] = 0;\n",
    "                    used[num] = false;\n",
    "                }\n",
    "            }\n",
    "        }\n",
    "    }\n",
    "\n",
    "    private static boolean isValid(int row, int col, int num) {\n",
    "        // Check if num is already present in the row or column\n",
    "        for (int i = 0; i < 3; i++) {\n",
    "            if (matrix[row][i] == num || matrix[i][col] == num) {\n",
    "                return false;\n",
    "            }\n",
    "        }\n",
    "\n",
    "        // Check diagonals\n",
    "        if (row == col) {\n",
    "            if (matrix[0][0] + matrix[1][1] + num != 15) {\n",
    "                return false;\n",
    "            }\n",
    "        }\n",
    "        if (row + col == 2) {\n",
    "            if (matrix[0][2] + matrix[1][1] + num != 15) {\n",
    "                return false;\n",
    "            }\n",
    "        }\n",
    "\n",
    "        return true;\n",
    "    }\n",
    "\n",
    "    private static void printMatrix() {\n",
    "        System.out.println(\"Magic Square:\");\n",
    "        for (int i = 0; i < 3; i++) {\n",
    "            for (int j = 0; j < 3; j++) {\n",
    "                System.out.print(matrix[i][j] + \" \");\n",
    "            }\n",
    "            System.out.println();\n",
    "        }\n",
    "    }\n",
    "}\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
