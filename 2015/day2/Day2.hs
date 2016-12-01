import Data.List.Split
import Data.List

inputLineToSortedIntList :: [Char] -> [Int]
inputLineToSortedIntList s = sort (map (\x -> read x :: Int) (splitOn "x" s))

surfaceArea :: [Int] -> Int
surfaceArea xs = 2*wl + 2*wh + 2*hl + minimum [wl, wh, hl]
    where w = xs !! 0
          l = xs !! 1
          h = xs !! 2
          wl = w*l
          wh = w*h
          hl = h*l

totalSurfaceArea :: [String] -> Int
totalSurfaceArea inputLines = sum (map surfaceArea (map inputLineToSortedIntList inputLines))

ribbonLength :: [Int] -> Int
ribbonLength xs = 2*w + 2*l + w*l*h
    where w = xs !! 0
          l = xs !! 1
          h = xs !! 2

totalRibbonLength :: [String] -> Int
totalRibbonLength inputLines = sum (map ribbonLength (map inputLineToSortedIntList inputLines))

main = do
    f <- readFile "input.txt"
    let totalArea = totalSurfaceArea (lines f)
    let totalRibbon = totalRibbonLength (lines f)
    return (totalArea, totalRibbon)



