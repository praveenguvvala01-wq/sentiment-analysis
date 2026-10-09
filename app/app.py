
from pathlib import Path

import joblib
import streamlit as st


# --------------------------------------------------
# Application configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Review Sentiment Analysis",
    page_icon="💬",
    layout="centered",
)

st.title("💬 Customer Review Sentiment Analysis")

st.write(
    "Enter a product review to predict whether the sentiment "
    "is Positive, Neutral, or Negative."
)

st.caption("Group 4 | Mentor: Prajwal")


# --------------------------------------------------
# Locate the trained model
# --------------------------------------------------

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent

MODEL_PATH = PROJECT_DIR / "model" / "sentiment_model.pkl"


@st.cache_resource
def load_model(model_path):
    """Load the saved TF-IDF and Linear SVM pipeline."""
    return joblib.load(model_path)


if not MODEL_PATH.exists():
    st.error(
        "The trained model was not found. Expected location: "
        "model/sentiment_model.pkl"
    )
    st.info(
        "Run the model-training and saving cells in your notebook "
        "before starting the application."
    )
    st.stop()

try:
    model = load_model(str(MODEL_PATH))
except Exception as exc:
    st.error(
        "The model could not be loaded. Check that it was saved "
        "correctly and that the scikit-learn versions are compatible."
    )
    st.exception(exc)
    st.stop()


# --------------------------------------------------
# Review input
# --------------------------------------------------

review_text = st.text_area(
    "Enter customer review",
    placeholder=(
        "Example: The product quality is excellent "
        "and I am very happy with my purchase."
    ),
    height=160,
    max_chars=10000,
)

predict_button = st.button(
    "Analyze Sentiment",
    type="primary",
    use_container_width=True,
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:
    if not review_text.strip():
        st.warning("Please enter a review before predicting.")

    else:
        try:
            prediction = str(model.predict([review_text.strip()])[0])
            sentiment = prediction.strip().lower()

            sentiment_labels = {
                "positive": "Positive",
                "neutral": "Neutral",
                "negative": "Negative",
            }

            display_label = sentiment_labels.get(
                sentiment, prediction.title()
            )

            st.subheader("Prediction Result")

            if sentiment == "positive":
                st.success(f"😊 Sentiment: {display_label}")

            elif sentiment == "negative":
                st.error(f"😞 Sentiment: {display_label}")

            elif sentiment == "neutral":
                st.info(f"😐 Sentiment: {display_label}")

            else:
                st.write(f"Sentiment: {display_label}")

            # LinearSVC generally does not provide predict_proba().
            # Only display probabilities if the loaded model supports them.
            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(
                    [review_text.strip()]
                )[0]

                st.subheader("Class probabilities")

                classes = model.classes_

                for class_name, probability in zip(
                    classes, probabilities
                ):
                    st.write(
                        f"{str(class_name).title()}: "
                        f"{probability:.1%}"
                    )

                st.caption(
                    "These are model probabilities, not a guarantee "
                    "that the prediction is correct."
                )

            else:
                st.caption(
                    "The selected Linear SVM does not provide "
                    "predict_proba() by default. No probability-based "
                    "confidence score is displayed."
                )

        except Exception as exc:
            st.error("An error occurred while predicting sentiment.")
            st.exception(exc)


# --------------------------------------------------
# Project information
# --------------------------------------------------

with st.expander("About this project"):
    st.write(
        "This application uses a TF-IDF text representation and "
        "a trained Linear Support Vector Machine (SVM) pipeline "
        "to classify customer reviews into sentiment categories."
    )

    st.write(
        "The training notebook derives sentiment labels from star "
        "ratings: 1–2 = Negative, 3 = Neutral, and 4–5 = Positive."
    )
