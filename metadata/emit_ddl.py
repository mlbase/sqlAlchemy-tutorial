from metadata_table import metadata_obj
from connection.engine_config import engine

'''injecting dependency(engine) for making ddl'''
metadata_obj.create_all(engine)
