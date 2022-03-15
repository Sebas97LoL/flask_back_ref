from src.extensions import db


class Connection:
    __instance = None

    @staticmethod
    def get_instance():
        if Connection.__instance is None:
            Connection.__instance = db.session()
        return Connection.__instance

    @classmethod
    def commit_changes(cls):
        Connection.get_instance().commit()

    @classmethod
    def close_session(cls):
        if Connection.__instance:
            Connection.get_instance().close()
            Connection.__instance = None
