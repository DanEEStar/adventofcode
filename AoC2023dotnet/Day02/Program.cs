// See https://aka.ms/new-console-template for more information

using System.Text.RegularExpressions;

var inputLines = File.ReadAllText("input.txt").Split("\n");

// var input = @"
// 1-3 a: abcde
// 1-3 b: cdefg
// 2-9 c: ccccccccc
// ";
// var inputLines = input.Trim().Split("\n");

int Part1()
{
    bool IsRevealsPossible(string[] reveals)
    {
        var revealRx = new Regex(@"(\d+) (red|green|blue)");

        foreach (var reveal in reveals)
        {
            var revealMatches = revealRx.Matches(reveal);
            foreach (Match revealMatch in revealMatches)
            {
                var num = int.Parse(revealMatch.Groups[1].Value);
                var color = revealMatch.Groups[2].Value;

                if (color == "red")
                    if (num > 12)
                        return false;

                if (color == "green")
                    if (num > 13)
                        return false;

                if (color == "blue")
                    if (num > 14)
                        return false;
            }
        }

        return true;
    }

    var result = 0;

    var gameRx = new Regex(@"^Game (\d+): (.*)$", RegexOptions.Compiled | RegexOptions.IgnoreCase);

    foreach (var line in inputLines)
    {
        Console.WriteLine(line);
        var match = gameRx.Matches(line)[0];
        var gameId = int.Parse(match.Groups[1].Value);
        var reveals = match.Groups[2].Value.Split(";");

        if (IsRevealsPossible(reveals)) result += gameId;
    }

    return result;
}

int Part2()
{
    (int, int, int) CalcMinimumCubes(string[] reveals)
    {
        var revealRx = new Regex(@"(\d+) (red|green|blue)");
        var red = 0;
        var green = 0;
        var blue = 0;

        foreach (var reveal in reveals)
        {
            var revealMatches = revealRx.Matches(reveal);
            foreach (Match revealMatch in revealMatches)
            {
                var num = int.Parse(revealMatch.Groups[1].Value);
                var color = revealMatch.Groups[2].Value;

                if (color == "red")
                    if (num > red)
                        red = num;

                if (color == "green")
                    if (num > green)
                        green = num;

                if (color == "blue")
                    if (num > blue)
                        blue = num;
            }
        }

        return (red, green, blue);
    }

    var result = 0;

    var gameRx = new Regex(@"^Game (\d+): (.*)$", RegexOptions.Compiled | RegexOptions.IgnoreCase);

    foreach (var line in inputLines)
    {
        Console.WriteLine(line);
        var match = gameRx.Matches(line)[0];
        var gameId = int.Parse(match.Groups[1].Value);
        var reveals = match.Groups[2].Value.Split(";");

        var (red, green, blue) = CalcMinimumCubes(reveals);
        Console.WriteLine($"red = {red}, green = {green}, blue = {blue}");
        result += red * green * blue;
    }

    return result;
}


Console.WriteLine(Part2());