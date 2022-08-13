from nltk.chat.util import Chat, reflections
logics = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is socratis's chatBot, but you can call me whatever you want.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [ r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla|salam)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*) ?",
        ["Socratis created me!!",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Dakar, Senegal',]
    ],

    [
        r"how (.*) videogame (.*)",
        ["VideoGame is very fun, i love fifa, nba 2k and fortnite too... ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of BasketBall, not that asked but Stephan Curry is my player...",]
    ],
    [
        r"who (.*) (best|genius|socratis)?",
        ["Socratis is a genius who write some codes for fun..."]
    ],
        [
        r"quit|bye",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

print("Hi, I'm socratis's chatBot\nPlease type lowercase english language to start a conversation. Type quit to leave ")
chat = Chat(logics, reflections)
chat.converse()