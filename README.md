# Customer Review Sentiment Analysis

## Project Overview

This project focuses on analyzing customer reviews and classifying their sentiment as **Positive, Negative, or Neutral** using Natural Language Processing (NLP) and Machine Learning techniques.

The project demonstrates text preprocessing, feature extraction, model training, sentiment prediction, and deployment through a Streamlit web application.

## Project Links

- **Live Application:** https://sentiment-analysis-ha3fhjjpptpvtfendzhete.streamlit.app/
- **GitHub Repository:** https://github.com/praveenguvvala01-wq/sentiment-analysis

## Objectives

- Analyze customer reviews using NLP techniques.
- Clean and preprocess textual data.
- Convert text into numerical features using TF-IDF.
- Train a machine learning model for sentiment classification.
- Predict sentiment from user-provided reviews.
- Deploy the application using Streamlit.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Machine Learning
- Streamlit
- Git and GitHub

## Project Structure

```text
sentiment-analysis/
├── app/
│   └── app.py
├── model/
│   └── sentiment_model.pkl
├── notebook/
│   └── Sentiment_Analysis.ipynb
├── data/
│   └── dataset.xlsx
├── .gitignore
├── README.md
└── requirements.txt
```

Note: The folder and file names shown above are examples. Your actual GitHub repository structure may differ. Ensure that the paths and capitalization match your project files.

## Methodology

### 1. Data Collection

The project uses a dataset containing customer reviews for sentiment analysis.

### 2. Data Preprocessing

The text data is prepared for analysis by applying the preprocessing steps implemented in the notebook.

### 3. Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency) is used to transform textual reviews into numerical features that can be processed by a machine learning model.

### 4. Model Training

A machine learning model is trained using the processed text data to classify customer reviews into sentiment categories.

### 5. Sentiment Prediction

The trained model predicts the sentiment of a customer review entered by the user.

### 6. Deployment

The application is deployed using Streamlit, allowing users to enter reviews and view the model's predictions through a web interface.

## How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/praveenguvvala01-wq/sentiment-analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd sentiment-analysis
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the Streamlit Application

If your application file is located at `app/app.py`, run:

```bash
python -m streamlit run app/app.py
```

If your folder or file uses different capitalization or a different path, update the command accordingly.

## Example Reviews

**Positive Review**

"Excellent product, great quality and fast delivery."

**Negative Review**

"Very disappointing. The product stopped working."

**Neutral Review**

"The product is okay, nothing special."

These are example inputs for testing the application. The predicted sentiment depends on the trained model.

## Applications

- Customer feedback analysis
- Product review analysis
- E-commerce sentiment monitoring
- Customer satisfaction analysis
- Business decision support

## Future Improvements

- Improve classification performance through model evaluation and hyperparameter tuning.
- Experiment with advanced NLP techniques and models.
- Expand the dataset to improve generalization.
- Add visualizations showing sentiment distribution.
- Provide additional insights into customer feedback.

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be applied to customer review sentiment classification. The Streamlit interface makes the trained model accessible through a simple web application.

## Author

**Praveen Guvvala**

GitHub: https://github.com/praveenguvvala01-wq

Project Repository: https://github.com/praveenguvvala01-wq/sentiment-analysis

Live Application: https://sentiment-analysis-ha3fhjjpptpvtfendzhete.streamlit.app/
