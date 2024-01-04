import os
import sqlite3
import logging


class DatabaseManager:
    def __init__(self):
        self.db_name = "db/db.sqlite3"
        self.default_username = str(os.getlogin()).upper()
        self.log_username = None

        logging.basicConfig(filename="log/log.txt", level=logging.ERROR, format="%(asctime)s - %(levelname)s: %(message)s")

    @staticmethod
    def log_error(error_message):
        logging.error(error_message)

    def initialize_database(self):
        if not os.path.exists(self.db_name):
            try:
                connection = sqlite3.connect(self.db_name)
                cursor = connection.cursor()

                # Create 'users' table if it doesn't exist
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        default_username TEXT,
                        log_username TEXT
                    )
                ''')

                cursor.execute(f'''
                                INSERT INTO users (default_username, log_username)
                                VALUES ("{self.default_username}", "{self.log_username}")
                            ''')

                connection.commit()
                return True
            except sqlite3.Error as e:
                self.log_error(f"Error creating table: {e}")
                return 'error'
            finally:
                if connection:
                    connection.close()
        pass

    def change_values(self, default_username, log_username):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            if default_username is None:
                cursor.execute(f'''
                                UPDATE users
                                SET log_username = "{log_username}"
                                ''')
            else:
                cursor.execute(f'''
                                UPDATE users
                                SET default_username = "{default_username}", log_username = "{log_username}"
                            ''')

            connection.commit()
            return True
        except sqlite3.Error as e:
            self.log_error(f"Error updating user: {e}")
            return 'error'
        finally:
            if connection:
                connection.close()

    def get_default_username(self):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Retrieve default username
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchone()

            if result:
                if result[2] == 'None':
                    return result[1]
                else:
                    return result[2]
            else:
                self.insert_values(self.default_username, self.log_username)
        except sqlite3.Error as e:
            self.log_error(f"Error getting default username: {e}")
            return 'error'
        finally:
            if connection:
                connection.close()


