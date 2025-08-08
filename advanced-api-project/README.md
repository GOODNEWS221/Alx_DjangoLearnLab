## 🔎 API Query Features

### ✅ Filtering
Filter books by exact matches on:
- `title`
- `author`
- `publication_year`

**Example:**  
`/api/books/?title=Python`

### 🔍 Searching
Search (case-insensitive, partial match) on:
- `title`
- `author`

**Example:**  
`/api/books/?search=django`

### ↕️ Ordering
Sort results by:
- `title`
- `publication_year`

**Example:**  
`/api/books/?ordering=-publication_year`


