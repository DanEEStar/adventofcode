namespace Tests;

public class UnitTestDay07CalcType
{
    [Fact]
    public void CalcTypePart1()
    {
        var highType = Day07.CalcTypePart1("23456");
        Assert.Equal(1, highType);

        var fiveOfAKindType = Day07.CalcTypePart1("55555");
        Assert.Equal(7, fiveOfAKindType);

        var fourOfAKindType = Day07.CalcTypePart1("AA8AA");
        Assert.Equal(6, fourOfAKindType);

        var fullHouse = Day07.CalcTypePart1("23332");
        Assert.Equal(5, fullHouse);

        var threeOfAKind = Day07.CalcTypePart1("TTT98");
        Assert.Equal(4, threeOfAKind);

        var twoPair = Day07.CalcTypePart1("23432");
        Assert.Equal(3, twoPair);

        var onePair = Day07.CalcTypePart1("A23A4");
        Assert.Equal(2, onePair);
    }

    public void CalcTypePart2()
    {
        var oneJ = Day07.CalcTypePart1("QQQJQ");
        Assert.Equal(7, oneJ);
    }


    [Fact]
    public void HandValue()
    {
        var h1 = Day07.HandValue("T55J5");
        Console.WriteLine();
        Assert.Equal(1, h1);
    }
}