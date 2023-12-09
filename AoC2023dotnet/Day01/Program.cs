using System.Text.RegularExpressions;

Console.WriteLine("Hello, World!");


int Part1(string input)
{
    var digit1 = -1;
    var digit2 = -1;
    foreach (var ch in input)
        if (char.IsDigit(ch))
        {
            if (digit1 == -1)
            {
                digit1 = ch - '0';
                digit2 = ch - '0';
            }
            else
            {
                digit2 = ch - '0';
            }
        }

    var result = digit1 * 10 + digit2;
    Console.WriteLine(result);
    return result;
}

int Part2(string input)
{
    var numStrings = new Dictionary<string, int>
    {
        ["one"] = 1,
        ["two"] = 2,
        ["three"] = 3,
        ["four"] = 4,
        ["five"] = 5,
        ["six"] = 6,
        ["seven"] = 7,
        ["eight"] = 8,
        ["nine"] = 9
    };

    int ToNumber(string str)
    {
        return numStrings.TryGetValue(str, out var value) ? value : -1;
    }


    var digit1 = -1;
    var digit2 = -1;

    // Console.WriteLine(input);

    var length = input.Length;
    for (var i = 0; i < length; i++)
    {
        var ch = input[i];
        if (char.IsDigit(ch))
        {
            if (digit1 == -1)
            {
                digit1 = ch - '0';
                digit2 = ch - '0';
            }
            else
            {
                digit2 = ch - '0';
            }

            continue;
        }

        var rx = new Regex(@"^(one|two|three|four|five|six|seven|eight|nine)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        var match = rx.Matches(input[i..]);

        if (match.Count > 0)
        {
            var numString = match[0].Groups[1].Value;
            var num = ToNumber(numString);

            if (num > 0)
            {
                // Console.WriteLine(num);
                if (digit1 == -1)
                {
                    digit1 = num;
                    digit2 = num;
                }
                else
                {
                    digit2 = num;
                }
            }
        }
    }

    var result = digit1 * 10 + digit2;
    // Console.WriteLine(result);
    return result;
}

var input = File.ReadAllText("input.txt");
var lines = input.Split('\n');

var sumNumbers = lines.Select(Part1).Sum();

Console.WriteLine(sumNumbers);


/*
for (var i = 0; i < numbers.Length; i++)
{
    for (var j = i + 1; j < numbers.Length; j++)
    {
        for (var k = i + 2; k < numbers.Length; k++)
        {
            var sum = numbers[i] + numbers[j] + numbers[k];

            if (sum == 2020)
            {
                Console.WriteLine(numbers[i]);
                Console.WriteLine(numbers[j]);
                Console.WriteLine(numbers[k]);
                Console.WriteLine(numbers[i] * numbers[j] * numbers[k]);
                return;
            }
        }
    }
}
*/