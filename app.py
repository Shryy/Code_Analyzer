
import streamlit as st

# Function to analyze code
def analyze_code(code: str) -> list:
    suggestions = []
    if "print" in code:
        suggestions.append("Avoid using print statements in production code.")
    if "for i in range" in code:
        suggestions.append("Consider using list comprehensions for efficiency.")
    if "==" in code and "None" in code:
        suggestions.append("Use 'is' instead of '==' to compare with None.")
    return suggestions

# Streamlit UI
def run_app():
    st.title("AI-Powered Code Analyzer")
    st.write("Paste your Python code below to analyze for performance bottlenecks:")
    code_input = st.text_area("Your Code:", height=200, placeholder="Paste your Python code here...")
    
    if st.button("Analyze Code"):
        if code_input:
            results = analyze_code(code_input)
            st.write("### Suggestions:")
            if results:
                for suggestion in results:
                    st.write(f"- {suggestion}")
            else:
                st.write("No performance issues detected. Great job!")
        else:
            st.error("Please enter some code to analyze.")

# Run the app
if __name__ == "__main__":
    run_app()
