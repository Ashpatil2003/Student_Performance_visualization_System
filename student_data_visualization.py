import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#used functions for easy understanding

def get_list_input(prompt, cast_type=str):
    while True:
        try:
            values = list(map(cast_type, input(prompt).split(",")))
            return values
        except:
            print("Invalid input. Please enter values separated by commas.")


def create_dataframe():
    print("\nEnter Subject Names (comma separated)")
    subjects = get_list_input("Subjects: ", str)

    print("\nEnter Marks for Each Exam (same number of values as subjects)")
    first_test = get_list_input("First Test: ", int)
    first_term = get_list_input("First Term: ", int)
    second_test = get_list_input("Second Test: ", int)
    second_term = get_list_input("Second Term: ", int)

    if not (len(subjects) == len(first_test) == len(first_term) == len(second_test) == len(second_term)):
        print("Number of subjects and marks do not match. Restart program.")
        exit()

    df = pd.DataFrame({
        "Subject": subjects,
        "First Test": first_test,
        "First Term": first_term,
        "Second Test": second_test,
        "Second Term": second_term
    })

    return df


def single_bar_graph(df):
    df.set_index("Subject").plot(kind="bar", figsize=(10,6))
    plt.title("Student Marks Comparison")
    plt.ylabel("Marks")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def subplot_line_graphs(df):
    exams = df.columns[1:]
    x = df["Subject"]

    plt.figure(figsize=(12,8))

    for i, exam in enumerate(exams, 1):
        plt.subplot(2, 2, i)
        plt.plot(x, df[exam], marker='o')
        plt.title(exam)
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def subplot_bar_graphs(df):
    exams = df.columns[1:]
    x = np.arange(len(df["Subject"]))

    plt.figure(figsize=(12,8))

    for i, exam in enumerate(exams, 1):
        plt.subplot(2, 2, i)
        plt.bar(df["Subject"], df[exam])
        plt.title(exam)
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def stacked_bar_graph(df):
    x = np.arange(len(df["Subject"]))

    plt.figure(figsize=(10,6))
    plt.bar(x, df["First Test"], label="First Test")
    plt.bar(x, df["First Term"], bottom=df["First Test"], label="First Term")
    plt.bar(x, df["Second Test"], bottom=df["First Test"] + df["First Term"], label="Second Test")
    plt.bar(x, df["Second Term"],
            bottom=df["First Test"] + df["First Term"] + df["Second Test"],
            label="Second Term")

    plt.xticks(x, df["Subject"], rotation=45)
    plt.ylabel("Marks")
    plt.title("Stacked Bar Graph – Total Performance")
    plt.legend()
    plt.tight_layout()
    plt.show()


def stacked_area_graph(df):
    x = np.arange(len(df["Subject"]))

    plt.figure(figsize=(10,6))
    plt.stackplot(
        x,
        df["First Test"],
        df["First Term"],
        df["Second Test"],
        df["Second Term"],
        labels=["First Test", "First Term", "Second Test", "Second Term"]
    )

    plt.xticks(x, df["Subject"], rotation=45)
    plt.ylabel("Marks")
    plt.title("Stacked Area Graph – Performance Distribution")
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()


def multi_line_graph(df):
    x = df["Subject"]

    plt.figure(figsize=(10,6))
    for col in df.columns[1:]:
        plt.plot(x, df[col], marker='o', label=col)

    plt.title("Student Marks Line Graph")
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Main Program

print("Student Performance Visualization System")
student_name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

df = create_dataframe()

print("\nStudent:", student_name)
print("Class:", student_class)
print("\nMarks Data:\n", df)

print("""
Choose Graph Type:
1. Bar Graph (All Exams Together)
2. Multiple Line Graphs (Subplots)
3. Multiple Bar Graphs (Subplots)
4. Stacked Bar Graph
5. Stacked Area Graph
6. Combined Line Graph
""")

choice = input("Enter choice (1-6): ")

if choice == "1":
    single_bar_graph(df)
elif choice == "2":
    subplot_line_graphs(df)
elif choice == "3":
    subplot_bar_graphs(df)
elif choice == "4":
    stacked_bar_graph(df)
elif choice == "5":
    stacked_area_graph(df)
elif choice == "6":
    multi_line_graph(df)
else:
    print("Invalid choice")
