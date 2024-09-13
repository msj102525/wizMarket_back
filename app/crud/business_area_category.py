import logging
from fastapi import HTTPException
import pymysql

from app.db.connect import (
    get_db_connection,
    close_connection,
    close_cursor,
    commit,
    rollback,
)


def get_all_detail_category_count() -> int:
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            select_query = """
            SELECT COUNT(BUSINESS_AREA_CATEGORY_ID) COUNT
            FROM BUSINESS_AREA_CATEGORY
            """
            cursor.execute(select_query)
            result = cursor.fetchone()

            # print(result)
            # print(result["COUNT"])
            return result["COUNT"]
    except Exception as e:
        print(f"get_all_detail_category_count Error: {e}")
        raise HTTPException(status_code=500, detail="Database query failed")
    finally:
        close_connection(connection)


if __name__ == "__main__":
    print(get_all_detail_category_count())
