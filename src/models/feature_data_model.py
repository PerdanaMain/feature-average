from utils.database import *


def get_features_value(part_id):
    conn = None
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = """
        SELECT id, value, date_time as datetime, part_id
        FROM dl_features_data 
        WHERE part_id = %s 
        ORDER BY date_time ASC
        """
        cur.execute(query, (part_id,))
        parts = cur.fetchall()
        return parts
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()
