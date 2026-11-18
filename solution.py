
%%writefile solution.py
import sqlite3
import csv

# Step 1: Connect to database
con = sqlite3.connect("week01_ledger.sqlite")

# Step 2: Create table
con.execute("DROP TABLE IF EXISTS events")

con.execute("""
CREATE TABLE events (
    seq INTEGER PRIMARY KEY,
    event TEXT NOT NULL,
    approved_by TEXT NOT NULL
)
""")

# Step 3: Insert four records
records = [
    ('Issue certificate C-001', 'Registrar'),
    ('Issue certificate C-002', 'Registrar'),
    ('Revoke certificate C-001', 'Registrar'),
    ('Issue certificate C-003', 'Registrar')
]

con.executemany(
    'INSERT INTO events(event, approved_by) VALUES(?, ?)',
    records
)
con.commit()

# Step 4: Retrieve records
rows = con.execute(
    'SELECT seq, event, approved_by FROM events ORDER BY seq'
).fetchall()

print("CENTRAL DATABASE:")
for record in rows:
    print(record)

# Step 5: Create two copies
registrar_copy = list(rows)
employer_copy = list(rows)

# Step 6: Change second record in Employer copy
employer_copy[1] = (
    employer_copy[1][0],
    'Issue certificate C-999',
    employer_copy[1][2]
)

# Step 7: Detect conflict
print("\nSHARED-COPY EXPERIMENT:")

for a, b in zip(registrar_copy, employer_copy):
    if a != b:
        print("CONFLICT DETECTED:", a, "versus", b)

# Step 8: Export to CSV
with open("week01_ledger.csv", "w", newline="") as output:
    w = csv.writer(output)
    w.writerow(["seq", "event", "approved_by"])
    w.writerows(rows)

# Step 9: Verify records
assert len(rows) == 4

print("\nTotal records:", len(rows))
print("PASS: All four records are present.")

con.close()
