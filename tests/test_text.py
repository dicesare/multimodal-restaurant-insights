from restaurant_insights import review_features


def test_returns_explainable_sentiment():
    result = review_features("Great fresh food, friendly team")
    assert result["sentiment"] == "positive"
    assert result["evidence"] == ["fresh", "friendly", "great"]


def test_neutral_for_unknown_words():
    assert review_features("Table near the window")["sentiment"] == "neutral"
