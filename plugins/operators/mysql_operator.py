from sqlalchemy import create_engine

def load_mysql_table(df, table_name, mode, engine_url):
    engine = create_engine(engine_url)
    if mode == "truncate":
        with engine.begin() as conn:
            conn.execute(f"TRUNCATE TABLE {table_name}")
            df.to_sql(table_name, engine, if_exists="append", index=False)
