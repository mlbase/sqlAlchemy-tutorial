from sqlalchemy import text
from sqlalchemy.orm import Session
from connection.engine_config import engine

with Session(engine) as session:

    '''transaction with session'''
    # stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=1)
    # result = session.execute(stmt)
    #
    # for row in result:
    #     print(f"x: {row.x} y: {row.y}")

    '''transaction with session with commit'''
    # result2 = session.execute(
    #     text("UPDATE some_table SET y=:y WHERE x=:x"),
    #     [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
    # )
    # print(result2)
    session.commit()

