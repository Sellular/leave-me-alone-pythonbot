from utils import DBUtils

__ignoreRoleSelectByGuildSql = """
    SELECT * FROM ignore_roles
    WHERE guild_id = ?
"""

__ignoreRoleInsertSql = """
    INSERT OR IGNORE INTO ignore_roles (
        role_id,
        guild_id
    ) VALUES (
        ?,
        ?
    )
"""

__ignoreRoleDeleteByRoleGuildSql = """
    DELETE FROM ignore_roles
    WHERE
        role_id = ?
        AND guild_id = ?
"""

def getIgnoreRolesByGuild(guildID: str):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbCursor = dbConnection.execute(
                __ignoreRoleSelectByGuildSql, (guildID,))
            
            rows = dbCursor.fetchall()

            roles = []
            if rows:
                for row in rows:
                    roles.append(row['role_id'])

            return roles
    except (Exception) as error:
        raise error

def insert(role_id, guild_id):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.execute(
                __ignoreRoleInsertSql, (role_id, guild_id)
            )

            dbConnection.commit()
    except Exception as error:
        raise error

def deleteIgnoreRolesByMemberGuild(roleID: str, guildID: str):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.execute(
                __ignoreRoleDeleteByRoleGuildSql, (roleID, guildID))
            dbConnection.commit()
    except (Exception) as error:
        raise error