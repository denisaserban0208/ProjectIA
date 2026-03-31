# -------------------------------
# FILTRARE COMENTARII - PROIECT FINAL
# -------------------------------

import pandas as pd
import re
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# modele clasice
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# deep learning
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -------------------------------
# 1. INCARCARE DATE
# -------------------------------
df = pd.read_csv("comments.csv")

# -------------------------------
# 2. PREPROCESARE TEXT
# -------------------------------
def curata_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

df['text_clean'] = df['text'].apply(curata_text)

# -------------------------------
# 3. ETICHETE NUMERICE
# -------------------------------
df['label_num'] = df['label'].apply(lambda x: 1 if x == 'respins' else 0)
y = df['label_num']

# ===============================
# 🔵 MODELE CLASICE
# ===============================
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(df['text_clean'])

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# Logistic Regression
model_lr = LogisticRegression()
model_lr.fit(X_train2, y_train2)
y_pred_lr = model_lr.predict(X_test2)
acc_lr = accuracy_score(y_test2, y_pred_lr)

# Decision Tree
tree = DecisionTreeClassifier()
tree.fit(X_train2, y_train2)
y_pred_tree = tree.predict(X_test2)
acc_tree = accuracy_score(y_test2, y_pred_tree)

# ===============================
# 🔵 LSTM
# ===============================
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(df['text_clean'])

sequences = tokenizer.texts_to_sequences(df['text_clean'])

max_len = 20
X = pad_sequences(sequences, maxlen=max_len)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_lstm = Sequential()
model_lstm.add(Embedding(input_dim=5000, output_dim=64))
model_lstm.add(LSTM(64))
model_lstm.add(Dense(1, activation='sigmoid'))

model_lstm.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_lstm.fit(X_train, y_train, epochs=10, batch_size=4, verbose=1)

loss, acc_lstm = model_lstm.evaluate(X_test, y_test)

y_pred_prob = model_lstm.predict(X_test)
y_pred_lstm = (y_pred_prob > 0.5).astype(int)

# ===============================
# 🔵 ANN
# ===============================
model_ann = Sequential()
model_ann.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model_ann.add(Dense(32, activation='relu'))
model_ann.add(Dense(1, activation='sigmoid'))

model_ann.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model_ann.fit(X_train, y_train, epochs=5, batch_size=4, verbose=1)

loss_ann, acc_ann = model_ann.evaluate(X_test, y_test)

# ===============================
# 🔵 AFISARE REZULTATE
# ===============================

print("\n" + "="*30)
print("REZULTATE MODELE")
print("="*30)

rezultate = {
    "Model": ["Logistic Regression", "Decision Tree", "LSTM", "ANN"],
    "Accuracy": [acc_lr, acc_tree, acc_lstm, acc_ann]
}

df_rez = pd.DataFrame(rezultate)
print(df_rez)

# ===============================
# 🔵 GRAFIC COMPARATIE (fereastra separata)
# ===============================
plt.figure(figsize=(8,5))

plt.bar(df_rez["Model"], df_rez["Accuracy"])
plt.title("Comparatie modele AI")
plt.ylabel("Accuracy")
plt.xlabel("Model")

plt.show()

# ===============================
# 🔵 MATRICE CONFUZIE (LSTM)
# ===============================
cm = confusion_matrix(y_test, y_pred_lstm)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Acceptat', 'Respins'],
            yticklabels=['Acceptat', 'Respins'])
plt.title("Confusion Matrix LSTM")
plt.show()

# ===============================
# 🔵 TEST INTERACTIV
# ===============================
def filtreaza_comentariu(text):
    text = curata_text(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    pred = model_lstm.predict(padded)
    return "RESPINS" if pred[0][0] > 0.5 else "ACCEPTAT"

print("\nScrie comentarii (exit pentru stop):")

while True:
    user_input = input("Comentariu: ")
    if user_input.lower() == "exit":
        break
    print("Rezultat:", filtreaza_comentariu(user_input))