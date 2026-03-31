Proiect AI: Sistem de Filtrare Automată a Comentariilor
 
 Descriere Generală
Acest proiect are ca scop clasificarea automată a comentariilor în două categorii: Acceptat (0) și Respins (1). Aplicația utilizează atât algoritmi de Machine Learning clasici, cât și arhitecturi de Deep Learning pentru a compara eficiența acestora în procesarea limbajului natural (NLP).

 1. Fundamente Teoretice
Procesarea Limbajului Natural (NLP)
Pentru ca un computer să înțeleagă textul, acesta trebuie convertit în numere. Proiectul utilizează două abordări:

TF-IDF (Term Frequency-Inverse Document Frequency): O metodă statistică ce măsoară importanța unui cuvânt în raport cu un document și cu întregul set de date.

Word Embeddings: O tehnică modernă unde cuvintele sunt reprezentate ca vectori densi într-un spațiu multidimensional, păstrând relațiile semantice între ele.

Algoritmi Utilizați
Logistic Regression: Un model liniar robust pentru clasificare binară.

Decision Tree: Un model bazat pe structuri arborescente care împarte datele în funcție de caracteristicile cele mai relevante.

ANN (Artificial Neural Network): O rețea neuronală densă care învață tipare complexe prin straturi de neuroni (Dense Layers).

LSTM (Long Short-Term Memory): Un tip special de rețea neuronală recurentă (RNN) capabilă să rețină contextul și ordinea cuvintelor dintr-o propoziție.

 2. Organizarea Arhitecturală a Aplicației
Aplicația este dezvoltată în Python și urmează următorii pași logici:

Preprocesare (Curățare): Textul este transformat în litere mici și semnele de punctuație sunt eliminate folosind expresii regulate (re).

Vectorizare/Tokenizare:

Pentru modelele clasice: Se folosește TfidfVectorizer.

Pentru modelele Deep Learning: Se folosește Tokenizer cu o limită de 5000 de cuvinte și pad_sequences pentru a aduce toate comentariile la o lungime fixă de 20 de cuvinte.

Antrenare: Datele sunt împărțite în set de antrenare (80%) și set de test (20%). Modelele sunt antrenate pentru a minimiza eroarea de clasificare.

Evaluare: Se calculează acuratețea și se generează o matrice de confuzie pentru a vedea erorile de tip "False Positive" sau "False Negative".

 3. Date de Test și Interpretarea Rezultatelor
Datele utilizate
Proiectul folosește un set de date de tip CSV (comments.csv) care conține:

Coloana text: Mesajele scrise de utilizatori.

Coloana label: Eticheta manuală (Acceptat/Respins).

Rezultate (Exemplu de interpretare)
În urma rulării, aplicația compară performanța modelelor:

Acuratețea: Reprezintă procentul de comentarii clasificate corect din totalul testelor.

Matricea de Confuzie (LSTM): Arată exact câte comentarii "Acceptate" au fost greșit catalogate ca "Respinse" și invers.

Graficul de Bare: Oferă o imagine comparativă rapidă, evidențiind dacă modelele complexe (LSTM) depășesc modelele simple (Logistic Regression).

 4. Mod de Utilizare
Modul Interactiv
După antrenare, utilizatorul poate introduce text direct în consolă pentru a primi un verdict instant din partea modelului LSTM:

Intrare: "Ești un prost" -> Ieșire: RESPINS

Intrare: "Bună ziua, mulțumesc pentru ajutor" -> Ieșire: ACCEPTAT

 5. Referințe Utilizate
Scikit-Learn Documentation: Pentru implementarea Logistic Regression și Decision Tree.

TensorFlow/Keras: Pentru arhitecturile de rețele neuronale și procesarea secvențelor.

Pandas & NumPy: Pentru manipularea structurilor de date.

Matplotlib & Seaborn: Pentru vizualizarea grafică a performanței.
