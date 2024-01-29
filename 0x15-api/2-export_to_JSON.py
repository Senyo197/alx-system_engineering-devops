#!/usr/bin/python3
"""
Script that exports an employee TODO tasks to a json file
Is an interger representing an employee id.
"""

import json
import requests
import sys


class TodoExporterJSON:
    """
    A class for exporting employee TODO tasks to a JSON file.
    """

    def __init__(self, user_id):
        """
        Initializes the TodoExporterJSON instance.

        Args:
            user_id (str): The ID of the user for whom tasks will be exported.
        """
        self.user_id = user_id

    def fetch_user_data(self):
        """
        Fetches user data from the REST API and returns it as a dictionary.
        """
        url_user = f"https://jsonplaceholder.typicode.com/users/{self.user_id}"
        user_data = requests.get(url_user).json()
        return user_data

    def fetch_user_todos(self):
        """
        Fetches user tasks (todos) from the REST API and returns them as a list
        """
        url_todos = (
            f"https://jsonplaceholder.typicode.com/"
            f"todos?userId={self.user_id}"
        )
        todos_data = requests.get(url_todos).json()
        return todos_data

    def export_to_json(self):
        """
        Exports user tasks to a JSON file named with the user ID.
        The JSON file includes a dictionary with the user ID as the key and
        a list of tasks as the value.
        Each task is represented as a dictionary with keys 'task',
        'completed', and 'username'.
        """
        user_data = self.fetch_user_data()
        todos_data = self.fetch_user_todos()

        with open(f"{self.user_id}.json", "w") as file_json:
            json.dump({self.user_id: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user_data.get('username')
            } for task in todos_data]}, file_json)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py user_id")
        sys.exit(1)

    user_id = sys.argv[1]

    todo_exporter = TodoExporterJSON(user_id)
    todo_exporter.export_to_json()
