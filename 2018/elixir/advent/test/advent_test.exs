defmodule AocTest do
  use ExUnit.Case
  doctest Aoc

  test "greets the world" do
    assert Aoc.Day01.parse_value("-30") == -30
  end
end
