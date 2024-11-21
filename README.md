# Collatz Sequence Generator

This Python project implements the **Collatz Sequence**, also known as the "3n + 1 problem" or the "simplest impossible math problem." The sequence is generated based on a user-provided positive integer. It iteratively applies the following rules until the number becomes 1:

- If the number is **even**, divide it by 2.
- If the number is **odd**, multiply it by 3 and add 1.

This sequence is fascinating because, no matter what positive integer you start with, it will always eventually reach 1 (though no formal proof exists for this claim). 

---

## **How It Works**
1. The program prompts the user to input a positive integer.
2. Input validation ensures that the user enters a valid positive integer. If an invalid value is provided, the program displays an error message and terminates gracefully.
3. Using a **while loop**, the program computes the Collatz Sequence step-by-step and displays each intermediate value until the sequence reaches `1`.
4. After the sequence is complete, a message is displayed to indicate successful execution.

---

## **Requirements**
- Python 3.x

No external libraries are required for this project.

---

## **How to Run**
1. Clone this repository:
   ```bash
   git clone https://github.com/Mr-Anas608/The_Collatz_Sequence
    ```bash
   cd The_collatz_sequence.py
    ```bash
   python The_collatz_sequence.py


