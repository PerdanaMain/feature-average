from utils.database import *


def get_parts():
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = "SELECT id, part_name FROM pf_parts"
        cur.execute(query)
        parts = cur.fetchall()
        return parts
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()


def get_part(part_id):
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = "SELECT id, part_name FROM pf_parts WHERE id = %s "
        cur.execute(query, (part_id,))
        part = cur.fetchone()
        return part
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()
