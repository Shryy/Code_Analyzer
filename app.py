import streamlit as st

def analyze_code(code):
    # Mock analysis function
    suggestions = []
    if "print" in code:
        suggestions.append("Avoid using print statements in production code.")
    if "for i in range" in code:
        suggestions.append("Consider using list comprehensions for efficiency.")
    return suggestions

st.title("AI-Powered Code Analyzer")
code_input = st.text_area("Paste your Python code here:")
if st.button("Analyze Code"):
    if code_input:
        results = analyze_code(code_input)
        if results:
            st.write("### Suggestions:")
            for suggestion in results:
                st.write(f"- {suggestion}")
        else:
            st.write("No issues detected.")
    else:
        st.error("Please enter some code to analyze.")
