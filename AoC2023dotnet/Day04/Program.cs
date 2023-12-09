// See https://aka.ms/new-console-template for more information

var inputLines = File.ReadAllText("input.txt").Split("\n");

int Part1()
{
    int CalcLinePoints(string line)
    {
        var parts = line.Split(":");
        var winningNumbers = parts[1].Split("|")[0].Trim().Split(" ").Where(s => s.Length > 0)
            .Select(s => int.Parse(s.Trim()));
        var userNumbers = parts[1].Split("|")[1].Trim().Split(" ").Where(s => s.Length > 0)
            .Select(s => int.Parse(s.Trim()));

        return (int)Math.Pow(2, userNumbers.Intersect(winningNumbers).Count() - 1);
    }

    var result = 0;
    foreach (var line in inputLines) result += CalcLinePoints(line);

    return result;
}

int Part2()
{
    var winningCards = Enumerable.Repeat(1, inputLines.Length).ToArray();

    int CalcNumWinningNumbers(string line)
    {
        var parts = line.Split(":");
        var winningNumbers = parts[1].Split("|")[0].Trim().Split(" ").Where(s => s.Length > 0)
            .Select(s => int.Parse(s.Trim()));
        var userNumbers = parts[1].Split("|")[1].Trim().Split(" ").Where(s => s.Length > 0)
            .Select(s => int.Parse(s.Trim()));

        return userNumbers.Intersect(winningNumbers).Count();
    }

    for (var i = 0; i < inputLines.Length; i++)
    {
        var numWinningNumbers = CalcNumWinningNumbers(inputLines[i]);
        var numCards = winningCards[i];
        for (var k = i + 1; k < numWinningNumbers + i + 1; k++) winningCards[k] += numCards;
    }

    return winningCards.ToList().Sum();
}


Console.WriteLine(Part2());