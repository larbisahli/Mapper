"""
            ####################################
            #                                  #
            #       Author: Larbi Sahli        #
            #                                  #
            #  https://github.com/larbisahli  #
            #                                  #
            ####################################
"""

import sqlite3
import threading


# =================== <Database management> =====================

# Tables: journal, Notes, Pre_values, BTC_H_daily, BTC_H_weekly, BTC_H_monthly, sign


class Table:

    def __init__(self, name):
        self.name = name

    def create(self):
        try:
            if self.name == "Metadata":
                c.execute(f"""CREATE TABLE IF NOT EXISTS Metadata(
                            id TEXT PRIMARY KEY,
                            data TEXT)""")
            else:
                c.execute(f"""CREATE TABLE IF NOT EXISTS {self.name}(
                                                    name TEXT PRIMARY KEY,
                                                    element TEXT,
                                                    attr TEXT,
                                                    parent TEXT,
                                                    children TEXT,
                                                    css TEXT,
                                                    description TEXT )""")
        except Exception:
            pass

    def drop(self):
        try:
            sql = f"DROP TABLE {self.name}"
            with conn:
                c.execute(sql)
        except Exception:
            pass

    @property
    def check(self):
        try:
            with conn:
                query = f"SELECT table_name from sqlite_master WHERE type='table' AND table_name='{self.name}';"
                result = c.execute(query).fetchone()
            return False if result is None else result[0] == self.name
        except sqlite3.Error:
            pass
        except Exception:
            pass


""" Using 'with', will allows us to create a temporary cursor 
that will be closed once you return to your previous indentation level. """


class Metadata:

    def __init__(self, _id):
        self.id = _id

    def insert(self, data):
        try:
            lock.acquire(True)
            with conn:
                c.execute("INSERT INTO Metadata VALUES (:id, :data)",
                          {"id": self.id, "data": data})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def update(self, data):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"""UPDATE Metadata SET data = :data WHERE id = :id""", {"id": self.id, "data": data})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def delete(self, _id):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"DELETE from Metadata WHERE id = :id", {'id': _id})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()


class Projects:

    def __init__(self, table_name):
        self.table_name = table_name

    def insert(self, name, element, attr, parent, children, css, description):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"INSERT INTO {self.table_name} VALUES "
                          f"(:table_name, :element, :attr, :parent, :children, :css, :description)"
                          , {"table_name": name, 'element': element, 'parent': parent,
                             "children": children, "css": css, "description": description, "attr": attr})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def update_all(self, name, element, attr, parent, children, css, description):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"""UPDATE {self.table_name} SET element = :element, attr = :attr, parent = :parent,
                              children = :children, css = :css, description = :description 
                              WHERE table_name = :table_name""",
                          {"table_name": name,
                           'element': element,
                           "attr": attr,
                           'parent': parent,
                           "children": children,
                           "css": css,
                           "description": description})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def update_one(self, update, name, data):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"""UPDATE {self.table_name} SET {update} = :data WHERE name = :name""",
                          {"data": data, "name": name})
        except sqlite3.Error as e:
            print(e)
            pass
        except Exception:
            pass
        finally:
            lock.release()


class Extract:

    def __init__(self, table_name):
        self.table_name = table_name

    def get_by_name(self, column, name):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"SELECT * FROM {self.table_name} WHERE {column}= :name", {'name': name})
                return [id_ for id_ in c.fetchall()[0]]
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def delete(self, name):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"DELETE from {self.table_name} WHERE name = :name", {'name': name})
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def select_column(self, column):
        try:
            lock.acquire(True)
            with conn:
                return [column[0] for column in c.execute(f"SELECT {column} FROM {self.table_name}")]
        except sqlite3.Error:
            pass
        except Exception:
            pass
        finally:
            lock.release()

    def fetchall(self):
        try:
            lock.acquire(True)
            with conn:
                c.execute(f"select * from '{self.table_name}'")
                return c.fetchall()
        except sqlite3.Error:
            return []
        finally:
            lock.release()

    def __len__(self):
        return len(self.select_column("name"))


conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()
lock = threading.Lock()
