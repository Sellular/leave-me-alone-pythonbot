import sqlite3

__leaveAloneMemberTableSql = """
    CREATE TABLE IF NOT EXISTS leave_alone_members (
        member_id   TEXT    NOT NULL,
        guild_id    TEXT    NOT NULL,
        PRIMARY KEY(member_id, guild_id)
    );
"""

__ignoredRoleTableSql = """
    CREATE TABLE IF NOT EXISTS ignore_roles (
        role_id     TEXT    NOT NULL    PRIMARY KEY,
        guild_id    TEXT    NOT NULL
    );
"""

def getDBConnection():
    dbConnection = None
    try:
        dbConnection = sqlite3.connect('pycord.db')
        dbConnection.row_factory = sqlite3.Row

        return dbConnection
    except (Exception) as error:
        if dbConnection:
            dbConnection.close()
        raise error


def checkTables():
    dbConnection = getDBConnection()

    try:
        dbCursor = dbConnection.cursor()
        tableCommands = (__leaveAloneMemberTableSql, __ignoredRoleTableSql)

        for command in tableCommands:
            dbCursor.execute(command)

        dbConnection.commit()
        dbCursor.close()
    except (Exception) as error:
        raise error
    finally:
        if dbConnection:
            dbConnection.close()