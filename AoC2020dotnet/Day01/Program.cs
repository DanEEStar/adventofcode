Console.WriteLine("Hello, World!");


int[] Numbers(string input)
{
    return input.Split('\n').Select(int.Parse).ToArray();
}

var input = File.ReadAllText("input.txt");
var numbers = Numbers(input);

var result = from x in numbers
             from y in numbers
             from z in numbers
             where x + y + z == 2020
             select x * y * z;

Console.WriteLine(result.First());

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
