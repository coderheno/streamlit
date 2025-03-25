import streamlit as st
import pandas as pd
import streamlit as st

def submission_and_feedback():
    """Streamlit function to display submission and feedback details along with video production tools and stages."""
    
    st.header("🎥 Video Production Stages")
    st.write("""
    **1. Pre-Production**:
    - This is the planning phase of the production process. It includes the development of the script, storyboarding, and preparing all the necessary elements for shooting.
    - **Tools**: 
        - **Scriptwriting Software** like **Celtx** or **Final Draft** to help structure your script.
        - **Storyboarding Tools** like **Storyboard That** or **Canva** to visualize your scenes.
        - **Location Scouting** using tools like **Shot Lister**.

    **2. Production**:
    - The shooting phase where the video is filmed.
    - **Tools**: 
        - **Teleprompter Apps** like **PromptSmart** or **Teleprompter Pro** help you read your script while looking directly into the camera, making your delivery smoother and more natural.
        - **Camera Equipment**: A DSLR or Mirrorless Camera is ideal for high-quality video. For a more budget-friendly option, **smartphones** with high-resolution cameras work too.
        - **Lighting Tools**: Softbox lighting or ring lights, such as **Neewer** or **Elgato Key Light**, to ensure your face is well-lit and visually appealing.

    **3. Post-Production**:
    - The editing phase where all the footage is put together, refined, and finalized.
    - **Tools**:
        - **Editing Software**: **Adobe Premiere Pro**, **Final Cut Pro**, or **DaVinci Resolve** for professional-level editing. For beginners, **Camedica** or **Filmora** can be good alternatives.
        - **Color Grading Tools**: Use tools like **FilmConvert** or **DaVinci Resolve** to adjust the colors and make the video look more polished.
        - **Audio Editing**: Use **Audacity** (free) or **Adobe Audition** for noise reduction, equalization, and mastering the audio.
        - **Text and Animation**: **After Effects** or **Camtasia** can be used for adding titles, transitions, and animations to enhance the video.

    **4. Feedback & Review**:
    - After post-production, it's important to review your video, get feedback from peers or mentors, and make necessary revisions.
    - Ask for feedback on aspects like the flow of information, pacing, and engagement. Ensure the call to action is clear and impactful.
    """)

    st.header("💻 Prompter Apps and Teleprompter Tools")
    st.write("""
    A **teleprompter** can make a significant difference in delivering your script smoothly and naturally. Here are some prompter apps you can use:
    - **PromptSmart Pro**: This is a highly recommended teleprompter app that automatically follows your speech, ensuring you don’t get stuck reading.
    - **Teleprompter Pro**: Another great app that offers a simple interface and works well for both iOS and Android devices. It also lets you control the speed of the script and add cues.
    - **Parrot Teleprompter**: A low-cost solution for small setups, with both mobile and professional use options.
    - **OnCue**: Offers a full teleprompter system that you can use to project your script onto a screen while you record.

    **Tips for Using a Teleprompter**:
    - **Practice**: Familiarize yourself with the script before recording. Even though the teleprompter follows your speech, you should feel comfortable and natural while delivering your lines.
    - **Speed**: Adjust the scrolling speed of the teleprompter to match your speaking pace. If you speak slowly, ensure the text doesn’t move too quickly.
    - **Eye Contact**: Position the teleprompter screen so it’s directly in front of the camera, ensuring that you maintain eye contact with the audience. This makes you appear more engaging and sincere.

    By using a teleprompter, you'll look more confident and professional, making it easier to deliver a smooth and impactful video.
    """)

    st.header("📁 Upload Your Files")
    st.write("""
    Once you have completed your script, video, and audio files, please upload them to the following **[Google Drive Link](https://drive.google.com/drive/folders/1NPLc70_IYDmqO5SiGF82vUIYw2CuU28G)** for assessment. Make sure your video quality is at least **1080p** for optimal viewing. The feedback will focus on areas such as:
    - Engagement and clarity of the script
    - Pacing and timing of the video
    - Audio quality and background noise
    - Visual elements (lighting, background, camera quality)
    - Overall presentation and professionalism

    After submitting, we will provide constructive feedback and suggestions for improving your content, ensuring you create a polished, professional final product.
    """)



