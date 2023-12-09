// See https://aka.ms/new-console-template for more information

using System.Text.RegularExpressions;

Console.WriteLine("Hello, World!");

var inputLines = File.ReadAllText("input.txt").Split("\n");

int Part1()
{
    bool HasNeighbours(int x, int y, int length)
    {
        var startX = x > 0 ? x - 1 : x;
        var endX = Math.Min(x + length + 1, inputLines[0].Length);

        var startY = y > 0 ? y - 1 : y;
        var endY = Math.Min(y + 2, inputLines.Length);

        for (var i = startX; i < endX; i++)
        for (var j = startY; j < endY; j++)
        {
            var ch = inputLines[j][i];
            if (char.IsDigit(ch) || ch == '.')
                continue;
            return true;
        }

        return false;
    }

    var result = 0;

    var numRegex = new Regex(@"(\d+)");
    for (var lineIndex = 0; lineIndex < inputLines.Length; lineIndex++)
    {
        var line = inputLines[lineIndex];
        var matches = numRegex.Matches(line);
        foreach (Match match in matches)
        {
            var numString = match.Value;
            // Console.WriteLine(numString);
            var hasNeighbours = HasNeighbours(match.Index, lineIndex, numString.Length);
            Console.WriteLine($"{numString} {hasNeighbours}");
            if (hasNeighbours) result += int.Parse(numString);
        }
    }

    return result;
}

int Part2()
{
    bool HasGearNeighbour(int x, int y, int length, out (int, int) gearPos)
    {
        var startX = x > 0 ? x - 1 : x;
        var endX = Math.Min(x + length + 1, inputLines[0].Length);

        var startY = y > 0 ? y - 1 : y;
        var endY = Math.Min(y + 2, inputLines.Length);

        for (var i = startX; i < endX; i++)
        for (var j = startY; j < endY; j++)
        {
            var ch = inputLines[j][i];
            if (ch == '*')
            {
                gearPos = (i, j);
                return true;
            }
        }

        gearPos = (-1, -1);
        return false;
    }

    var gearNumbers1 = new Dictionary<(int, int), int>();
    var gearNumbers2 = new Dictionary<(int, int), int>();

    var numRegex = new Regex(@"(\d+)");
    for (var lineIndex = 0; lineIndex < inputLines.Length; lineIndex++)
    {
        var line = inputLines[lineIndex];
        var matches = numRegex.Matches(line);
        foreach (Match match in matches)
        {
            var numString = match.Value;
            var num = int.Parse(numString);
            // Console.WriteLine(numString);
            var gearPos = (-1, -1);
            if (HasGearNeighbour(match.Index, lineIndex, numString.Length, out gearPos))
                if (!gearNumbers1.TryAdd(gearPos, num))
                    gearNumbers2[gearPos] = num;
        }
    }

    var gearKeys = gearNumbers1.Keys.Intersect(gearNumbers2.Keys);
    return gearKeys.Sum(gearKey => gearNumbers1[gearKey] * gearNumbers2[gearKey]);
}


Console.WriteLine(Part2());