// See https://aka.ms/new-console-template for more information

using System.Text.RegularExpressions;

var inputLines = File.ReadAllText("input.txt").Split("\n\n");

List <Dictionary<string, string>> passports = new List<Dictionary<string, string>>();

foreach (var line in inputLines)
{
    var pairs = line.Replace("\n", " ").Split(" ");
    var passport = new Dictionary<string, string>();
    foreach (var pair in pairs)
    {
        var keyValue = pair.Split(":");
        if (keyValue.Length == 2)
        {
            passport.Add(keyValue[0], keyValue[1]);
        }
    }
    passports.Add(passport);
}

string[] requiredFields = new string[] { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };

bool isPassportValid(Dictionary<string, string> passport)
{
    return passport.Keys.Intersect(requiredFields).Count() == requiredFields.Length;
}

bool isPassportValidPart2(Dictionary<string, string> passport)
{
    bool containsKeys = passport.Keys.Intersect(requiredFields).Count() == requiredFields.Length;
    if (!containsKeys)
    {
        return false;
    }

    bool byrValid = int.TryParse(passport["byr"], out var byr) && byr is >= 1920 and <= 2002;
    bool iyrValid = int.TryParse(passport["iyr"], out var iyr) && iyr is >= 2010 and <= 2020;
    bool eyrValid = int.TryParse(passport["eyr"], out var eyr) && eyr is >= 2020 and <= 2030;

    bool hgtValid = false;
    if (passport["hgt"].EndsWith("cm"))
    {
        hgtValid = int.TryParse(passport["hgt"].Replace("cm", ""), out var hgt) && hgt is >= 150 and <= 193;
    }
    else if (passport["hgt"].EndsWith("in"))
    {
        hgtValid = int.TryParse(passport["hgt"].Replace("in", ""), out var hgt) && hgt is >= 59 and <= 76;
    }

    bool hclValid = Regex.IsMatch(passport["hcl"], "^#[0-9a-f]{6}$");
    bool eyeColorsValid = new string[] { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" }.Contains(passport["ecl"]);

    bool pidValid = Regex.IsMatch(passport["pid"], "^[0-9]{9}$");

    return byrValid && iyrValid && eyrValid && hgtValid && hclValid && eyeColorsValid && pidValid;
}


Console.WriteLine(passports);


var numValidPassports = passports.Where(isPassportValidPart2).Count();

Console.WriteLine(numValidPassports);

/*
foreach (var passport in passports)
{
    Console.WriteLine("Passport:");
    // Iterate through each key-value pair in the passport dictionary
    foreach (var field in passport)
    {
        Console.WriteLine($" {field.Key}: {field.Value}");
    }
    Console.WriteLine(); // Print a blank line after each passport for better readability
}
*/