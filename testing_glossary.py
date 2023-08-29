import streamlit as st

# Define your glossary of software testing terminologies
glossary = {
    "Regression Testing": "Re-running previously executed test cases to ensure that changes in the code have not introduced new defects.",
    "QA (Quality Assurance)": "A systematic process that ensures product quality meets specified requirements by implementing quality control and quality improvement processes.",
    "Bug": "A flaw or defect in a software application that causes it to behave unexpectedly or incorrectly.",
    "Automation Testing": "The use of automated scripts and tools to perform tests on software applications, speeding up the testing process and increasing test coverage.",
    "Acceptance Testing": "Testing conducted to determine whether a system satisfies the acceptance criteria and is ready for customer use.",
    "Ad Hoc Testing": "Informal testing without predefined test cases; testers explore the application to find defects.",
    "Alpha Testing": "Testing conducted by the development team to evaluate the software's functionality and stability before beta testing.",
    "Beta Testing": "Testing conducted by external users to identify defects and provide feedback before the software's final release.",
    "Boundary Testing": "Testing at the edges or boundaries of valid input or output to check for potential issues.",
    "Code Coverage": "A metric indicating the percentage of code covered by executed test cases.",
    "Continuous Integration (CI)": "Automatically integrating code changes into a shared repository multiple times a day, ensuring early detection of issues.",
    "Defect": "A variance between expected and actual results that indicates a flaw in the software.",
    "End-to-End Testing": "Testing the entire application flow, including all integrated components.",
    "Exploratory Testing": "Informal testing where testers explore the application without predefined test cases.",
    "Fuzz Testing": "Sending random, invalid, or unexpected data to the application to discover vulnerabilities.",
    "Load Testing": "Testing the system's performance under expected load conditions.",
    "Negative Testing": "Testing to validate that the application handles invalid inputs or unexpected behaviors correctly.",
    "Performance Testing": "Testing to evaluate the application's speed, responsiveness, and stability under different conditions.",
    "Smoke Testing": "Basic testing to ensure the application is stable enough for further testing.",
    "Static Testing": "Reviewing code and documentation without executing it to find defects early in the development process.",
    "Test Case": "A set of conditions and inputs to be tested, along with the expected results.",
    "Test Plan": "A document outlining the scope, objectives, resources, and schedule for testing activities.",
    "Test Suite": "A collection of test cases grouped together for a specific purpose or functionality.",
    "Usability Testing": "Testing to assess how user-friendly and intuitive the application is.",
    "Validation Testing": "Testing to ensure that the software meets the specified requirements and satisfies the user's needs.",
    "White Box Testing": "Testing that examines the internal structure, code, and logic of the application.",
    # Add more glossary terms here
}

# Streamlit app title and description
st.title("Test Gloss")
st.write("Welcome to the Software Testing Glossary! Here you will find a wide range of software testing concepts, from different testing types to testing methodologies and practices")

# Dropdown to select a glossary term
selected_term = st.selectbox("Select a Term:", sorted(glossary.keys()))

# Display the definition of the selected term
if selected_term:
    st.subheader(selected_term)
    st.write(glossary[selected_term])

# Optional: Provide a search bar for terms
search_term = st.text_input("Search for a Term:")
if search_term:
    matching_terms = [term for term in glossary.keys(
    ) if search_term.lower() in term.lower()]
    if matching_terms:
        st.write("Matching Terms:")
        for term in matching_terms:
            st.write(f"- {term}")


