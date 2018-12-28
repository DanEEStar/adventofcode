// Learn more about F# at http://fsharp.org

open System

let counter (input: string) =
    input
    |> Seq.countBy (fun a -> a)
    |> string

let part1 (input: string) =
    input.Split("\n") 
    //|> Seq.scan (fun a b -> a + b) 0
    |> Seq.last
    
let part2 (input: string) =
    input.Split("\n") 
    |> Seq.map int
    |> Seq.scan (fun (a, seen) b -> (a + b, Set.add a seen)) (0, Set.empty)
    |> Seq.find (fun (a, seen) -> Set.contains a seen)
    |> fst

[<EntryPoint>]
let main argv =
    //IO.File.ReadAllText("day01.txt")
    //|> printf "%d" 
    printf "%s" (counter "rmyxgdlihczskunpfwbgqoeybv")
    0 // return an integer exit code
