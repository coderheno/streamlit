import streamlit as st

def main():
    st.title("Career Paths After Undergraduate Studies")

    # Define the tabs
    tabs = ["Post-Graduation", "Placements", "Business Plans", "Interview Questions"]
    selected_tab = st.sidebar.selectbox("Select a Tab", tabs)

    if selected_tab == "Post-Graduation":
        post_graduation()
    elif selected_tab == "Placements":
        placements()
    elif selected_tab == "Business Plans":
        business_plans()
    elif selected_tab == "Interview Questions":
        interview_questions()

def post_graduation():
    st.header("Post-Graduation")

    st.subheader("Post-Graduation in India")
    st.write("""
    1. **Choosing Institutions and Courses:**
        - Research and Rankings
        - Accreditation
        - Faculty and Infrastructure
        - Alumni Network and Placement Records
        - Course Curriculum
        - Entrance Exams
    
    2. **Popular Institutions:**
        - IITs, NITs, IIMs, IIITs, IISc, TIFR, and other premier universities
    """)

    st.subheader("Post-Graduation Abroad")
    st.write("""
    1. **Choosing Institutions and Courses:**
        - World Rankings and Reputation
        - Course Structure and Specializations
        - Research Opportunities
        - Location and Cost
        - Scholarships and Financial Aid
    
    2. **Popular Countries and Exams:**
        - Countries: USA, UK, Canada, Australia, Germany
        - Exams: GRE, TOEFL, IELTS, GMAT
    
    3. **Application Process:**
        - Standardized Tests
        - Documentation
        - Deadlines
    """)

def placements():
    st.header("Placements")

    st.subheader("Selecting Companies")
    st.write("""
    - Industry Fit
    - Company Reputation
    - Roles Offered
    - Location
    """)

    st.subheader("Cracking Interviews")
    st.write("""
    - **Preparation:**
        - Aptitude Tests
        - Technical Skills
        - Mock Interviews
    
    - **Resources:**
        - Books: "Cracking the Coding Interview", "Programming Interviews Exposed"
        - Online Platforms: LeetCode, HackerRank, CodeSignal
    """)

    st.subheader("Aiming for Top Companies (Microsoft, Google, Oracle, etc.)")
    st.write("""
    - **Preparation Tips:**
        - Coding: Master data structures and algorithms
        - System Design: Understand system architecture, scalability, and design patterns
        - Mock Interviews: Focus on problem-solving and system design
        - Behavioral Interviews: Prepare using the STAR method (Situation, Task, Action, Result)
        - Networking: Connect with employees, attend events, seek referrals
    """)

def business_plans():
    st.header("Business Plans")

    st.subheader("Business Plan Ideas for Software Students")
    st.write("""
    1. **Startup Company:**
        - App Development
        - Software as a Service (SaaS)
        - Tech Consultancy
        - E-commerce Platform
        - Game Development
    
    2. **Developing a Business Plan:**
        - Market Research
        - Business Model
        - Funding
        - Marketing Strategy
        - Legal Formalities
    """)

def interview_questions():
    st.header("Interview Questions")

    st.subheader("Technical Problem-Solving Questions")
    st.write("""
    **Question 1:**
    Given a string, reverse only the vowels of the string.

    **Solution:**
    ```python
    def reverse_vowels(s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
        return ''.join(s)
    
    # Example
    print(reverse_vowels("hello"))  # Output: "holle"
    print(reverse_vowels("leetcode"))  # Output: "leotcede"
    ```

    **Question 2:**
    Find the intersection of two arrays.

    **Solution:**
    ```python
    def intersection(nums1, nums2):
        return list(set(nums1) & set(nums2))
    
    # Example
    print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]
    ```

    **Question 3:**
    Implement a function to check if a given binary tree is a binary search tree (BST).

    **Solution:**
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def is_valid_bst(root, low=float('-inf'), high=float('inf')):
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return (is_valid_bst(root.left, low, root.val) and
                is_valid_bst(root.right, root.val, high))
    
    # Example
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_valid_bst(root))  # Output: True
    ```
    """)

    st.subheader("Scenario-Based Questions")
    st.write("""
    **Question 1:**
    You are given a team project to deliver a software product within a tight deadline. Midway through the project, one of your key team members falls sick and cannot contribute. How would you handle this situation to ensure the project is still delivered on time?

    **Solution:**
    - **Assess the Impact:** Determine which parts of the project are affected and the extent of the impact.
    - **Reallocate Tasks:** Redistribute the key team member's tasks among the remaining team members based on their strengths.
    - **Prioritize:** Focus on the most critical components that need to be delivered.
    - **Seek Help:** If necessary, request additional resources or temporary help from other teams.
    - **Communicate:** Keep stakeholders informed about the situation and any potential changes to the delivery schedule.
    - **Monitor Progress:** Regularly check on the progress and provide support to ensure the team stays on track.

    **Question 2:**
    You are leading a project, and you notice that two team members have conflicting opinions on how to proceed with a particular task. This conflict is causing delays. How would you resolve this conflict?

    **Solution:**
    - **Listen to Both Sides:** Hear out each team member's perspective without taking sides.
    - **Find Common Ground:** Identify areas where both opinions overlap or can be integrated.
    - **Evaluate Options:** Assess the pros and cons of each approach with the team.
    - **Make a Decision:** Choose the best approach based on the project's goals and constraints.
    - **Communicate Clearly:** Explain the decision to the team and ensure everyone understands and agrees to move forward.
    - **Follow-Up:** Monitor the implementation to ensure the conflict is resolved and progress is made.

    **Question 3:**
    You are in charge of a software deployment, and a critical bug is discovered just before the release deadline. What steps would you take to handle this situation?

    **Solution:**
    - **Assess the Bug:** Determine the severity and impact of the bug on the system.
    - **Communicate:** Inform stakeholders about the bug and its potential impact on the release.
    - **Fix the Bug:** Allocate resources to fix the bug as quickly as possible.
    - **Test Thoroughly:** Ensure the fix is thoroughly tested to avoid any further issues.
    - **Decide on Release:** Based on the severity of the bug and the fix, decide whether to proceed with the release or delay it.
    - **Post-Release Monitoring:** If the release goes ahead, closely monitor the system for any related issues.

    **Question 4:**
    You have been assigned a new project that requires learning a new technology. How would you go about acquiring the necessary skills and ensuring the project's success?

    **Solution:**
    - **Research:** Start by understanding the basics of the new technology through online resources, tutorials, and documentation.
    - **Training:** Enroll in relevant courses or workshops to gain in-depth knowledge.
    - **Practice:** Work on small projects or exercises to apply the new skills.
    - **Seek Mentorship:** Connect with experts or colleagues who have experience with the technology for guidance.
    - **Integrate Learning:** Gradually apply the new technology to the project while continuously learning.
    - **Stay Updated:** Keep up with the latest trends and updates in the technology.

    **Question 5:**
    Imagine you are working remotely, and you need to ensure effective communication and collaboration with your team. What strategies would you employ?

    **Solution:**
    - **Regular Meetings:** Schedule regular video calls for updates and discussions.
    - **Communication Tools:** Use collaboration tools like Slack, Microsoft Teams, or Zoom for seamless communication.
    - **Clear Goals:** Set clear objectives and expectations for the team.
    - **Document Sharing:** Utilize cloud storage for sharing and collaborating on documents.
    - **Status Updates:** Implement daily or weekly status updates to track progress.
    - **Encourage Openness:** Foster an environment where team members feel comfortable sharing ideas and concerns.

    """)

if __name__ == "__main__":
    main()
