#  Filtrarea comentariilor intr-o aplicatie de tip booksharing

##  1. Introducere

In cadrul aplicatiilor moderne de tip booksharing, utilizatorii pot publica recenzii si comentarii despre carti. Aceste platforme trebuie sa gestioneze continutul generat de utilizatori, prevenind aparitia limbajului ofensator sau toxic.

Scopul acestui proiect este dezvoltarea unui sistem inteligent capabil sa clasifice automat comentariile in doua categorii:

* **acceptat** (continut adecvat)
* **respins** (continut toxic sau ofensator)

Pentru aceasta problema, au fost utilizate tehnici din domeniul Inteligentei Artificiale, in special procesarea limbajului natural (NLP) si invatarea automata.

---

##  2. Fundamente teoretice

### 🔹 Procesarea limbajului natural (NLP)

NLP (Natural Language Processing) este un subdomeniu al Inteligentei Artificiale care se ocupa cu analiza si intelegerea textului uman. In acest proiect, NLP este folosit pentru:

* curatarea textului
* transformarea cuvintelor in reprezentari numerice
* clasificarea automata a comentariilor

---

### 🔹 Reprezentarea textului

Pentru a putea utiliza algoritmi de invatare automata, textul trebuie transformat in vectori numerici:

* **TF-IDF (Term Frequency - Inverse Document Frequency)**
  Metoda statistica care evalueaza importanta unui cuvant intr-un document.

* **Tokenizare + Padding**
  Transformarea textului in secvente de numere si aducerea lor la aceeasi lungime pentru retele neuronale.

---

### 🔹 Modele utilizate

#### 1. Logistic Regression

* model clasic de clasificare liniara
* eficient pentru probleme simple de text

#### 2. Decision Tree

* model bazat pe reguli
* interpretabile dar pot supra-invata datele

#### 3. ANN (Artificial Neural Network)

* retea neuronala simpla (feedforward)
* invata relatii non-lineare

#### 4. LSTM (Long Short-Term Memory)

* tip de retea neuronala recurenta
* capabila sa inteleaga dependentele dintre cuvinte
* potrivita pentru procesarea textului

---

##  3. Arhitectura aplicatiei

Aplicatia este structurata in mai multe etape:

1. **Incarcarea datelor**

   * citirea datasetului CSV

2. **Preprocesare**

   * transformare in lowercase
   * eliminare punctuatie

3. **Vectorizare**

   * TF-IDF pentru modelele clasice
   * Tokenizare pentru LSTM si ANN

4. **Antrenare modele**

   * Logistic Regression
   * Decision Tree
   * ANN
   * LSTM

5. **Evaluare**

   * accuracy
   * classification report
   * matrice de confuzie

6. **Testare interactiva**

   * utilizatorul introduce comentarii
   * sistemul returneaza clasificarea

---

##  4. Dataset

Datasetul utilizat a fost creat manual si contine comentarii despre carti, etichetate in doua categorii:

* acceptat
* respins

Caracteristici:

* ~200-300 exemple
* echilibrat intre clase
* include variatii de limbaj (pozitiv, negativ, toxic)

Motivatie:
Dataseturile existente nu reflecta exact contextul aplicatiilor de tip booksharing, motiv pentru care a fost construit un dataset personalizat.

---

##  5. Implementare

Proiectul a fost implementat in Python folosind urmatoarele biblioteci:

* pandas (manipulare date)
* scikit-learn (modele clasice)
* tensorflow / keras (retele neuronale)
* matplotlib & seaborn (vizualizare)

Etapele principale:

* curatarea textului
* transformarea in vectori
* antrenarea modelelor
* compararea performantelor

---

##  6. Rezultate si interpretare

Performanta modelelor a fost evaluata folosind accuracy si matricea de confuzie.

Observatii:

* modelele clasice sunt rapide si eficiente pentru date mici
* LSTM ofera rezultate mai bune pentru intelegerea contextului
* ANN ofera performanta intermediara

Matricea de confuzie arata:

* cate comentarii sunt clasificate corect
* unde apar erori (ex: comentarii toxice acceptate)

Cea mai importanta eroare este clasificarea comentariilor toxice ca fiind acceptate.

---

##  7. Concluzii

Acest proiect demonstreaza utilizarea tehnicilor de Inteligenta Artificiala pentru filtrarea automata a comentariilor.

Avantaje:

* automatizarea moderarii continutului
* reducerea interventiei umane
* aplicabilitate reala in platforme online

Limitari:

* dataset relativ mic
* dificultate in detectarea nuantelor limbajului

---

##  8. Posibile imbunatatiri

* utilizarea unui dataset mai mare
* folosirea modelelor moderne (BERT, transformers)
* detectarea sarcasmului
* integrarea intr-o aplicatie web

---

##  9. Bibliografie

1. Jurafsky, D., & Martin, J. H. – *Speech and Language Processing*
2. Goodfellow, I., Bengio, Y., Courville, A. – *Deep Learning*
3. Documentatia oficiala Scikit-learn – https://scikit-learn.org
4. Documentatia TensorFlow – https://www.tensorflow.org
5. Kaggle – https://www.kaggle.com
6. Manning, C. D. – *Foundations of Statistical Natural Language Processing*

---


![image alt](https://github.com/denisaserban0208/ProjectIA/blob/ca6c8284924e4334493286f434fbbbc04e95e04e/Screenshot%202026-03-31%20123346.png)

![image alt](https://github.com/denisaserban0208/ProjectIA/blob/0c163a9b142eb0a35cdcae27c3492070d1d0b0b2/Screenshot%202026-03-31%20123401.png)
