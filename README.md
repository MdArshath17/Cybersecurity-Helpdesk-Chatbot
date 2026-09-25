# Cybersecurity Helpdesk Chatbot

A simple NLP-based cybersecurity helpdesk chatbot developed using Python and Scikit-learn. The chatbot identifies common cybersecurity-related user queries and provides appropriate security guidance.

This project was developed as part of an Artificial Intelligence Internship project.

## Features

- NLP-based intent recognition
- TF-IDF text vectorization
- Cosine similarity for matching user queries
- Confidence threshold for unknown questions
- Cybersecurity-focused helpdesk responses
- Handles different ways of asking similar questions
- Rejects unrelated queries
- Command-line interface
- Optional debug mode for displaying detected intent and confidence score

## Cybersecurity Topics

The chatbot can provide basic guidance about:

- Strong passwords
- Password reset
- Phishing emails
- Suspicious links
- Malware
- Ransomware
- Compromised accounts
- Multi-factor authentication (MFA)
- VPN information
- VPN connection problems
- Antivirus software
- Wi-Fi security
- Security updates

## Technologies Used

- Python
- Scikit-learn
- JSON
- TF-IDF Vectorization
- Cosine Similarity

## Project Structure

```text
Cybersecurity-Helpdesk-Chatbot/
│
├── chatbot.py
├── intents.json
├── requirements.txt
└── README.md
```

## How It Works

1. Cybersecurity intents, patterns, and responses are stored in `intents.json`.
2. The chatbot loads the training patterns.
3. TF-IDF converts the text patterns into numerical vectors.
4. The user's message is converted using the same TF-IDF vectorizer.
5. Cosine similarity compares the user's message with known patterns.
6. The most similar intent is selected.
7. If the similarity score is below the confidence threshold, the chatbot returns an unknown-question response.
8. Otherwise, an appropriate cybersecurity response is displayed.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Cybersecurity-Helpdesk-Chatbot
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Example:

```text
You: I received a suspicious email

Bot: Phishing attempts often use urgent requests, suspicious links,
unexpected attachments, or impersonation. Verify the request through
a trusted channel before taking action.
```

Unknown questions are rejected:

```text
You: tell me how to cook pasta

Bot: I'm sorry, I don't understand that question. Please ask me about
passwords, phishing, malware, suspicious links, VPNs, MFA, or account security.
```

## NLP Technique

The chatbot uses `TfidfVectorizer` from Scikit-learn to convert text into numerical features.

Cosine similarity is then used to compare the user's query with the patterns stored in the cybersecurity intent dataset.

A confidence threshold helps prevent unrelated questions from being incorrectly classified as cybersecurity questions.

## Limitations

- The chatbot uses a small predefined cybersecurity dataset.
- It does not use a large language model or generative AI.
- It may misclassify questions that are significantly different from its training patterns.
- Responses provide general cybersecurity guidance and are not a replacement for an organization's security or incident-response team.

## Learning Outcomes

Through this project, I learned about:

- Natural Language Processing fundamentals
- TF-IDF text vectorization
- Cosine similarity
- Intent-based chatbot design
- JSON-based datasets
- Confidence thresholds
- Testing and improving text classification
- Applying NLP concepts to cybersecurity support

## Disclaimer

This chatbot is created for educational purposes. Its responses provide general cybersecurity awareness and should not be considered a substitute for professional security or incident-response guidance.