import _ from "https://cdn.skypack.dev/lodash-es";

const input = await Deno.readTextFile("./input.txt");

function part1(input: string, numSteps: number): number {
  function step(state: number[]):number[] {
    let newState:number[] = [];
    let newFish = 0;

    state.forEach((n, _index) => {
      if (n === 0) {
        newState.push(6);
        newFish += 1;
      } else {
        newState.push(n-1)
      }
    });

    newState = _.concat(newState, Array(newFish).fill(8));
    return newState;
  }

  const inputLines = input.split("\n");
  const initialState = inputLines[0].split(',').map(n => parseInt(n));
  let state = initialState;

  console.log(initialState);

  for (let i = 0; i < numSteps; i++) {
    state = step(state);
    console.log(i, state.length);
  }

  return state.length;
}

function part2(input: string, numSteps: number): number {
  const inputLines = input.split("\n");

  const initialState = inputLines[0].split(',').map(n => parseInt(n));
  console.log(initialState);

  let numFishes = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
  }

  initialState.forEach(n => {
    if (n >= 0 && n <= 8) {
      // @ts-ignore
      numFishes[n] += 1;
    }
  });

  console.log(numFishes);

  for (let step = 0; step < numSteps; step++) {
    let newNumFishes = _.clone(numFishes);
    for (let i = 0; i <= 8; i++) {
      if (i === 6) {
        newNumFishes[6] = numFishes[0] + numFishes[7];
      } else if (i === 8) {
        newNumFishes[8] = numFishes[0];
      } else {
        // @ts-ignore
        newNumFishes[i] = numFishes[i + 1];
      }
    }

    numFishes = newNumFishes;
    console.log(numFishes);
    console.log(_.sum(_.values(numFishes)));
  }

  return _.sum(_.values(numFishes));
}

const testInput = `3,4,3,1,2`;

// console.log(part1(testInput, 80));
// console.log(part1(testInput, 18));
// console.log(part1('8', 256));
console.log(part2(input, 256));
