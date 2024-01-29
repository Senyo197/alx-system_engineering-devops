#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
"""

import csv
import requests
import sys


class TodoExporter:
    """
    A class for exporting user tasks from a REST API to a CSV file.
    """

    def __init__(self, user_id):
        """
        Initializes the TodoExporter instance.

        Args:
            user_id (str): The ID of the user for whom tasks will be exported.
        """
        self.user_id = user_id
        self.username = None
        self.tasks = []

    def fetch_user_data(self):
        """
        Fetches user data from the REST API and sets the username attribute.
        """
        url_user = f"https://jsonplaceholder.typicode.com/users/{self.user_id}"
        user_data = requests.get(url_user).json()
        self.username = user_data.get("username")

    def fetch_user_todos(self):
        """
        Fetches user tasks (todos) from the REST API and sets
        the tasks attribute.
        """
        url_todos = (
            f"https://jsonplaceholder.typicode.com/users/"
            f"{self.user_id}/todos"
        )
        todos_data = requests.get(url_todos).json()
        self.tasks = todos_data

    def export_to_csv(self):
        """
        Exports user tasks to a CSV file named with the user ID.
        The CSV file includes columns for user ID, username,
        task completion status, and task title.
        """
        with open(f"{self.user_id}.csv", "w") as file_c:
            writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
            for task in self.tasks:
                writer.writerow([self.user_id, self.username,
                                task.get("completed"), task.get("title")])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py user_id")
        sys.exit(1)

    user_id = sys.argv[1]

    todo_exporter = TodoExporter(user_id)
    todo_exporter.fetch_user_data()
    todo_exporter.fetch_user_todos()
    todo_exporter.export_to_csv()
