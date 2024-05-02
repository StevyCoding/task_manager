import re
import sys
import psycopg2 as ps
from task import Task  # Assurez-vous que le module task est correctement importé

def connect_to_db():
    return ps.connect(database="task_manager",
                      host="localhost",
                      user="postgres",
                      password="steve",
                      port="5432")

class TaskManager:  # Modifiez le nom de la classe pour utiliser la convention de nommage PEP8
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tasks (
                                id SERIAL PRIMARY KEY,
                                description VARCHAR(255) NOT NULL,
                                status VARCHAR(50) NOT NULL
                            );""")
        conn.commit()

    def get_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def insert_task(self, task):
        if self.validate_task(task):
            self.cursor.execute("INSERT INTO tasks (description, status) VALUES (%s, %s)", (task.description, task.status))
            self.conn.commit()
        else:
            print("La description ou le statut de la tâche est invalide.")

    def update_task(self, task):
        if self.validate_task(task):
            self.cursor.execute("""
                UPDATE tasks
                SET description = %s, status = %s
                WHERE id = %s
            """, (task.description, task.status, task.id))
            self.conn.commit()
        else:
            print("La description ou le statut de la tâche est invalide.")

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.conn.commit()

    @staticmethod
    def validate_task(task):  # Décorez la méthode comme statique car elle ne fait pas référence à self
        # Valider la description de la tâche
        if not re.match(r'^[\w\s\-\'\",.?!]*$', task.description):
            return False
        # Valider le statut de la tâche
        if task.status not in ["En cours", "En attente", "Terminé"]:
            return False
        return True

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

def main():
    task_manager = TaskManager(connect_to_db())

    if len(sys.argv) > 1:
        if sys.argv[1] == "add":
            print("Ajout d'une nouvelle tâche")
            description = input("Description de la tâche : ")
            status = input("Statut de la tâche (En cours/En attente/Terminé) : ")
            task = Task(0, description, status)
            task_manager.insert_task(task)
        elif sys.argv[1] == "selectAll":
            print(task_manager.get_tasks())
        elif sys.argv[1] == "update":
            print("Modification d'une tâche")
            task_id = input("ID de la tâche à modifier : ")
            description = input("Nouvelle description de la tâche : ")
            status = input("Nouveau statut de la tâche (En cours/En attente/Terminé) : ")
            task = Task(int(task_id), description, status)
            task_manager.update_task(task)
        elif sys.argv[1] == "delete":
            print("Suppression d'une tâche")
            task_id = input("ID de la tâche à supprimer : ")
            task_manager.delete_task(int(task_id))
    else:
        print("Usage: python script_name.py [add|selectAll|update|delete]")

    task_manager.close_connection()

if __name__ == "__main__":
    main()

