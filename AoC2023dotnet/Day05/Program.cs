// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello, World!");

var input = File.ReadAllText("input.txt");


long Part1()
{
    List<(long, long, long)> getMap(IEnumerable<string> lines)
    {
        return lines.Select(line =>
        {
            var nums = line.Split(" ").Select(long.Parse).ToArray();
            if (nums.Length == 3) return (nums[0], nums[1], nums[2]);

            throw new Exception("wrong numbers");
        }).ToList();
    }

    var inputParts = input.Split("\n\n");

    var seeds = inputParts[0].Split(":")[1].Split(" ").Where(s => s.Length > 0).Select(long.Parse).ToList();
    var seedToSoilMap = getMap(inputParts[1].Split("\n").Skip(1));
    var soilToFertilizerMap = getMap(inputParts[2].Split("\n").Skip(1));
    var fertilizerToWaterMap = getMap(inputParts[3].Split("\n").Skip(1));
    var waterToLightMap = getMap(inputParts[4].Split("\n").Skip(1));
    var lightToTemperatureMap = getMap(inputParts[5].Split("\n").Skip(1));
    var temperatureToHumidityMap = getMap(inputParts[6].Split("\n").Skip(1));
    var humidityToLocationMap = getMap(inputParts[7].Split("\n").Skip(1));

    long ConvertMap(long value, List<(long, long, long)> map)
    {
        foreach (var (dest, src, length) in map)
            if (value >= src && value < src + length)
                return value + (dest - src);

        return value;
    }

    long ConvertAllMaps(long value)
    {
        value = ConvertMap(value, seedToSoilMap);
        value = ConvertMap(value, soilToFertilizerMap);
        value = ConvertMap(value, fertilizerToWaterMap);
        value = ConvertMap(value, waterToLightMap);
        value = ConvertMap(value, lightToTemperatureMap);
        value = ConvertMap(value, temperatureToHumidityMap);
        value = ConvertMap(value, humidityToLocationMap);
        return value;
    }

    return seeds.Select(ConvertAllMaps).Min();
}

long Part2()
{
    List<(long, long, long)> getMap(IEnumerable<string> lines)
    {
        return lines.Select(line =>
        {
            var nums = line.Split(" ").Select(long.Parse).ToArray();
            if (nums.Length == 3) return (nums[0], nums[1], nums[2]);

            throw new Exception("wrong numbers");
        }).ToList();
    }

    var inputParts = input.Split("\n\n");

    var inputSeeds = inputParts[0].Split(":")[1].Split(" ").Where(s => s.Length > 0).Select(long.Parse).ToList();
    var seedPairs = inputSeeds.Where((_, i) => i % 2 == 0)
        .Zip(inputSeeds.Where((_, i) => i % 2 == 1), (a, b) => (a, b))
        .ToList();

    IEnumerable<long> CreateRange(long start, long count)
    {
        var limit = start + count;

        while (start < limit)
        {
            yield return start;
            start++;
        }
    }

    var seeds = new List<long>();
    for (var i = 0; i < inputSeeds.Count; i += 2) seeds.AddRange(CreateRange(inputSeeds[i], inputSeeds[i + 1]));

    var seedToSoilMap = getMap(inputParts[1].Split("\n").Skip(1));
    var soilToFertilizerMap = getMap(inputParts[2].Split("\n").Skip(1));
    var fertilizerToWaterMap = getMap(inputParts[3].Split("\n").Skip(1));
    var waterToLightMap = getMap(inputParts[4].Split("\n").Skip(1));
    var lightToTemperatureMap = getMap(inputParts[5].Split("\n").Skip(1));
    var temperatureToHumidityMap = getMap(inputParts[6].Split("\n").Skip(1));
    var humidityToLocationMap = getMap(inputParts[7].Split("\n").Skip(1));

    long ConvertMap(long value, List<(long, long, long)> map)
    {
        foreach (var (dest, src, length) in map)
            if (value >= src && value < src + length)
                return value + (dest - src);

        return value;
    }

    long ConvertAllMaps(long value)
    {
        value = ConvertMap(value, seedToSoilMap);
        value = ConvertMap(value, soilToFertilizerMap);
        value = ConvertMap(value, fertilizerToWaterMap);
        value = ConvertMap(value, waterToLightMap);
        value = ConvertMap(value, lightToTemperatureMap);
        value = ConvertMap(value, temperatureToHumidityMap);
        value = ConvertMap(value, humidityToLocationMap);
        return value;
    }

    // brute forcing solution
    return seeds.Select(ConvertAllMaps).Min();
}


Console.WriteLine(Part2());