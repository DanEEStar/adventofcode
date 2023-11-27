// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello, World!");

var inputLines = File.ReadAllText("input.txt").Split("\n");

int CalculateTrees(int right, int down)
{
    int lineIndex = 0;
    int x = 0;
    int treeCount = 0;

    while (lineIndex < inputLines.Length - 1)
    {
        lineIndex += down;
        x = (x + right) % inputLines[0].Length;

        if (inputLines[lineIndex][x] == '#')
        {
            treeCount++;
        }
    }

    return treeCount;
}

Console.WriteLine(CalculateTrees(3, 1));

long r1 = CalculateTrees(1, 1);
long r2 = CalculateTrees(3, 1);
long r3 = CalculateTrees(5, 1);
long r4 = CalculateTrees(7, 1);
long r5 = CalculateTrees(1, 2);

Console.WriteLine(r1);
Console.WriteLine(r2);
Console.WriteLine(r3);
Console.WriteLine(r4);
Console.WriteLine(r5);

Console.WriteLine(r1 * r2 * r3 * r4 * r5);