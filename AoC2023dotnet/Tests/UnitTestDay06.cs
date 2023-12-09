namespace Tests;

public class UnitTestDay06
{
    [Fact]
    public void Test1()
    {
        var result = Day06.SimulateWinners(30, 200);
        Assert.Equal(9, result);
    }
}