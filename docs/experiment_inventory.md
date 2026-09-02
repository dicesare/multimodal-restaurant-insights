# Historical experiment inventory

## Branch coverage

- `main`: introductory README only.
- `master`: complete project directory with the principal notebooks.
- `dev`: the most recent implementation; nine commits and the corrected notebook set.

The public repository never imports the original authentication folders, API module or API key history.

## Notebook evidence

| Historical notebook | Work found | Public representation |
|---|---|---|
| `P6_notebook.ipynb` | broad end-to-end multimodal project | case-study gallery and synthesis notebook |
| `notebok_brut.ipynb` | Yelp acquisition and early data inspection | safe data contract; no live API call |
| `notebok_cours_traitement_text.ipynb` | NLP method exploration | review-text case study |
| `traitement_commentaire.ipynb` | preprocessing, TF-IDF, LDA tuning, coherence analysis and pyLDAvis | text study and historical-results notebook |
| `traitement_image.ipynb` | image archive inspection, balanced sampling, SIFT, VGG16, PCA, t-SNE and clustering | image-quality and historical-results notebooks |
| `notebook_voila.ipynb` | interactive delivery experiment | multimodal synthesis and reporting contract |

## Text-research scale

The LDA tuning loop evaluated **1,680 configurations**. The result table covered:

- 2 to 29 topics;
- two corpus fractions;
- six alpha choices;
- five beta choices.

Recorded coherence ranged from **0.359759** to **0.630641** across all trials. On the full-corpus selection shown in the notebook, the selected parameters were 22 topics, alpha 0.61 and beta 0.01, with coherence **0.5572207084**. The notebook then prepared a pyLDAvis view for topic interpretation.

## Image-research scale

The Yelp photo metadata described **200,100 rows**, **200,098 unique photo IDs**, **36,680 businesses**, **76,413 captions** and five labels:

| Label | Images | Share |
|---|---:|---:|
| food | 108,152 | 54.05% |
| inside | 56,031 | 28.00% |
| outside | 18,569 | 9.28% |
| drink | 15,670 | 7.83% |
| menu | 1,678 | 0.84% |

To avoid training only on the dominant food class, the notebook formed a 1,000-image working set with 200 examples per label. It used an 800/200 train/test split at 224×224 pixels.

The image pipeline explored:

1. SIFT keypoints and descriptors;
2. VGG16 convolutional features;
3. a five-class transfer-learning head;
4. PCA and t-SNE projections;
5. MiniBatchKMeans clustering;
6. adjusted Rand score against known photo labels.

The displayed VGG16-based model had **27,562,821 parameters**, of which **12,848,133** were trainable and **14,714,688** frozen.

## What is deliberately not claimed

The historical image notebook contains incomplete cells and a later feature-extraction error. No final classification accuracy is therefore promoted in this README. Showing the scale, architecture and investigative path is accurate; inventing a clean final score would not be.

