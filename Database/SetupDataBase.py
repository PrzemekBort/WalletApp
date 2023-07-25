import sqlite3 as sql


if __name__ == "__main__":
    conn = sql.connect('WalletApp.db', 5)

    with open('CreatePassTable.sql') as script:
        conn.executescript(script.read())

    with open('CreateAssetsTable.sql') as script:
        conn.executescript(script.read())

    conn.commit()
