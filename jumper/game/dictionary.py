import random
class Dictionary:

    words = ["about", "above", "across", "act", "actor", "active", "activity", "add", "afraid", "after", "again", "age", "agree", "air", "all", "alone", "along", "already", "always", "amount", "angry", "another", "answer", "anyone", "anything", "anytime", "appear", "apple", "area", "arm", "army", "around", "arrive", "art", "ask", "attack", "aunt", "autumn", "away", 
    "baby", "base", "back", "bad", "bag", "ball", "bank", "basket", "bath", "bean", "bear", "beautiful", "beer", "bed", "bedroom", "behave", "before", "begin", "behind", "bell", "below", "besides", "best", "better", "between", "big", "bird", "birth", "birthday", "bit", "bite", "black", "bleed", "block", "blood", "blow", "blue", "board", "boat", "body", "boil", "bone", "book", "border", "born", "borrow", "both", "bottle", "bottom", "bowl", "box", "boy", "branch", "brave", "bread", "break", "breakfast", "breathe", "bridge", "bright", 
    "bring", "brother", "brown", "brush", "build", "burn", "business", "bus", "busy", "buy", "cake", "call", "can", "candle", "cap", "car", "card", "care", "careful", "careless", "carry", "case", "cat", "catch", "central", "century", "certain", "chair", "chance", "change", "chase", "cheap", "cheese", "chicken", "child", "children", "chocolate", "choice", "choose", "circle", "city", "class", "clever", "clean", "clear", "climb", "clock", "cloth", "clothes", "cloud", "cloudy", "close", "coffee", "coat", "coin", "cold", "collect", 
    "colour", "comb", "come", "comfortable", "common", "compare", "complete", "computer", "condition", "continue", "control", "cook", "cool", "copper", "corn", "corner", "correct", "cost", "contain", "count", "country", "course", "cover", "crash", "cross", "cry", "cup", "cupboard", "cuttable", "take", "talk", "tall", "taste", "taxi", "tea", "teach", "team", "tear", "telephone", "television", "tell", "ten", "tennis", "terrible", "test", "than", "that", "the", "their", "theirs", "then", "there", "therefore", "these", "thick", "thin", 
    "thing", "think", "third", "this", "those", "though", "threat", "three", "tidy", "tie", "title", "today", "toe", "together", "tomorrow", "tonight", "too", "tool", "tooth", "top", "total", "touch", "town", "train", "tram", "travel", "tree", "trouble", "true", "trust", "twice", "try", "turn", "typemachine", "main", "make", "male", "man", "many", "map", "mark", "market", "marry", "matter", "may", "meal", "mean", "measure", "meat", "medicine", "meet", "member", "mention", "method", "middle", "milk", "mill", "million", "mind", "mine", 
    "minute", "miss", "mistake", "mix", "model", "modern", "moment", "money", "monkey", "month", "moon", "more", "morning", "most", "mother", "mountain", "mouse", "mouth", "move", "much", "music", "must"]

    def __init__(self):
        pass
    def choose_word(self):
        words = self.words
        word = random.choice(words)
        return word
        
    def make_game(self, word):
        lenght = len(word)
        game = []
        for x in lenght:
            game.append("_ ")
        return game 