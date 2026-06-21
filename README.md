# Smart Query Builder

## Overview

Convert simple English database queries into SQL automatically.

---

## Files

- query_parser.py
- sql_generator.py

---

## Run

```bash
python sql_generator.py
```

---

## Examples

Input:

```text
Show all students with CPI > 8
```

Output:

```sql
SELECT *
FROM students
WHERE cpi > 8;
```

---

Input:

```text
Find top 5 employees by salary
```

Output:

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

---

Input:

```text
Count students
```

Output:

```sql
SELECT COUNT(*)
FROM students;
```

---

Generated File

```text
query.sql
```

---

Future Improvements

- JOIN Queries
- GROUP BY
- PostgreSQL Support
- MySQL Support
- Natural Language AI Parsing
- Query Execution