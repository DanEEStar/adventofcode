import { readLines } from "https://deno.land/std/io/buffer.ts";

const input = await Deno.readTextFile("./input.txt");

function part1(input: string): number {
  const lines = input.split('\n');

  let lastInput:number|null = null;
  let incrementCount = 0;

  lines.forEach((line) => {
    const currentNumber = parseInt(line);
    if (lastInput && currentNumber > lastInput) {
      incrementCount += 1;
    }
    lastInput = currentNumber;
  })

  return incrementCount;
}

function part2(input: string): number {
  const lines = input.split('\n');
  const numbers = lines.map((line) => parseInt(line));

  let lastSlidingWindow:number|null = null;
  let incrementCount = 0;

  numbers.forEach((number, index) => {
    const currentSlidingWindow = number + (numbers[index+1] || 0) + (numbers[index+2] || 0);

    if (lastSlidingWindow && currentSlidingWindow > lastSlidingWindow) {
      incrementCount += 1;
    }
    lastSlidingWindow = currentSlidingWindow;
  })

  return incrementCount;
}

// console.log(part1(input));
console.log(part2(input));
