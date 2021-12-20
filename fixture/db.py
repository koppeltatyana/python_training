import pymysql.cursors
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)  # autocommit = True - отключили кэширование БД (кэш после каждого запроса сбрасывается)

    #  загружает список групп из БД
    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                group_list += [Group(group_id=str(group_id), group_name=group_name, group_header=group_header, group_footer=group_footer)]
        finally:
            cursor.close()
        return group_list

    def destroy(self):
        self.connection.close()
