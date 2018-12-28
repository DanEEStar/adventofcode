let readInputLines = (fileName) => {
    Node.Fs.readFileAsUtf8Sync(fileName)
    |> Js.String.split("\n")
}


let result = readInputLines("day01.txt")
-> Belt.Array.map(Js.Float.fromString)
-> Belt.Array.reduce(0.0, (+.))
Js.log(result);
