import _ from 'https://cdn.skypack.dev/lodash-es';

const input = await Deno.readTextFile("./input.txt");

function part1(input: string): number {
  const lines = input.split('\n');
  const gammaRateDigits:string[] = [];
  const epsilonRateDigits:string[] = [];

  _.range(12).forEach((index) => {
    const bits = lines.map(line => line[index]).filter(digit => digit === '1');
    if (lines.map(line => line[index]).filter(digit => digit === '1').length > 500) {
      gammaRateDigits.push('1');
      epsilonRateDigits.push('0');
    } else {
      gammaRateDigits.push('0');
      epsilonRateDigits.push('1');
    }
  });

  const gammaRate = parseInt(gammaRateDigits.join(''), 2);
  const epsilonRate = parseInt(epsilonRateDigits.join(''), 2);

  return gammaRate * epsilonRate;
}

function part2(input: string, numDigits = 12): number {
  function findNumber(numbers: string[], n0: string, n1: string): string {
    for (let i = 0; i < numDigits; i++) {
      const oneBits = numbers.map(line => line[i]).filter(digit => digit === '1');
  
      if (oneBits.length >= numbers.length / 2) {
        numbers = numbers.filter(line => line[i] === n0);
      } else {
        numbers = numbers.filter(line => line[i] === n1);
      }

      // console.log(numbers);
      console.log(numbers.length);

      if (numbers.length === 1) {
        return numbers[0];
      }
    }

    return '';
  }

  const lines = input.split('\n');
  const oxygenNumber = findNumber(lines, '1', '0');
  console.log(oxygenNumber);

  const co2Number = findNumber(lines, '0', '1');
  console.log(co2Number);

  return parseInt(co2Number, 2) * parseInt(oxygenNumber, 2);
}

const testInput = `00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010`;

console.log(part1(input));
// console.log(part2(testInput, 5));
console.log(part2(input));
