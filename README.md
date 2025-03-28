Here's an example of how to use the command-line to-do list application:

1. **Add a new task**:
   ```sh
   python todo.py add "Buy groceries"
   ```
   Output:
   ```
   Task 'Buy groceries' added.
   ```

2. **View all tasks**:
   ```sh
   python todo.py view
   ```
   Output:
   ```
   To-Do List:
   1. Buy groceries
   2. Complete homework assignment
   3. Walk the dog
   4. Call the bank
   5. Read a book
   6. Schedule dentist appointment
   ```

3. **Delete a task by its number**:
   ```sh
   python todo.py delete 2
   ```
   Output:
   ```
   Task 'Complete homework assignment' deleted.
   ```

4. **Show the help message**:
   ```sh
   python todo.py help
   ```
   Output:
   ```
   Usage:
     python todo.py add <task>      Add a new task
     python todo.py view            View all tasks
     python todo.py delete <number> Delete a task by its number
     python todo.py help            Show this help message
   ```

These commands demonstrate how to add, view, and delete tasks using the command-line to-do list application.
