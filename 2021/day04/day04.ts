import _ from "https://cdn.skypack.dev/lodash-es";

const input = await Deno.readTextFile("./input.txt");

function part1(input: string): number {
  const lines = input.split("\n");

  const bingoNumbers = lines[0].split(",").map((n) => parseInt(n));
  console.log(bingoNumbers);
  console.log(bingoNumbers.length);

  const boards = _.chunk(lines.slice(2), 6).map((rawBoard) => {
    const board: string[] = rawBoard.slice(0, 5);
    return board.map((row) => row.trim().split(/\s+/).map((n) => parseInt(n)));
  });
  // console.log(boards);

  let bingoBoard;
  for (let i = 0; i < bingoNumbers.length; i++) {
    const currentNumbers = bingoNumbers.slice(0, i);
    // console.log(currentNumbers);
    const currentNumber = currentNumbers[currentNumbers.length - 1];
    console.log(i, currentNumber);

    bingoBoard = boards.find((board) => {
      return board.some((row) => {
        // console.log(row);
        return _.intersection(row, currentNumbers).length === 5;
      });
    });

    if (bingoBoard) {
      console.log(bingoBoard);
      console.log(currentNumber);
      const unmarkedNumbers = bingoBoard.flatMap((row) => {
        return _.difference(row, currentNumbers);
      });
      console.log(unmarkedNumbers);
      return _.sum(unmarkedNumbers) * currentNumber;
    }
  }

  return 0;
}

function part2(input: string): number {
  const lines = input.split("\n");

  const bingoNumbers = lines[0].split(",").map((n) => parseInt(n));
  // console.log(bingoNumbers);
  // console.log(bingoNumbers.length);

  let boards = _.chunk(lines.slice(2), 6).map((rawBoard) => {
    const board: string[] = rawBoard.slice(0, 5);
    return board.map((row) => row.trim().split(/\s+/).map((n) => parseInt(n)));
  });
  // console.log(boards);

  for (let i = 0; i < bingoNumbers.length; i++) {
    const currentNumbers = bingoNumbers.slice(0, i);
    const currentNumber = currentNumbers[currentNumbers.length - 1];
    // const currentNumber2 = bingoNumbers[currentNumbers.length];
    console.log(i, currentNumber);

    const nextBoards = boards.filter((board) => {
      return !board.some((row) => {
        // console.log(row);
        return _.intersection(row, currentNumbers).length === 5;
      });
    });

    console.log(boards.length);

    if (nextBoards.length === 0) {
      const bingoBoard = boards[0];
      console.log(bingoBoard);
      console.log(currentNumber);
      const unmarkedNumbers = bingoBoard.flatMap((row) => {
        return _.difference(row, currentNumbers);
      });
      console.log(unmarkedNumbers);
      return _.sum(unmarkedNumbers) * currentNumber;
    }

    boards = nextBoards;
  }

  return 0;
}

// console.log(part1(input));
console.log(part2(input));
