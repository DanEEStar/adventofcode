import { readLines } from "https://deno.land/std/io/buffer.ts";

const input = await Deno.readTextFile("./input.txt");

function part1(input: string): number {
  const lines = input.split('\n');

  let depth = 0;
  let position = 0;

  lines.forEach((line) => {
    const [command, numStr] = line.split(/\s+/);
    const num = parseInt(numStr);

    switch (command) {
      case "forward":
        position += num;
        break;
      case "down":
        depth += num;
        break;
      case "up":
        depth -= num;
        break;
    }
  })

  console.log(depth, position);

  return depth * position;
}

function part2(input: string): number {
  const lines = input.split('\n');

  let depth = 0;
  let position = 0;
  let aim = 0;

  lines.forEach((line) => {
    const [command, numStr] = line.split(/\s+/);
    const num = parseInt(numStr);

    switch (command) {
      case "forward":
        position += num;
        depth += aim * num;
        break;
      case "down":
        aim += num;
        break;
      case "up":
        aim -= num;
        break;
    }
  })

  console.log(depth, position);

  return depth * position;
}

console.log(part1(input));
console.log(part2(input));
