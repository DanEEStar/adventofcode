// Learn more about F# at http://fsharp.org

open System

let cycle items =
    Seq.initInfinite (fun _ -> items) |> Seq.concat
    
let part1 (input: string) =
    input.Split("\n") 
    |> Seq.map int
    |> Seq.scan (fun a b -> a + b) 0
    |> Seq.last
    
let part2 (input: string) =
    input.Split("\n") 
    |> Seq.map int
    |> cycle
    |> Seq.scan (fun (a, seen) b -> (a + b, Set.add a seen)) (0, Set.empty)
    |> Seq.find (fun (a, seen) -> Set.contains a seen)
    |> fst
    

[<EntryPoint>]
let main argv =
    IO.File.ReadAllText("day01.txt")
    |> part2
    |> printf "%d" 
    0 // return an integer exit code
