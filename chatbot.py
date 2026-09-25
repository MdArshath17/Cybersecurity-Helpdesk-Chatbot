import json
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DEBUG = False


# Load dataset
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# Prepare patterns and tags
patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])


# Create TF-IDF model
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

pattern_vectors = vectorizer.fit_transform(patterns)


# Get chatbot response
def get_response(user_message):

    user_vector = vectorizer.transform([user_message])

    similarities = cosine_similarity(
        user_vector,
        pattern_vectors
    )[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    predicted_tag = tags[best_match_index]

    # Reject unrelated questions
    if best_score < 0.35:
        return (
            "unknown",
            best_score,
            "I'm sorry, I don't understand that question. "
            "Please ask me about passwords, phishing, malware, "
            "suspicious links, VPNs, MFA, or account security."
        )

    # Find response
    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            response = random.choice(intent["responses"])

            return (
                predicted_tag,
                best_score,
                response
            )

    return (
        "unknown",
        0.0,
        "I'm sorry, I couldn't find an answer."
    )


# Main program
def main():

    print("=" * 55)
    print("          CYBERSECURITY HELPDESK CHATBOT")
    print("=" * 55)

    print("\nBot: Hello! I can help you with basic cybersecurity questions.")

    print(
        "Bot: Ask me about passwords, phishing, malware, "
        "VPNs, suspicious links, or MFA."
    )

    print("Bot: Type 'exit' to close the chatbot.")

    while True:

        user_message = input("\nYou: ").strip()

        if not user_message:
            print("Bot: Please enter a question.")
            continue

        if user_message.lower() in [
            "exit",
            "quit",
            "bye",
            "goodbye"
        ]:
            print("\nBot: Goodbye! Stay safe online.")
            break

        intent, confidence, response = get_response(
            user_message
        )

        print("Bot:", response)

if DEBUG:
    print(
        f"[Intent: {intent} | "
        f"Confidence: {confidence:.2f}]"
    )


if __name__ == "__main__":
    main()