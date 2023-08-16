import mysql.connector
import tkinter as tk
from tkinter import messagebox
import random
import difflib

# Connect to the MySQL database
db = mysql.connector.connect(host="localhost", user="root", password="1234", database="CSproject")


# Create a cursor to interact with the database
cursor = db.cursor()


# Function to handle the "Add New User" button click
def add_new_user():

    # Function to save new user data to the UserTable
    def save_user_to_database(username,password):
        try:
            # Establish a connection to the database for user
            user_db_connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="CSproject")

            # Create a cursor to interact with the user database
            user_db_cursor = user_db_connection.cursor()

            # Insert data into the UserTable
            insert_query = "INSERT INTO UserTable (Username, Password) VALUES (%s, %s)"
            values = (username, password)
            user_db_cursor.execute(insert_query, values)
            user_db_connection.commit()

            messagebox.showinfo("Success", "User added successfully! ID: {}".format(user_db_cursor.lastrowid))

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")

        finally:
            if user_db_cursor:
                user_db_cursor.close()
            if user_db_connection:
                user_db_connection.close()

    user_window = tk.Toplevel()
    user_window.title("Add New User")

    username_label = tk.Label(user_window, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(user_window)
    username_entry.pack()

    password_label = tk.Label(user_window, text="Password (not greater than 8 characters):")
    password_label.pack()

    password_entry = tk.Entry(user_window, show="*")
    password_entry.pack()

    def save_user():
        new_username = username_entry.get()
        new_password = password_entry.get()

        if len(new_password) <= 8:
            save_user_to_database(new_username, new_password)
            user_window.destroy()
        else:
            messagebox.showerror("Error", "Password should not be greater than 8 characters.")

    save_button = tk.Button(user_window, text="Save User", command=save_user)
    save_button.pack(padx=20, pady=10)



# Function to add new question to the database
def add_question():

    # Function to save data to the database
    def save_to_database():

        try:
            # ...

            qno_str = qno_var.get().strip()
            if not qno_str:
                raise ValueError("Question number cannot be empty")
    
            q_no = int(qno_str)


        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")


        try:
            # Establish a connection to the database
            db_connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="CSproject")

            # Create a cursor to interact with the database
            db_cursor = db_connection.cursor()

            # Create the QuestionAnswer table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS QuestionAnswer (
                Q_no INT PRIMARY KEY,
                Question TEXT NOT NULL,
                Answer TEXT NOT NULL,
                QuestionType VARCHAR(20) DEFAULT NULL
            );
            """
            db_cursor.execute(create_table_query)


            # Get user input
            question = question_text.get("1.0", tk.END).strip()
            answer = answer_text.get("1.0", tk.END).strip()
            question_type_input = question_type_text.get("1.0", tk.END).strip()  # Retrieve question type from text widget

            # Insert data into the QuestionAnswer table
            insert_query = "INSERT INTO QuestionAnswer (Q_no, Question, Answer, QuestionType) VALUES (%s, %s, %s, %s)"
            values = (q_no, question, answer, question_type_input)
            db_cursor.execute(insert_query, values)
            db_connection.commit()

            messagebox.showinfo("Success", "Question and answer saved successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {err}")

        finally:
            if db_cursor:
                db_cursor.close()
            if db_connection:
                db_connection.close()

    

    # Create the GUI window
    root = tk.Tk()
    root.title("Question and Answer Entry")

    def cancel():
        root.destroy()  # Close the Add Question window


    # Create and place GUI widgets
    qno_label = tk.Label(root, text="Question Number:")
    qno_label.pack()

    qno_var = tk.StringVar()

    # Display the automatically generated question number
    last_question_query = "SELECT MAX(Q_no) FROM QuestionAnswer"
    cursor.execute(last_question_query)
    last_question_number = cursor.fetchone()[0]
    next_question_number = last_question_number + 1
    qno_var.set(str(next_question_number))

    qno_label_text = f"Question Number: {next_question_number}"
    qno_label = tk.Label(root, text=qno_label_text)
    qno_label.pack()

    question_label = tk.Label(root, text="Question:")
    question_label.pack()

    question_text = tk.Text(root, height=3, width=40)
    question_text.pack(padx=10)

    answer_label = tk.Label(root, text="Answer:")
    answer_label.pack()

    answer_text = tk.Text(root, height=3, width=40)
    answer_text.pack(padx=10)

    question_type_label = tk.Label(root, text="Question Type (Easy, Medium, Hard):")
    question_type_label.pack()

    question_type_text = tk.Text(root, height=1, width=10)
    question_type_text.pack(padx=30)

    save_button = tk.Button(root, text="Save", command=save_to_database)
    save_button.pack(padx=20, pady=10)

    
    cancel_button = tk.Button(root, text="Cancel/Close", command=cancel)
    cancel_button.pack(padx=20, pady=10)


    root.mainloop()

# Function to view the question database
def view_database():
    # Code to view the question database
    pass

# Function to play the quiz game
def play_quiz():
    # Select a random question from the database
    cursor.execute("SELECT question FROM QuestionAnswer")
    questions = cursor.fetchall()
    if not questions:
        messagebox.showinfo("Info", "No questions available in the database.")
        return

    random_question = random.choice(questions)[0]

    # Create a new window for the quiz game
    quiz_window = tk.Toplevel(app)
    quiz_window.title("Quiz Game")

    # Display the random question
    question_label = tk.Label(quiz_window, text=random_question)
    question_label.pack()

    # Entry for user's answer
    answer_entry = tk.Entry(quiz_window)
    answer_entry.pack()

    # Function to check the answer
    def check_answer():
        user_answer = answer_entry.get()
        correct_answer = random_question.lower()

        # Compare the user's answer with the correct answer
        similarity_ratio = difflib.SequenceMatcher(None, user_answer.lower(), correct_answer).ratio()

        if similarity_ratio >= 0.10:  
            result = "Correct"
        else:
            result = "Incorrect"

        messagebox.showinfo("Result", f"Your answer is {result}.")

        # Close the quiz window
        quiz_window.destroy()

    check_button = tk.Button(quiz_window, text="Check Answer", command=check_answer)
    check_button.pack()

# Create the main application window
app = tk.Tk()
app.title("Quiz App")

# Create and place the buttons horizontally
#Add New question button
add_button = tk.Button(app, text="Add New Question", command=add_question)
add_button.pack(side="left", padx=10, pady=10)

#Play button
play_button = tk.Button(app, text="Play Quiz Game", command=play_quiz)
play_button.pack(side="left", padx=10, pady=10)

#View database button
view_button = tk.Button(app, text="View Question Database", command=view_database)
view_button.pack(side="left", padx=10, pady=10)

#Add new user button
add_user_button = tk.Button(app, text="Add New User", command=add_new_user)
add_user_button.pack(side="left", padx=10, pady=10)


# Run the GUI application
app.mainloop()
