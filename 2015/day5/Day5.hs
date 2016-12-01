import Data.List

isVowel :: Char -> Bool
isVowel c = c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

sameInTuple :: (Char,Char) -> Bool
sameInTuple t = (fst t) == (snd t)

containsBadSubstring :: String -> Bool
containsBadSubstring s = isInfixOf "ab" s || isInfixOf "cd" s || isInfixOf "pq" s || isInfixOf "xy" s

isNiceString :: String -> Bool
isNiceString s = 
    let containsThreeVowels = length (filter isVowel s) >= 3
        containsDoubleLetter = length (filter sameInTuple (zip s (drop 1 s))) >= 1
    in
        containsThreeVowels && containsDoubleLetter && not (containsBadSubstring s)

repeatInTriplet :: (Char, Char, Char) -> Bool
repeatInTriplet (a, _, b) = a == b



main1 = do
    f <- readFile "input.txt"
    let niceStrings = filter isNiceString (lines f)
    return niceStrings
