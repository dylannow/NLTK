import nltk
from nltk import CFG
from nltk import generate

# Define the CFG rules
grammar = CFG.fromstring('''
    Det -> "The" | "the"
    Adj -> "very" | "hard" | "dark" | "this" | "good" | "young" | "impossible" | "ready" | "own" | "grave" | "chosen"
    N -> "Republic" | "Sith" | "side" | "assassin" | "Force" | "master" | "mind" | "fear" | "boy" | "future" | "apprentice" | "second" | "council" | "level" | "Knight" | "danger" | "defiance" | "need" | "apprentice" | "master"
    V -> "is" | "threatened" | "involved" | "see" | "discover" | "must" | "stay" | "protect" | "be" | "say" | "request" | "tested" | "feel" | "are" | "can" | "think" | "leads" | "suffering" | "have" | "sense" | "were" | "mask" | "take" | "know" | "learn" | "draw" | "decided" | "train" | "agree" | "do" | "will"
    PropN -> "Qui-Gon" | "Qui-Gon's" | "Naboo" | "Skywalker"
    P -> "with" | "on" | "in" | "of" | "to" | "as"
    Modal -> "May" | "will" | "do" | "can"

    # Basic sentence structure
    S -> NP VP

    # Adverbial phrases
    S -> AdvP VP NP
    S -> AdvP VP
    AdvP -> Adv

    # Imperative sentences with object-subject inversion
    S -> V NP NP
    S -> V NP

    # Noun phrases
    NP -> Det N
    NP -> Det Adj N
    NP -> PropN

    # Verb phrases
    VP -> V
    VP -> V NP
    VP -> V NP PP
    VP -> Modal VP

    # Prepositional phrases
    PP -> P NP
    ''')

nltk.parse.generate.generate(grammar, start=None, depth=2, n=1)