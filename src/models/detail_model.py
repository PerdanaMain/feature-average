from utils.database import *
from utils.logger import logger
import uuid


def get_detail(part_id):
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = "SELECT * FROM pf_details WHERE part_id = %s"
        cur.execute(query, (part_id,))
        details = cur.fetchone()
        return details
    except Exception as e:
        print(f"An exception occurred: {e}")
        logger.error(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()


def create_detail(
    part_id,
    upper_threshold,
    lower_threshold,
    one_hundred_percent_condition,
    predict_value=None,
    time_failure=None,
    predict_status=None,
    percent_condition=None,
):
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        detail_id = str(uuid.uuid4())

        query = "INSERT INTO pf_details (id, part_id, upper_threshold, lower_threshold, one_hundred_percent_condition, predict_value, time_failure, predict_status, percent_condition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(
            query,
            (
                detail_id,
                part_id,
                upper_threshold,
                lower_threshold,
                one_hundred_percent_condition,
                predict_value,
                time_failure,
                predict_status,
                percent_condition,
            ),
        )
        conn.commit()
        return detail_id
    except Exception as e:
        print(f"An exception occurred: {e}")
        logger.error(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()


def update_detail(
    part_id, upper_threshold, lower_threshold, one_hundred_percent_condition
):
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = "UPDATE pf_details SET upper_threshold = %s, lower_threshold = %s, one_hundred_percent_condition = %s WHERE part_id = %s"
        cur.execute(
            query,
            (upper_threshold, lower_threshold, one_hundred_percent_condition, part_id),
        )
        conn.commit()
    except Exception as e:
        print(f"An exception occurred: {e}")
        logger.error(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()


def update_one_percent_condition(part_id, one_percent_condition):
    try:
        conn = get_main_connection()
        cur = conn.cursor()

        query = "UPDATE pf_details SET one_hundred_percent_condition = %s WHERE part_id = %s"
        cur.execute(query, (one_percent_condition, part_id))
        conn.commit()
    except Exception as e:
        print(f"An exception occurred: {e}")
        logger.error(f"An exception occurred: {e}")
    finally:
        if conn:
            conn.close()
