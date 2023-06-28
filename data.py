import sqlite3

db_path = 'bangtan.db'

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_mems_by_mem_type(bang_mem):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM membio WHERE line_type = ?'
    value = (bang_mem,)  # Wrap the value in a tuple
    cur.execute(query, value)  # Pass the tuple directly as the second argument
    results = cur.fetchall()  # Use fetchall() instead of fetchone()
    conn.close()
    return results

def read_bangmems_by_bangmem_id(bangmem_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM membio WHERE id = ?'
    value = bangmem_id
    result = cur.execute(query, (value,)).fetchone()
    conn.close()
    return result

def insert_mem(mem_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO membio (fname, sname, bdate, pbirth, position, picurl, line_type) VALUES (?,?,?,?,?,?,?)'
    values = (mem_data['fname'], mem_data['sname'], mem_data['bdate'], mem_data['pbirth'], mem_data['position'], mem_data['picurl'], mem_data['line_type'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def update_mem(mem_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE membio SET fname=?, sname=?, bdate=?, pbirth=?, position=?, picurl=?, line_type=? WHERE id=?"
    values = (mem_data['fname'], mem_data['sname'], mem_data['bdate'], mem_data['pbirth'], mem_data['position'], mem_data['picurl'], mem_data['line_type'], mem_data['bangmem_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_mem(bangmem_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM membio WHERE id = ?"
    values = (bangmem_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()