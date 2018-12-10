// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =
    let text = IO.File.ReadAllText("day01.txt")
    printfn("Hello")
    printfn "%s" text
    0 // return an integer exit code