def script_preparation_tips():
    """Streamlit function to display tips for script preparation for promo videos."""
    
    st.title("🎬 Script Preparation for Promo Videos")
    st.subheader("📜 Tips for Writing an Engaging Promo Script")

    st.write("""
    A strong, engaging script is key to creating a captivating promo video for your online course. Here are some tips to help you write an effective and impactful promo script:
    """)

    st.header("💡 Script Preparation Tips")
    st.write("""
    1. **Start Strong**:
       - **Tip**: Begin your script with a **hook** to capture attention immediately. For example, rather than using generic greetings like "Good morning" or "Hello", start with something more engaging, such as "Ready to turbocharge your web app development skills?" This piques interest right away and sets the tone for your course.
    
    2. **Focus on Benefits, Not Features**:
       - **Tip**: Instead of just listing features, highlight the **benefits** the learner will gain. For instance, instead of saying, “You will learn how to use Streamlit,” try something like, “By the end of this course, you’ll be able to build stunning web apps in minutes.”

    3. **Keep It Conversational**:
       - **Tip**: Use a **friendly and conversational tone**. Imagine you are talking to a friend, not reading from a textbook. Avoid jargon unless it’s essential, and explain terms if necessary. For example, your script starts with “In just 15 hours, this course will take you from novice to ninja,” which is clear and engaging, not overly technical.
    
    4. **Structure Your Script**:
       - **Tip**: Structure your script so it flows smoothly. Break down the content into **three sections**:
         - **Introduction**: Present the value of the course.
         - **Middle**: Explain how the course works and what the learner will gain.
         - **Conclusion**: End with a strong call to action, such as "Enroll now and become a web app development ninja!"

    5. **Engage with Visuals**:
       - **Tip**: Align the visuals with the script. For example, in your script, you mention "Random photo of coding and demonstrating code" — visuals should be complementary and not overly busy. Make sure they enhance the story rather than distract from it.

    6. **Use a Call to Action (CTA)**:
       - **Tip**: Always include a strong call to action at the end of your script. Phrases like “So, are you ready to join the Streamlit revolution?” or “Let’s embark on this exhilarating journey together” create excitement and encourage action. Your CTA should be clear, concise, and motivating.

    7. **Timing and Pacing**:
       - **Tip**: Keep an eye on your script’s length. A promo video should be brief but impactful (1 minute). Adjust the pacing to ensure you're not rushing through key points. If you're exceeding 1 minute, consider trimming down or splitting information into multiple sections.

    8. **Don’t Overcomplicate**:
       - **Tip**: Simplicity is key. Avoid complicated language or long-winded sentences. For example, instead of saying, “We’ll explore and demonstrate how to use dynamic data sources and integrate interactive elements seamlessly,” break it down into something clearer, like, “You’ll easily learn to bring your data to life with interactive elements.”
    """)

    st.header("📋 Do's and Don'ts for Scriptwriting")
    st.write("""
    **Do’s**:
    - **Do** engage your audience immediately with an exciting opening.
    - **Do** keep your sentences short and easy to follow.
    - **Do** maintain an active voice: “You’ll learn” rather than “You will be taught.”
    - **Do** include a strong closing statement to motivate learners to take action.

    **Don’ts**:
    - **Don’t** start with generic greetings like “Good morning” or “Hello, everyone.”
    - **Don’t** overload the script with technical jargon without explanations.
    - **Don’t** make it too long—aim for brevity and clarity.
    - **Don’t** leave the audience hanging—always end with a call to action!
    """)

    st.header("📑 Sample Promo Script")
    st.write("""
    Let's take a look at an example promo script. Here’s a segment from the **Streamlit Data Drive: Practical Web App Development** course script [here](https://docs.google.com/document/d/1AvY4a9nAM-j3CPZuROyGxQ3PhLoNEu1-/edit?usp=sharing&ouid=109717452376599156061&rtpof=true&sd=true):

    **Original**:
    - “Are you ready to turbocharge your web app development skills?”

    **Improved**:
    - “Ready to turbocharge your web app skills? Let’s dive into Streamlit!”

    **Original**:
    - “In just 15 hours, this course will take you from novice to ninja in Streamlit development.”

    **Improved**:
    - “In just 15 hours, you’ll go from beginner to pro, mastering the powerful tools of Streamlit development!”

    This shows how simple tweaks can make your script more engaging and motivating.
    """)
