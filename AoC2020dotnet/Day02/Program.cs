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
    var rx = new Regex(@"^(\d+)-(\d+) (\w): (\w+)$", RegexOptions.Compiled | RegexOptions.IgnoreCase);

    int numValid = 0;

    foreach (var line in inputLines)
    {
        var match = rx.Matches(line)[0];
        var min = int.Parse(match.Groups[1].Value);
        var max = int.Parse(match.Groups[2].Value);
        var ch = match.Groups[3].Value[0];
        var password = match.Groups[4].Value;
        if (IsPasswordValid(password, ch, min, max))
        {
            numValid++;
        }
    }

    bool IsPasswordValid(string password, char ch, int min, int max)
    {
        var count = password.Count(c => c == ch);
        return count >= min && count <= max;
    }

    return numValid;
}

int Part2()
{
    var rx = new Regex(@"^(\d+)-(\d+) (\w): (\w+)$", RegexOptions.Compiled | RegexOptions.IgnoreCase);

    int numValid = 0;

    foreach (var line in inputLines)
    {
        var match = rx.Matches(line)[0];
        var min = int.Parse(match.Groups[1].Value);
        var max = int.Parse(match.Groups[2].Value);
        var ch = match.Groups[3].Value[0];
        var password = match.Groups[4].Value;
        if (IsPasswordValid(password, ch, min, max))
        {
            numValid++;
        }
    }

    bool IsPasswordValid(string password, char ch, int pos1, int pos2)
    {
        return password[pos1 - 1] == ch ^ password[pos2 - 1] == ch;
    }

    return numValid;

}


Console.WriteLine(Part2());