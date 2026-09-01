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

## Case-study gallery

The historical branches contained separate acquisition, text, image and dashboard experiments. They are represented here as concise, safe studies:

| Study | Main question | Portfolio value |
|---|---|---|
| [01 — Data contract](notebooks/01_data_contract.ipynb) | How can platform data be ingested without coupling analysis to credentials? | schemas, validation, privacy boundaries |
| [02 — Review text](notebooks/02_review_text.ipynb) | Which recurring themes and sentiment signals appear in reviews? | NLP preprocessing, interpretable features |
| [03 — Image quality](notebooks/03_image_quality.ipynb) | Which visual metadata can support content analysis? | image features, quality checks, responsible use |
| [04 — Multimodal synthesis](notebooks/04_multimodal_synthesis.ipynb) | How can text and image evidence be combined? | entity-level joins, aggregation, product storytelling |
| [End-to-end demo](notebooks/restaurant_insights.ipynb) | How does the complete offline workflow run? | reproducible synthetic example |

The gallery consolidates the useful work from `master`, `dev` and `main`. Raw notebooks, API modules, cached resources and credentials are intentionally excluded.

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

