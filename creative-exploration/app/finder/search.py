from difflib import SequenceMatcher
from unicodedata import normalize


def clean(value):
    return normalize("NFC", value.strip()).casefold()


def literal(query, services):
    return [s for s in services if query in clean(s.name) or query in clean(s.category)]


def suggestions(query, services):
    def score(service):
        name = clean(service.name)
        return max(SequenceMatcher(None, query, term).ratio() for term in [name, *name.split()])
    ranked = sorted(((score(s), s) for s in services), key=lambda pair: -pair[0])
    return [service for similarity, service in ranked if similarity >= 0.76][:3]


def lookup(value, services):
    query = clean(value)
    if query:
        for label, strategy in [("Results", literal), ("Possible matches", suggestions)]:
            matches = strategy(query, services)
            if matches:
                return label, matches
    return "Results", []
