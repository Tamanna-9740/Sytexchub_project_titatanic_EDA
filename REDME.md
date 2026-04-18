# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to understand patterns affecting passenger survival.

The analysis includes:

* Data inspection (missing values & data types)
* Survival analysis by gender, class, and age groups
* Data visualization using statistical plots
* Key insights derived from the dataset

---

## 📊 Dataset

* Source: Kaggle Titanic Dataset
* Rows: ~891 passengers
* Features include:

  * Survival (0 = No, 1 = Yes)
  * Passenger Class
  * Sex
  * Age
  * Fare
  * Embarked location

---

## 🔍 Data Inspection

### Data Types & Structure

```python
df.info()
```

### Missing Values Analysis

```python
df.isnull().sum()
```

#### Key Findings:

* `deck` → High missing values (dropped)
* `age` → Moderate missing values (imputed)
* `embarked` → Few missing values (filled with mode)

---

## 📈 Exploratory Data Analysis

### Survival by Gender

* Females had significantly higher survival rates than males

### Survival by Passenger Class

* First-class passengers had the highest survival rate

### Survival by Age Group

* Children had higher survival probability compared to adults

---

## 📊 Visualizations

| Plot              | Description                       |
| ----------------- | --------------------------------- |
| Survival by Sex   | Gender-wise survival comparison   |
| Survival by Class | Class-based survival distribution |
| Age Distribution  | Age variation across survival     |

---

## 🧠 Key Insights

* Women and children were prioritized during evacuation
* Higher-class passengers had better survival chances
* Socioeconomic status played a major role in survival
* Missing data (especially age) impacts analysis accuracy

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
```

Run notebook:

```bash
jupyter notebook notebooks/titanic_eda.ipynb
```

---

## 📌 Conclusion

The analysis highlights strong correlations between survival and gender, class, and age. These insights demonstrate how data analysis can uncover meaningful patterns in real-world datasets.

---

## 🔗 Author

**Tamanna Akter**
Data Science Intern
Syntecxhub Internship Program
