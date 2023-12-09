// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello, World!");

var inputLines = File.ReadAllText("input.txt").Split("\n");

var inputCards = inputLines.Select(s =>
{
    var parts = s.Split(" ");
    return (parts[0], int.Parse(parts[1]));
});

long Part1()
{
    var orderedCards = inputCards.OrderBy(pairs => Day07.HandValue(pairs.Item1)).ToList();
    var result = 0;
    for (var i = 0; i < orderedCards.Count(); i++)
    {
        result += (i + 1) * orderedCards[i].Item2;
    }
    return result;
}

long Part2()
{
    var orderedCards = inputCards.OrderBy(pairs => Day07.HandValuePart2(pairs.Item1)).ToList();
    var result = 0;
    for (var i = 0; i < orderedCards.Count(); i++)
    {
        result += (i + 1) * orderedCards[i].Item2;
    }
    return result;
}

Console.WriteLine(Part1());
Console.WriteLine(Part2());

public class Day07
{
    public static int CalcTypePart1(string cardsString)
    {
        var cards = cardsString.ToList().GroupBy(c => c).ToList();

        if (cards.Count == 1)
        {
            // five of a kind
            return 7;
        }
        else if (cards.Count == 2)
        {
            if (cards.Any(c => c.Count() == 4))
                // four of a kind
                return 6;
            if (cards[0].Count() == 3 || cards[1].Count() == 3)
                // full house
                return 5;
        }
        else if (cards.Count == 3)
        {
            if (cards.Any(c => c.Count() == 3))
                // three of a kind
                return 4;

            // two pair
            return 3;
        }
        else if (cards.Count == 4)
        {
            // one pair
            return 2;
        }

        return 1;
    }

    public static int CalcTypePart2(string cardsString)
    {
        var cards = cardsString.ToList().GroupBy(c => c).ToList();
        var cardsDictionary = cards.ToDictionary(g => g.Key, g => g.Count());
        cardsDictionary.TryAdd('J', 0);

        if (cards.Count == 1)
        {
            // five of a kind
            return 7;
        }
        else if (cards.Count == 2)
        {
            if (cardsDictionary['J'] > 0)
            {
                return 7;
            }
            if (cards.Any(c => c.Count() == 4))
                // four of a kind
                return 6;
            if (cards[0].Count() == 3 || cards[1].Count() == 3)
                // full house
                return 5;
        }
        else if (cards.Count == 3)
        {
            if (cards.Any(c => c.Count() == 3))
            {
                if (cardsDictionary['J'] > 0)
                {
                    // four of a kind
                    return 6;
                }
                // three of a kind
                return 4;
            }

            if (cardsDictionary['J'] == 2)
            {
                // four of a kind
                return 6;
            }
            else if (cardsDictionary['J'] == 1)
            {
                // full house
                return 5;
            }

            // two pair
            return 3;
        }
        else if (cards.Count == 4)
        {
            if (cardsDictionary['J'] > 0)
            {
                // three of a kind
                return 4;
            }

            // one pair
            return 2;
        }

        if (cardsDictionary['J'] > 0)
        {
            // one pair
            return 2;
        }

        return 1;
    }


    public static int CardValuePart1(char card)
    {
        return card switch
        {
            'A' => 14,
            'K' => 13,
            'Q' => 12,
            'J' => 11,
            'T' => 10,
            _ => int.Parse(card.ToString())
        };
    }

    public static int CardValuePart2(char card)
    {
        return card switch
        {
            'A' => 14,
            'K' => 13,
            'Q' => 12,
            'J' => 1,
            'T' => 10,
            _ => int.Parse(card.ToString())
        };
    }


    public static int HandValue(string cards)
    {
        return CardValuePart1(cards[4]) +
               CardValuePart1(cards[3]) * 16 +
               CardValuePart1(cards[2]) * 256 +
               CardValuePart1(cards[1]) * 4096 +
               CardValuePart1(cards[0]) * 65536 +
               CalcTypePart1(cards) * 65536 * 16;
    }

    public static int HandValuePart2(string cards)
    {
        return CardValuePart2(cards[4]) +
               CardValuePart2(cards[3]) * 16 +
               CardValuePart2(cards[2]) * 256 +
               CardValuePart2(cards[1]) * 4096 +
               CardValuePart2(cards[0]) * 65536 +
               CalcTypePart2(cards) * 65536 * 16;
    }

}