import re


POSITIVE = {"amazing", "excellent", "fresh", "friendly", "good", "great", "love"}
NEGATIVE = {"awful", "bad", "cold", "dirty", "poor", "rude", "slow", "terrible"}


def review_features(text: str) -> dict[str, object]:
    tokens = re.findall(r"[a-z']+", text.lower())
    positive = sorted(set(tokens) & POSITIVE)
    negative = sorted(set(tokens) & NEGATIVE)
    score = len(positive) - len(negative)
    return {
        "token_count": len(tokens),
        "sentiment": "positive" if score > 0 else "negative" if score < 0 else "neutral",
        "evidence": positive + negative,
    }
