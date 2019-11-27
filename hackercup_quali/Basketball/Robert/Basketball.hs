-----------------------------------------------------------------------------
--
-- Module      :  Hackercup.Basketball
-- Copyright   :
-- License     :  AllRightsReserved
--
-- Maintainer  :
-- Stability   :
-- Portability :
--
-- |
--
-----------------------------------------------------------------------------

import qualified Data.Text as T
import qualified Data.Text.Lazy as L
import qualified Data.Text.IO as TIO
import qualified Data.Text.Lazy.Read as LR
import qualified Data.Text.Read as TR

import Data.Monoid
import Data.List
import Control.Exception (assert)

isLeft :: Either a b -> Bool
isLeft (Left _) = True
isLeft _ = False

data Player = Player {
                name :: T.Text,
                shotPercentage :: Int,
                height :: Int
              } deriving (Eq, Show)

getPlayersInMinute :: Int -> Int -> [Player] -> [Player]
getPlayersInMinute m p players= map (\(i,player) -> player) .
                            filter (\(i,_) -> i) .  map (\(i,player) -> (playing i, player)) .
                            zip [0..] $ players
    where
        n = length players
        playing i =
            let m' = if i<p then mod (m+i) n else mod (m-(i-p+1)) n
                in  if m' < p then True else False

playGame :: Int -> Int -> [Player] -> [T.Text]
playGame m p players = sort . map name $
     (getPlayersInMinute m p team1 ++ getPlayersInMinute m p team2)
    where
        (team1, team2) = makeTeams . rankPlayers $ players

rankComp :: Player -> Player -> Ordering
rankComp  p1 p2
  | shotPercentage p1 < shotPercentage p2 = LT
  | shotPercentage p1 > shotPercentage p2 = GT
  | height p1 < height p2 = LT
  | height p1 > height p2 = GT
  | otherwise = EQ


rankPlayers :: [Player] -> [Player]
rankPlayers = reverse . sortBy rankComp


makeTeams :: [Player] -> ([Player], [Player])
makeTeams (p1:p2:rem) = (p1:p1s, p2:p2s)
    where (p1s, p2s) = makeTeams rem
makeTeams (p1:[]) = (p1:[], [])
makeTeams [] = ([],[])




-- Parse players, every player is on a separate line of input
parsePlayers :: [T.Text] -> Either String [Player]
parsePlayers = mapM parsePlayer

parsePlayer :: T.Text -> Either String Player
parsePlayer l = do
    let (name:perc:hght:[]) = T.words l
    iperc <- readAll TR.decimal $ perc
    ihght <- readAll TR.decimal $ hght
    return $ Player name iperc ihght


readAll :: (T.Text -> Either String (a, T.Text)) -> T.Text -> Either String a
readAll parse input = do
    (res, rem) <- parse input
    if rem == T.empty
        then Right res
        else Left $ "Input \"" ++ T.unpack input ++"\" had trailing garbage: " ++ T.unpack rem

parseChallenge :: [T.Text] -> Either String (T.Text, [T.Text])
parseChallenge [] = error "Some ugly bastard called parseChallenge with an empty list!"
parseChallenge input = do
        (n:m:p:[]) <- mapM (readAll TR.decimal) . T.words . head $ input
        let remChallenges = drop n .tail $ input
        let iplayers = take n . tail $ input
        players <- parsePlayers iplayers
        if anyEqual rankComp players
            then Left "Not supposed to happen, Facebook betrayed us, there are two equal players!"
            else Right ((T.unwords . playGame m p $ players),  remChallenges)
    where
        anyEqual cmp [] = False
        anyEqual cmp xxs@(x:xs) = or . zipWith (\a b -> cmp a b== EQ) xxs $ xs


-- Apply a function repeately on its result until its remainder is empty
doRecursive :: ([a] -> (b,[a])) -> [a] -> [b]
doRecursive _ [] = []
doRecursive f arg = let (result, rem) = f arg
    in result : doRecursive f rem

parseChallengesRec :: [T.Text] -> [Either String T.Text]
parseChallengesRec [] = []
parseChallengesRec input =
    case parseChallenge input  of
        Left errorMsg ->  Left errorMsg : parseChallengesRec findNext
        Right (result, rem) -> Right result : parseChallengesRec rem
    where
        findNext = dropWhile (\l -> T.words l == [] || (isLeft . readAll TR.decimal . head . T.words) l) . tail $ input

parseChallenges :: T.Text -> T.Text
parseChallenges input = T.unlines $ zipWith printResLine
         [1..] (parseChallengesRec input')
    where
        input' = tail . T.lines $ input
        printResLine num (Left errorMsg) = T.pack ("ERROR in Case #" ++ show num ++ ": " ++ errorMsg )
        printResLine num (Right res) = T.pack ("Case #" ++ show num ++ ": ") `mappend` res


main = TIO.interact parseChallenges
