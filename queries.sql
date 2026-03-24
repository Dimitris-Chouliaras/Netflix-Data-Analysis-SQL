-- Τα 10 πιο πρόσφατα "δυνατά" περιεχόμενα
SELECT title, type, release_year, country 
FROM netflix_content 
WHERE release_year >= 2021 
ORDER BY release_year DESC 
LIMIT 10;

-- Πόσες ταινίες VS πόσες σειρές (Aggregation)
SELECT type, COUNT(*) as total_count 
FROM netflix_content 
GROUP BY type;

-- Αναζήτηση συγκεκριμένου περιεχομένου (Filtering)
SELECT title, director, release_year 
FROM netflix_content 
WHERE country LIKE '%Greece%';