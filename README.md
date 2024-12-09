# Code_Analyzer
## How to Run the Project

1. Clone the repository:

2. Install required dependencies:pip install -r requirements.txt

3. Run the Streamlit app:streamlit run app.py
   
4. The app should open in your browser at `http://localhost:8501`.
5. ## Design Choices

- **Framework**: Streamlit was chosen because it provides a simple and intuitive interface to build interactive web applications with minimal code.
- **Code Analysis**: The code analyzer uses simple heuristics to check for performance bottlenecks. This can later be expanded to use AI-based methods for deeper analysis.
- **User Input**: A text area is used for the user to paste code. This approach was chosen for simplicity and ease of use.
- **Log Level**: The code uses basic logging with Streamlit's built-in functionality to display results, avoiding the use of `print` in production code.
- 
6. ## Assumptions and Limitations

- The code currently performs simple static analysis, which can only handle basic Python code patterns. A more sophisticated AI-driven analysis could be implemented in the future.
- The application assumes that the user will provide Python code in the correct format.
- The tool does not handle large files or code snippets efficiently. Future improvements could include more advanced parsing techniques and optimization.
- The app only handles Python code and does not support other languages or non-standard Python syntax.

## Screenshots

Here are some screenshots of the application in action:

- **Input Screen**:
  ![Input Screenshot](https://github.com/Shryy/Code_Analyzer/blob/2f35284f4f390d161a35f517859185fe070b6c6b/Input.png
)

- **Result Screen**:
  ![Result Screenshot](https://github.com/Shryy/Code_Analyzer/blob/2f35284f4f390d161a35f517859185fe070b6c6b/result.png)




