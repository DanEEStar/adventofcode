// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello, World!");


long Part1()
{
    /*
     * Time:        56     97     77     93
       Distance:   499   2210   1097   1440
     */
    var input = new List<(long, long)> { (56, 499), (97, 2210), (77, 1097), (93, 1440) };

    var numWins = input.Select(p => Day06.SimulateWinners(p.Item1, p.Item2));
    var product = numWins.Aggregate(1, (acc, x) => acc * (int)x);

    return product;
}

long Part2()
{
    return Day06.SimulateWinners(56977793, 499221010971440);
}

Console.WriteLine(Part2());


public class Day06
{
    public static long SimulateWinners(long time, long distanceToBeat)
    {
        var result = 0;
        for (var i = 0; i < time; i++)
        {
            var speed = i;
            var distance = speed * (time - i);

            if (distance > distanceToBeat) result++;
        }

        return result;
    }
}