def icebreaker_activity():
    st.header("🎉 Icebreaker: Two Truths and a Lie – Learning Edition")
    st.write("""
    **Activity**: Two Truths and a Lie – Learning Edition  
    Each group will state **two real courses** they have taken (technical or non-technical) and **one fake course** (a made-up one). Others must guess which one is the lie.

    **Engagement**: This activity encourages interaction and showcases the variety of learning paths that participants have taken throughout their careers. It helps to break the ice while highlighting the diversity of learning experiences.

    **Twist**: As we go through the activity, we'll highlight that **micro-credentials** provide diverse and unique learning opportunities, just like the varied courses that everyone has experienced!
    
    **Team Formation**: Each team should have **3 members**, and they can choose their team members themselves. Once your teams are formed, you can begin sharing your courses!
    """)
def online_courses_development():
    """Streamlit function to display content for the Online Courses Development FDP."""
    
    st.title("📚 Effective Microcredentials and E-Content Strategies")
    

    # Sidebar Navigation
    st.sidebar.title("📌 Navigation")
    options = [
        "Overview", 
        "Session Breakdown & Activities", 
        "Icebreaker & Activity", 
        "Course Planner & Script Preparation", 
        "Video Shooting & Finalization", 
        "Submission & Feedback"
    ]
    choice = st.sidebar.radio("Go to Section", options)
    
    with st.container():
        if choice == "Overview":
            st.subheader("🎓 Enhance Your Skills to Create Effective Online Courses")

            st.write("""
    In this FDP, we will guide participants through the process of designing and developing **high-quality micro-credentials** and **full courses** tailored to students, professionals and alumni. These programs will be available on multiple platforms, providing flexible, scalable learning solutions.
    """)
            st.header("💡 Overview of Micro-Credentials & Full Course Development")
            st.write("""
            **Micro-Credentials** are short, stackable, and specialized learning units designed to equip professionals with specific skills or knowledge. They allow learners to enhance their qualifications in a particular area without committing to a full degree program.

            **Full Course Programs**: In addition to micro-credentials, participants will also learn how to design and offer full-fledged online courses for students, professionals and alumni. These courses will be robust, comprehensive, and can be delivered across popular platforms like **Coursera**, **edX**, **Udemy**, and **LinkedIn Learning**.

            ### Historical Background:
            The concept of micro-credentials and online courses has evolved over the past two decades, driven by advancements in technology and the increasing demand for flexible, career-focused learning. Initially, many platforms offered traditional university degrees, but with the rise of **MOOCs** (Massive Open Online Courses), micro-credentials have become more prevalent, offering targeted learning in a flexible format.

            ### Popular Platforms(Worldwide):
            Micro-credentials and full courses are offered across various platforms:
            - **Coursera**: Partners with universities to offer certifications and degrees.
            - **edX**: Offers free online courses from universities and institutions.
            - **Udemy**: A marketplace for learning and teaching online courses.
            - **LinkedIn Learning**: Provides a variety of professional courses.
            
            ### Popular Platforms(India):
            Micro-credentials and full courses are offered across various platforms in Indian context:
            - **NPTEL (National Programme on Technology Enhanced Learning)**: Government initiative offering free online courses with certification.
            - **SWAYAM**: Indian government's MOOC platform providing university-level courses for free with certification options.
            - **e-Pathshala**: An MHRD and NCERT initiative providing free digital textbooks, audiobooks, and e-learning materials.
            - **Great Learning**: Offers professional and executive education programs in AI, ML, Data Science, and more.

            ### Statistics:
            - The global market for micro-credentials is expected to grow rapidly, with projections indicating a market size of **USD 35 billion** by 2025.
            - **40%** of employers are now recognizing the value of micro-credentials for skill validation.
            - Platforms like **Coursera** and **edX** have seen exponential growth in course enrollments, with over **180 million users** combined.
            """)

            st.video("https://www.youtube.com/watch?v=wY5n3uGZ6Js")  # Sample video reference

        elif choice == "Session Breakdown & Activities":
            st.header("📝 Session Breakdown & Activities")
            session_data = pd.DataFrame({
                "Time": ["0-10 mins", "10-30 mins", "30-50 mins", "50-60 mins", "60-80 mins", "80-100 mins", "100-120 mins"],
                "Topic": [
                    "Introduction", 
                    "Icebreaker & Activity", 
                    "Course Planner & Script Preparation", 
                    "Video Shooting", 
                    "Submission & Feedback", 
                    "Wrap-Up & Discussion", 
                    "Q&A"
                ],
                "Activity": [
                    "Introduction to Online Course Development",
                    "Interactive Icebreaker: Share your thoughts on online learning",
                    "Prepare your course planner and script for micro-credentials",
                    "Learn video shooting techniques and screen presence",
                    "Submit scripts, videos, and audio files for feedback",
                    "Discussion on best practices and experiences",
                    "Q&A session for course-related inquiries"
                ]
            })
            st.table(session_data)

        elif choice == "Icebreaker & Activity":
            icebreaker_activity()
            st.write("""
            **Rules**:
            - Think of a fun, quirky course you'd love to teach.
            - Try to focus on interdisciplinary and multidisciplinary orientations.
            - Share your idea by entering it in the shared sheet [here](https://docs.google.com/spreadsheets/d/1d9OwSPF6oTi-Vt-5Nzm7FV-UtZbtsqd3clu5icxzZA0/edit?usp=sharing) (link to shared sheet).
            - Choose a random course name and theme which should target students, alumni and professionals. Bonus points/prize for creativity! 
            """)

        elif choice == "Course Planner & Script Preparation":
            st.header("📝 Course Planner & Script Preparation")
            st.write("""
            Participants will receive a detailed **Course Planner**  (**PYGENE Excel file Sample** [here](https://docs.google.com/spreadsheets/d/1rhhB333HipDj6YukVhmZqPhpAq7vdbSTxE2J2ywGJZw/edit?usp=sharing)), where you will structure your **micro-credential courses**. The planner should include:
            - **Main Topics**: Max 4.
            - **Sub-Topics**: Detailed sub-topics for each main topic.
            - **Video Content**: Total 1 hour, with individual videos of 10-15 minutes.
            - **Promo Video**: 1-minute introductory video.
            - **Assessments & Activities**: To gauge learner understanding.

            **The Lotus Blossom Method**:
            - This technique is used to expand ideas systematically. Begin with your main topic in the center and branch out with related subtopics. This method helps in brainstorming and organizing course content effectively.
            """)
            st.video("https://www.youtube.com/watch?v=eYzjM9un2p8")  # Sample video reference
            script_preparation_tips()
        elif choice == "Video Shooting & Finalization":
            st.header("🎥 Video Shooting & Finalization")
            st.write("""
            **Do’s**:
            - Make sure the lighting is good—natural light works best.
            - Speak clearly and at a steady pace.
            - Use visuals to support your points.
            - Keep your background clean and professional.

            **Don’ts**:
            - Avoid distracting noises or background activity.
            - Don’t rush through your content; ensure clarity.
            - Don’t use excessive effects or transitions; keep it simple.
            """)
            st.write(""" Sample Video- without proper preparation and practice.
            """)
            st.video("https://youtu.be/R_5Uqr0y-0s")  # Sample video reference
            st.write(""" Sample Video- Lack of practice and Fear towards first shooting.
            """)
            st.video("https://youtu.be/ox8tdHwI2PA")  # Sample video reference
            st.write(""" Sample Video- Practice, Practice and Practice.
            """)
            st.video("https://youtu.be/8SUqGk0VgYE")  # Sample video reference
        elif choice == "Submission & Feedback":
            st.header("📤 Submission & Feedback")
            st.write("""
            Once the scripts, videos, and audio files are ready, participants can upload their materials for assessment. Please use the following **[Drive Link](https://drive.google.com/drive/folders/1NPLc70_IYDmqO5SiGF82vUIYw2CuU28G?usp=sharing)** to submit your files. Feedback will be provided on improving your content for maximum impact.
            """)
            submission_and_feedback()

def main():
    st.set_page_config(page_title="Online Courses Development FDP", layout="wide")
    online_courses_development()

if __name__ == "__main__":
    main()
