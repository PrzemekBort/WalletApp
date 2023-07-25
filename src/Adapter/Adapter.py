import os
import sqlite3 as sql


class Adapter:

    def __init__(self, databasePath):
        self.databasePath = databasePath
        self.connection = self._connect()

    def _connect(self):
        """
        Create a database connection to the SQLite database
        specified by the databasePath
            :return: Connection object or None
        """
        if os.path.exists(self.databasePath):
            try:
                conn = sql.connect(self.databasePath)
                return conn
            except sql.OperationalError:
                print('Database connection error.')
                return None
        else:
            print('Database file not found.')
            return None

    def select(self, assetID):
        """
        Takes data from row where Asset_ID == assetID
        :param assetID: unique asset ID
        :return: one row from Assets table or None
        """
        if self.connection is not None:
            cur = self.connection.cursor()
            cur.execute(
                f"""
                SELECT * FROM Assets
                WHERE Asset_ID = {assetID}
                """)
            row = cur.fetchall()
            return row
        else:
            return None

    def selectAll(self):
        """
        Takes all rows from Assets table
        :return: all rows from Assets table or None
        """
        if self.connection is not None:
            cur = self.connection.cursor()
            cur.execute('SELECT * FROM Assets')
            rows = cur.fetchall()
            return rows
        else:
            return None

    def insert(self, assetDataDict):
        asset = assetDataDict
        if self.connection is not None:
            cur = self.connection.cursor()
            cur.execute(
                f"""
                INSERT INTO Assets
                VALUES ({asset['Asset_ID']}, {asset['AssetType']}, {asset['Name']}, {asset['Quantity']}
                {asset['BuyPrice']}, {asset['BuyDate']})
                """)
