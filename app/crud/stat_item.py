import pymysql
from app.db.connect import (
    get_db_connection,
    close_connection,
    close_cursor,
    commit,
    rollback,
)
from app.schemas.biz_detail_category import BizDetailCategoryId
from app.schemas.stat_item import StatItemInfo


# stat_item 테이블에 데이터 삽입
def insert_stat_item(table_name, column_name, reference_id):
    connection = None
    cursor = None
    try:
        # DB 연결
        connection = get_db_connection()
        cursor = connection.cursor()

        # stat_item 테이블에 데이터 삽입하는 SQL 쿼리 작성
        insert_query = """
            INSERT INTO stat_item (table_name, column_name, REFERENCE_ID)
            VALUES (%s, %s, %s)
        """

        # 데이터 삽입
        cursor.execute(insert_query, (table_name, column_name, reference_id))

        # 커밋
        commit(connection)

        print(
            f"Data inserted successfully into stat_item with table_name={table_name}, column_name={column_name}, reference_id={reference_id}"
        )

    except Exception as e:
        print(f"Error inserting into stat_item: {e}")
        # 문제가 생기면 롤백
        rollback(connection)

    finally:
        # 커서와 연결 종료
        close_cursor(cursor)
        close_connection(connection)


def insert_stat_item_add_detail_category(
    table_name, column_name, reference_id, search_detail_category_id
):
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        # stat_item 테이블에 데이터 삽입하는 SQL 쿼리 작성
        insert_query = """
            INSERT INTO stat_item (table_name, column_name, REFERENCE_ID, detail_category_id)
            VALUES (%s, %s, %s, %s)
        """

        # 데이터 삽입
        for detail_category_id in search_detail_category_id:
            cursor.execute(
                insert_query,
                (table_name, column_name, reference_id, detail_category_id),
            )

        # 커밋
        commit(connection)

        # print(
        #     f"stat_item: table_name={table_name}, column_name={column_name}, reference_id={reference_id}, detail_category_id={detail_category_id}"
        # )

    except Exception as e:
        print(f"Error inserting into stat_item: {e}")
        rollback(connection)

    finally:
        close_cursor(cursor)
        close_connection(connection)


def select_detail_category_id_by_stat_item_id(stat_item_id) -> BizDetailCategoryId:
    # DB 연결
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:

        # stat_item 테이블에 데이터 삽입하는 SQL 쿼리 작성
        select_query = """
            SELECT
                DETAIL_CATEGORY_ID
            FROM
                STAT_ITEM
            WHERE STAT_ITEM_ID = %s
        """

        return cursor.execute(select_query, (stat_item_id,))

    except Exception as e:
        print(f"Error inserting into stat_item: {e}")
        rollback(connection)

    finally:
        close_cursor(cursor)
        close_connection(connection)


def select_stat_item_info_by_stat_item_id(stat_item_id) -> StatItemInfo:
    # DB 연결
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        # stat_item 테이블에서 데이터 조회하는 SQL 쿼리 작성
        select_query = """
            SELECT
                TABLE_NAME,
                COLUMN_NAME,
                DETAIL_CATEGORY_ID
            FROM
                STAT_ITEM
            WHERE STAT_ITEM_ID = %s
        """
        cursor.execute(select_query, (stat_item_id,))
        row = cursor.fetchone()  # Fetch the result

        if row:  # Check if row is not None
            return StatItemInfo(
                table_name=row["TABLE_NAME"],
                column_name=row["COLUMN_NAME"],
                biz_detail_category_id=row["DETAIL_CATEGORY_ID"],
            )
        else:
            # Handle the case where no result is found
            return StatItemInfo(table_name="", column_name="", biz_detail_category_id=0)

    except Exception as e:
        print(f"Error selecting from stat_item: {e}")
        connection.rollback()  # Rollback if there's an error
        raise  # Re-raise the exception after rollback

    finally:
        close_cursor(cursor)
        close_connection(connection)
