import _ from "https://cdn.skypack.dev/lodash-es";

const input = await Deno.readTextFile("./input.txt");

function part1(input: string): number {
  const inputLines = input.split("\n");

  const lineRegex = /(\d+),(\d+) -> (\d+),(\d+)/;

  const lines = inputLines.map((line) => {
    let [, xs1, ys1, xs2, ys2] = line.match(lineRegex) as string[];
    return [parseInt(xs1), parseInt(ys1), parseInt(xs2), parseInt(ys2)];
  }).filter((coords) => {
    return coords[0] === coords[2] || coords[1] === coords[3];
  });

  console.log(lines.length);

  const diagram = new Map<string, number>();
  lines.forEach((coords) => {
    // console.log(coords);
    if (coords[0] === coords[2]) {
      _.range(Math.min(coords[1], coords[3]), Math.max(coords[1], coords[3]) + 1).forEach((n) => {
        const key = `${coords[0]},${n}`;
        // console.log(key);
        diagram.set(key, (diagram.get(key) || 0) + 1);
      });
    } else {
      _.range(Math.min(coords[0], coords[2]), Math.max(coords[0], coords[2]) + 1).forEach((n) => {
        const key = `${n},${coords[1]}`;
        // console.log(key);
        diagram.set(key, (diagram.get(key) || 0) + 1);
      });
    }
  });

  // console.log(Array.from(diagram.entries()));

  return Array.from(diagram.values()).filter((n) => n > 1).length;
}

function part2(input: string): number {
  const inputLines = input.split("\n");

  const lineRegex = /(\d+),(\d+) -> (\d+),(\d+)/;

  const lines = inputLines.map((line) => {
    let [, xs1, ys1, xs2, ys2] = line.match(lineRegex) as string[];
    return [parseInt(xs1), parseInt(ys1), parseInt(xs2), parseInt(ys2)];
  });

  console.log(lines.length);
  const diagram = new Map<string, number>();

  lines.forEach((coords) => {
    // console.log(coords);
    if (coords[0] === coords[2]) {
      _.range(Math.min(coords[1], coords[3]), Math.max(coords[1], coords[3]) + 1).forEach((n) => {
        const key = `${coords[0]},${n}`;
        // console.log(key);
        diagram.set(key, (diagram.get(key) || 0) + 1);
      });
    } else if (coords[1] === coords[3]) {
      _.range(Math.min(coords[0], coords[2]), Math.max(coords[0], coords[2]) + 1).forEach((n) => {
        const key = `${n},${coords[1]}`;
        // console.log(key);
        diagram.set(key, (diagram.get(key) || 0) + 1);
      });
    } else {
      // console.log(coords);
      const xDiff = coords[0] < coords[2] ? 1 : -1;
      const xs = _.range(coords[0], coords[2] + xDiff, xDiff);
      const yDiff = coords[1] < coords[3] ? 1 : -1;
      const ys = _.range(coords[1], coords[3] + yDiff, yDiff).forEach((n, index) => {
        const key = `${xs[index]},${n}`;
        // console.log(key);
        diagram.set(key, (diagram.get(key) || 0) + 1);
      });
    }
  });

  // console.log(Array.from(diagram.entries()));

  return Array.from(diagram.values()).filter((n) => n > 1).length;
}

const testInput = `0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2`

// console.log(part1(input));
console.log(part2(input));
