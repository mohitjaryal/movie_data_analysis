# 🎬 Movie Data Analysis using Pandas & NumPy

## 📖 Overview
This project analyzes **The Movie Database (TMDB)** dataset from Kaggle to explore insights about movie ratings, revenue, and trends.  
The goal of this project is to practice **data cleaning, exploration, and numerical analysis** using **Pandas** and **NumPy** in Python.

---

## 🧠 Skills Practiced
- Python data manipulation with **Pandas**
- Numerical computation with **NumPy**
- Handling missing data
- Data filtering, grouping, and sorting
- Extracting insights from real-world datasets

---

## 🗂️ Dataset
**Source:** [TMDB 5000 Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
The dataset contains metadata for over 5,000 movies, including:

- 🎞️ `title`
- 📅 `release_date`
- 💰 `budget` and `revenue`
- ⭐ `vote_average` and `vote_count`
- 🎭 `genres`, `production_companies`, etc.

---
## 🚀 Steps Performed

### **1️⃣ Data Loading & Exploration**
- Loaded dataset using Pandas  
- Displayed first 10 rows, column names, and data types  
- Checked missing values and summary statistics  

### **2️⃣ Data Cleaning**
- Converted `release_date` to datetime format  
- Filled or dropped missing values in numeric columns like `budget`, `revenue`, `vote_average`, and `vote_count`  
- Created `release_year` column from `release_date`  

### **3️⃣ Analysis**
- Found **Top 10 Highest-Grossing Movies**  
- Found **Top 10 Highest-Rated Movies** (with a minimum vote count filter)  
- Filtered **Movies Released After 2010**

### **4️⃣ Data Visulization**
- Added visualizations using Matplotlib and Seaborn
- Performed genre-wise analysis of revenue and ratings
- Explored correlations between budget, revenue, and ratings
- Built simple machine learning models to predict movie success


### **5️⃣ NumPy Practice**
- Converted numeric columns (`revenue`, `budget`, etc.) to NumPy arrays  
- Calculated mean, median, standard deviation, min, and max values  
- Computed `profit = revenue - budget`  
- Calculated percentage of profitable movies  

---

## 📊 Tools & Libraries Used
- 🐍 Python 3  
- 🧩 Pandas  
- 🔢 NumPy  

---

## 💡 Key Insights
- Highest-grossing movies are large franchise blockbusters (e.g., Avatar, Jurassic World).  
- Average movie rating lies between **6 and 7** for most movies.  
- The number of movies released increased significantly after 2000.  

---

## 📁 How to Run This Project
```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/movie_data_analysis.git
cd movie_data_analysis

# 2. Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn

# 4. Run the script
python3 scripts/main.py
```

## Mohit Jaryal
🌐 Learn more and contact me : [mohitjaryal.online](https://mohitjaryal.online)
