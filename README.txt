
# Customer Review Sentiment Analysis

## Project Overview

This project uses Natural Language Processing (NLP) and Machine
Learning to classify customer product reviews into three sentiment
categories:

- Positive
- Neutral
- Negative

The project includes Exploratory Data Analysis (EDA), text
preprocessing, model comparison, hyperparameter tuning, and a
Streamlit application for interactive sentiment prediction.

**Group:** 4  
**Mentor:** Prajwal  
**Final Model:** TF-IDF + Linear Support Vector Machine (SVM)

## Business Objective

The objective is to extract sentiment from customer reviews
to understand whether customers express positive, neutral, or
negative opinions about a product.

## Dataset Details

The supplied dataset is `dataset.xlsx`.

It contains the following columns:

| Column | Description |
|---|---|
| `title` | Review title |
| `rating` | Customer star rating |
| `body` | Review text |

The dataset's original source is not established by the project
files. Confirm its source before describing it as Amazon data.

### Sentiment Labeling

The notebook derives the target sentiment from the star rating:

| Rating | Sentiment |
|---|---|
| 1–2 | Negative |
| 3 | Neutral |
| 4–5 | Positive |

These labels are inferred from ratings rather than manually
annotated review text.

## Exploratory Data Analysis

The notebook includes:

- Dataset dimensions and column inspection
- Data types and descriptive statistics
- Rating distribution
- Missing-value and duplicate checks
- Review text preparation
- Review length and word-count analysis
- Sentiment distribution
- Duplicate text removal before model training

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine
- GridSearchCV
- Joblib
- Streamlit

## Model Development

Three candidate models are compared:

1. Logistic Regression
2. Multinomial Naive Bayes
3. Linear SVM

The models use TF-IDF text features, including unigrams and
bigrams.

The notebook then tunes the Linear SVM using five-fold
GridSearchCV with Macro F1 as the selection metric.

The final selected pipeline is TF-IDF + Linear SVM.

The saved pipeline includes both text vectorization and the
trained classifier.

## Evaluation

The notebook evaluates the models using:

- Accuracy
- Macro F1-score
- Weighted F1-score
- Classification report
- Confusion matrix

The notebook reports an approximate hold-out accuracy of 79.17%
and Macro F1-score of 63.70% for the selected configuration.
Rerun the notebook to verify these values before final submission.

The Neutral class is a known challenge because it has fewer
examples and is more difficult to classify.

## Project Structure

```text
Sentiment_Analysis/
│
├── app/
│   └── app.py
│
├── model/
│   └── sentiment_model.pkl
│
├── notebook/
│   └── Sentiment_Analysis.ipynb
│
├── data/
│   └── dataset.xlsx
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Local Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Sentiment_Analysis
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub
repository URL.

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Generate the trained model

Open `notebook/Sentiment_Analysis.ipynb`.

Run the notebook using the dataset at `data/dataset.xlsx`.
Ensure the final trained pipeline is saved to:

```text
model/sentiment_model.pkl
```

The model file must exist before starting the application.

### 5. Run Streamlit

From the main project directory:

```bash
streamlit run app/app.py
```

Streamlit will display a local URL in the terminal. Open that
URL in your browser and test the application.

## Streamlit Community Cloud Deployment

1. Push the project to GitHub.
2. Open https://share.streamlit.io/
3. Create a new app and connect the GitHub repository.
4. Select the correct branch.
5. Set the main file path to `app/app.py`.
6. Deploy the application.
7. Test the deployed app using different customer reviews.

Ensure that `model/sentiment_model.pkl` is included in the
repository and that the deployed dependencies are compatible
with the model's training environment.

## Limitations

- Sentiment labels are derived from star ratings.
- A written review may not always agree with its star rating.
- The Neutral class can be difficult to predict accurately.
- The dataset's original source needs to be verified.
- Model performance depends on the dataset and its quality.

## Future Improvements

- Obtain a larger and more balanced dataset.
- Evaluate additional text-classification models.
- Improve Neutral sentiment detection.
- Perform detailed error analysis.
- Validate performance on reviews from an independently
  verified data source.

## Conclusion

This project demonstrates a complete sentiment-analysis
workflow, from customer-review exploration and model training
to an interactive Streamlit deployment.
