import random
class CardValue:
    def __init__(self, value_txt: str, value_pts: int):
        self.value_txt = value_txt
        self.value_pts = value_pts

class CardColor:
    def __init__(
        self,
        shade: str,
        shade_name: str,
        foreground_color: str = "",
        background_color: str = "",
    ):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color


class Card:

    def __init__(self, value: CardValue, color: CardColor):
        self.value = value
        self.color = color

    def is_equal_value(self, card: "Card") -> bool:
        return self.value.value_pts == card.value.value_pts

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Card)
            and self.value.value_pts == other.value.value_pts
        )

    def __lt__(self, other: "Card") -> bool:
        return self.value.value_pts < other.value.value_pts

    def __gt__(self, other: "Card") -> bool:
        return self.value.value_pts > other.value.value_pts

    def __str__(self) -> str:
        return f"{self.value.value_txt}{self.color.shade}"

    def __repr__(self) -> str:
        return f"Card('{self.value.value_txt}', '{self.color.shade}')"


class Deck:

    def __init__(self):
        self.cards: list[Card] = []
        self.discard_pile: list[Card] = []

    def init52_cards(self):
        self.cards = [
            Card(CardValue(txt, pts), CardColor(shade, name))
            for shade, name in [
                ("♠", "Pique"),
                ("♣", "Trèfle"),
                ("♦", "Carreau"),
                ("♥", "Cœur"),
            ]
            for txt, pts in [
                ("2", 2),
                ("3", 3),
                ("4", 4),
                ("5", 5),
                ("6", 6),
                ("7", 7),
                ("8", 8),
                ("9", 9),
                ("10", 10),
                ("J", 11),
                ("Q", 12),
                ("K", 13),
                ("A", 14),
            ]
        ]
        self.discard_pile.clear()

    def Shuffle(self):
        random.shuffle(self.cards)

    def Draw(self) -> Card | None:
        return self.cards.pop(0) if self.cards else None

    def Discard(self, card: Card):
        self.discard_pile.append(card)

    def __str__(self) -> str:
        return f"Deck({len(self.cards)} cartes)"


def play_duel():
    deck = Deck()
    deck.init52_cards()
    deck.Shuffle()

    p1, p2 = 0, 0
    while len(deck.cards) >= 2:
        c1, c2 = deck.Draw(), deck.Draw()
        print(f"J1: {c1} vs J2: {c2}")

        if c1 > c2:
            p1 += 1
        elif c2 > c1:
            p2 += 1

        deck.Discard(c1)
        deck.Discard(c2)

    print(f"Score : J1={p1} | J2={p2}")


if __name__ == "__main__":
    play_duel()