
1. **Algorithms Used:**
   - **Multinomial Naive Bayes:** Ideal for discrete features (like word counts in text).
   - **Bernoulli Naive Bayes:** Works well when features are binary or boolean.

2. **Performance Insights:**
   - **Multinomial Naive Bayes:**
     - Training score: 0.97
   - **Bernoulli Naive Bayes:**
     - Training score: 0.96
     - Testing score: 0.95

3. **Why It Matters:**
   Proper email categorization streamlines communication, reduces spam, and ensures critical messages aren't overlooked.

4. **Tech Stack:**
   - Python (NumPy, Pandas, Sklearn)
   - Data preprocessing with Pandas
   - Text processing using regular expressions
   - Feature extraction with CountVectorizer and TfidfVectorizer
   - Sklearn's Naive Bayes classifiers

5. **Visualizations and Deployment:**
   - Seaborn and Matplotlib for insightful visualizations
   - Joblib for model deployment
