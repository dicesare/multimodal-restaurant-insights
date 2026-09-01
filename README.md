# Multimodal Restaurant Insights

An offline, privacy-conscious pipeline for exploring restaurant review text and image metadata without requiring Yelp API credentials.

## Portfolio story

The project combines two modalities often encountered in product analytics:

- review text: normalization, simple sentiment evidence and aggregate trends;
- images: safe metadata and quality features such as dimensions, aspect ratio and brightness.

It is designed for the Yelp Open Dataset or fully synthetic examples. The public repository performs no authenticated API call.

## Quick start

```bash
python -m venv .venv
pip install -e .[dev]
pytest
jupyter lab notebooks/restaurant_insights.ipynb
```

## Security design

- no API key, token or authentication module;
- `.env` and raw data are ignored;
- examples are synthetic;
- network access is outside the analysis package;
- the compromised historical repository is never imported.

## Responsible use

Review sentiment is subjective and can vary by language and culture. Image analysis must respect licensing, privacy and platform terms. Results are exploratory, not automated moderation decisions.

## License

Code is released under the [MIT License](LICENSE). Yelp datasets and media remain governed by their own terms.
