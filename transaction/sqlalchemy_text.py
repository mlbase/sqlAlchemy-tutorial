######## pip dependencies #####
from sqlalchemy import text

######### connection ########
from connection.engine_config import engine

#
# 이 파일은 sqlalchemy 의 text 를 활용한 statement transation을 구현하는 code입니다


with engine.connect() as conn:

    '''create table'''
    # conn.execute(
    #     text("CREATE TABLE user_table (name varchar(100), fullname varchar(100))")
    # )

    '''insert table'''
    # conn.execute(
    #     text("INSERT INTO some_table (x, y) values (:x, :y)"),
    #     [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    # )

    '''drop table'''
    # conn.execute(
    #     text("DROP TABLE some_table")
    # )

    '''update  table'''
    # conn.execute(
    #     text("UPDATE some_table SET y= 37 WHERE x= 6")
    # )

    '''조건주어검색'''
    # result = conn.execute(
    #     text("SELECT x, y FROM some_table WHERE y > :y"),
    #     {"y": 11}
    # )

    # result = (conn.execute(
    #     text("SELECT * FROM some_table")
    # ))

    '''select via statement when multiple row'''
    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=13)
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

    # print(result.all())

    '''create delete update 이후 바로 select를 하면 commit이 된다'''
    # conn.commit()
