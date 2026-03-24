import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# --- ΦΑΣΗ 1: EXTRACT & LOAD (Μεταφορά στη Βάση) ---
print("Φόρτωση δεδομένων και δημιουργία SQL βάσης...")
df = pd.read_csv('netflix_titles.csv')

# Σύνδεση με την SQLite (θα δημιουργήσει το αρχείο netflix.db αυτόματα)
conn = sqlite3.connect('netflix.db')

# Μετατροπή του DataFrame σε SQL Πίνακα
df.to_sql('netflix_content', conn, if_exists='replace', index=False)

# --- ΦΑΣΗ 2: TRANSFORM & QUERY (Χρήση SQL) ---
print("Εκτέλεση SQL Queries για ανάλυση...")

# Παράδειγμα SQL Query: Πόσες ταινίες vs σειρές
query_type = "SELECT type, COUNT(*) as total FROM netflix_content GROUP BY type"
res_type = pd.read_sql(query_type, conn)

# Παράδειγμα SQL Query: Top 10 Χώρες
query_country = """
SELECT country, COUNT(*) as count 
FROM netflix_content 
WHERE country IS NOT NULL 
GROUP BY country 
ORDER BY count DESC 
LIMIT 10
"""
res_country = pd.read_sql(query_country, conn)

# --- ΦΑΣΗ 3: VISUALIZE (Γραφήματα) ---
print("Δημιουργία γραφημάτων...")

# Γράφημα 1: Movies vs TV Shows
plt.figure(figsize=(8,6))
plt.pie(res_type['total'], labels=res_type['type'], autopct='%1.1f%%', colors=['#E50914', '#221F1F'])
plt.title('Netflix Content Ratio (SQL Query Result)')
plt.savefig('content_ratio.png')
plt.close()

# Γράφημα 2: Top 10 Χώρες
plt.figure(figsize=(10,6))
sns.barplot(x='count', y='country', data=res_country, palette='Reds_r')
plt.title('Top 10 Countries by Content (SQL Query Result)')
plt.savefig('top_countries.png')
plt.close()

# Κλείσιμο σύνδεσης
conn.close()
print("Το project ολοκληρώθηκε! Τα αρχεία netflix.db και οι εικόνες δημιουργήθηκαν.")