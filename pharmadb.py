import sqlite3
con=sqlite3.connect("PHARMA.db")
cur=con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS MEDICINES(
    id integer primary key,
    name text,
    batch_no text,
    category text,
    expiry_date date,
    price real,
    quantity integer)''')

def add_medicine(id, name, batch_no, category, expiry_date, price, quantity):
    try:
        if price < 0 or quantity <0:
            raise ValueError("Price and Quantity must be non-negative")
        cur.execute('''INSERT INTO MEDICINES (id, name, batch_no, category, expiry_date, price, quantity)
                    VALUES(?,?,?,?,?,?,?)''', (id, name, batch_no, category, expiry_date, price, quantity))
        con.commit()
        print("Medicine added successfully")
    except ValueError as ve:
        print("Validation error: ",ve)    
    except Exception as e:
        print("Error: ", e)
        
def view_inventory():
    try:
        cur.execute("select * from MEDICINES")
        rows=cur.fetchall()
        print("ID | Name         | Batch No | Category | Expiry Date | Price  | Quantity")
        print("-" * 70)
        for row in rows:
            print(f"{row[0]:<3}| {row[1]:<12}| {row[2]:<9}| {row[3]:<9}| {row[4]:<11}| {row[5]:<6}| {row[6]}")
    except Exception as e:
        print("Error: ", e)
        
def update_medicine(id,field, new_value):
    try:
        cur.execute(f"UPDATE MEDICINES SET {field} = ? WHERE id = ?", (new_value,id))
        con.commit()
    except Exception as e:
        print("Error: ", e)
        
def delete_medicine(id):
    try:
        cur.execute("DELETE FROM MEDICINES WHERE id = ?",(id))
        con.commit()
        print(f"Medicine with ID {id} deleted successfully!")
    except Exception as e:
        print("Error: ", e)
add_medicine(1, "Paracetamol", "PCT202501", "Tablet", "2025-01-15", 12.50, 100)
view_inventory()

