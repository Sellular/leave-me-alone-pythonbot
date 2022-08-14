from utils import DBUtils

__leaveAloneMemberSelectByGuildSql = """
    SELECT * FROM leave_alone_members
    WHERE guild_id = ?
"""

__leaveAloneInsertSql = """
    INSERT OR IGNORE INTO leave_alone_members (
        member_id,
        guild_id
    ) VALUES (
        ?,
        ?
    )
"""

__leaveAloneMemberDeleteByMemberGuildSql = """
    DELETE FROM leave_alone_members
    WHERE
        member_id = ? AND
        guild_id = ?
"""

def getLeaveAloneMembersByGuild(guildID: str):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbCursor = dbConnection.execute(
                __leaveAloneMemberSelectByGuildSql, (guildID,))
            
            rows = dbCursor.fetchall()

            members = []
            if rows:
                for row in rows:
                    members.append(row['member_id'])

            return members
    except (Exception) as error:
        raise error

def insert(member_id, guild_id):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.execute(
                __leaveAloneInsertSql, (member_id, guild_id)
            )

            dbConnection.commit()
    except Exception as error:
        raise error

def deleteLeaveAloneMembersByMemberGuild(memberID: str, guildID: str):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.execute(
                __leaveAloneMemberDeleteByMemberGuildSql, (memberID, guildID))
            dbConnection.commit()
    except (Exception) as error:
        raise error