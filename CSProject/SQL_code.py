import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to save data to the database
def save_to_database():
    try:
        # Establish a connection to the database
        db_connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="CSproject")

        # Create a cursor to interact with the database
        cursor = db_connection.cursor()

        # Create the QuestionAnswer table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS QuestionAnswer (
            Q_no INT PRIMARY KEY,
            Question TEXT NOT NULL,
            Answer TEXT NOT NULL,
            QuestionType VARCHAR(20) DEFAULT NULL
        );
        """
        cursor.execute(create_table_query)

        # Get user input
        q_no = int(qno_var.get())
        question = question_text.get("1.0", tk.END).strip()
        answer = answer_text.get("1.0", tk.END).strip()
        question_type_input = question_type_text.get("1.0", tk.END).strip()  # Retrieve question type from text widget

        # Insert data into the QuestionAnswer table
        insert_query = "INSERT INTO QuestionAnswer (Q_no, Question, Answer, QuestionType) VALUES (%s, %s, %s, %s)"
        values = (q_no, question, answer, question_type_input)
        cursor.execute(insert_query, values)
        db_connection.commit()

        messagebox.showinfo("Success", "Question and answer saved successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

# Create the GUI window
root = tk.Tk()
root.title("Question and Answer Entry")

# Create and place GUI widgets
qno_label = tk.Label(root, text="Question Number:")
qno_label.pack()

qno_var = tk.StringVar()
qno_entry = tk.Entry(root, textvariable=qno_var)
qno_entry.pack()

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

root.mainloop()
