import streamlit as st

# Initialize session state
if 'user_dict' not in st.session_state:
    st.session_state.user_dict = {}
if 'class_dict' not in st.session_state:
    st.session_state.class_dict = {}
if 'emoji_dict' not in st.session_state:
    st.session_state.emoji_dict = {"happy": "😊", "sad": "😢", "love": "❤️"}
if 'level_progress' not in st.session_state:
    st.session_state.level_progress = {"activity1": 1, "activity2": 1}

st.title("🗝️ Python Dictionary Adventure")
st.write("Learn **Dictionaries** step by step with interactive activities!")

# Sidebar navigation
activity = st.sidebar.radio("Choose Activity", ["Home", "Crowd-Sourced Dictionary", "Emoji Translator"])

# ---------------- HOME ----------------
if activity == "Home":
    st.header("Welcome!")
    st.write("""
    **Activities Available:**
    1. Crowd-Sourced Dictionary (Learn dictionary creation, update, delete, merge)
    2. Build Your Own Emoji Translator (Learn mapping and real-world application)
    
    Complete levels to unlock new challenges!
    """)

# ---------------- ACTIVITY 1 ----------------
elif activity == "Crowd-Sourced Dictionary":
    st.header("📚 Activity 1: Crowd-Sourced Dictionary")
    st.progress(st.session_state.level_progress["activity1"]/7)

    level = st.session_state.level_progress["activity1"]

    # LEVEL 1: Create Dictionary
    if level == 1:
        st.subheader("Level 1: Create Your Dictionary")
        name = st.text_input("Enter your name")
        food = st.text_input("Enter your favorite food")
        if st.button("Create Dictionary"):
            if name and food:
                st.session_state.user_dict = {"name": name, "favorite_food": food}
                st.success(f"Dictionary created: {st.session_state.user_dict}")
                st.session_state.level_progress["activity1"] += 1
            else:
                st.warning("Please enter both name and favorite food.")

    # LEVEL 2: Access Elements
    elif level == 2:
        st.subheader("Level 2: Access Elements")
        st.write(f"Your dictionary: {st.session_state.user_dict}")
        key = st.selectbox("Choose a key to access", list(st.session_state.user_dict.keys()))
        if st.button("Show Value"):
            st.info(f"Value: {st.session_state.user_dict[key]}")
            st.session_state.level_progress["activity1"] += 1

    # LEVEL 3: Add New Key
    elif level == 3:
        st.subheader("Level 3: Add a New Key-Value Pair")
        drink = st.text_input("Enter your favorite drink")
        if st.button("Add Drink"):
            st.session_state.user_dict["favorite_drink"] = drink
            st.success(f"Updated Dictionary: {st.session_state.user_dict}")
            st.session_state.level_progress["activity1"] += 1

    # LEVEL 4: Update a Value
    elif level == 4:
        st.subheader("Level 4: Update a Value")
        update_key = st.selectbox("Select key to update", list(st.session_state.user_dict.keys()))
        new_value = st.text_input(f"Enter new value for {update_key}")
        if st.button("Update"):
            st.session_state.user_dict[update_key] = new_value
            st.success(f"Updated Dictionary: {st.session_state.user_dict}")
            st.session_state.level_progress["activity1"] += 1

    # LEVEL 5: Delete a Key
    # LEVEL 5: Delete a Key (safe)
    elif level == 5:
        st.subheader("Level 5: Delete a Key (safe)")
        user_dict = st.session_state.user_dict

    # Protect essential keys needed in Level 6
        protected = {"name", "favorite_food"}
        deletable = [k for k in user_dict.keys() if k not in protected]

        if not deletable:
            st.info("No deletable keys (protected keys hidden). Click **Next** to continue.")
            if st.button("Next"):
                st.session_state.level_progress["activity1"] += 1
        else:
            delete_key = st.selectbox("Select a key to delete (protected keys are hidden)", deletable, key="del_key")
            if st.button("Delete"):
                user_dict.pop(delete_key, None)
                st.success(f"Updated Dictionary: {user_dict}")
                st.session_state.level_progress["activity1"] += 1


    # LEVEL 6: Combine All Dictionaries
    # LEVEL 6: Combine All Dictionaries (robust)
    elif level == 6:
        st.subheader("Level 6: Combine Dictionaries (Crowd Source Simulation)")

    # Gracefully handle missing keys by asking the user to confirm them
        current_name = st.session_state.user_dict.get("name", "")
        current_food = st.session_state.user_dict.get("favorite_food", "")

        c1, c2 = st.columns(2)
        name = c1.text_input("Confirm your name", value=current_name)
        food = c2.text_input("Confirm your favorite food", value=current_food)

        if st.button("Add to Class Dictionary"):
            name = name.strip()
            food = food.strip()
            if name and food:
            # Ensure user_dict has required keys for later levels
                st.session_state.user_dict["name"] = name
                st.session_state.user_dict["favorite_food"] = food

            # Simulate 'crowd source' by adding/overwriting in class_dict
                st.session_state.class_dict[name] = food
                st.success(f"Class Dictionary: {st.session_state.class_dict}")
                st.session_state.level_progress["activity1"] += 1
            else:
                st.warning("Please provide both **name** and **favorite food** before continuing.")


    # LEVEL 7: Dictionary Methods
    elif level == 7:
        st.subheader("Level 7: Dictionary Methods")
        st.write(f"Class Dictionary: {st.session_state.class_dict}")
        if st.button("Show Keys"):
            st.info(st.session_state.class_dict.keys())
        if st.button("Show Values"):
            st.info(st.session_state.class_dict.values())
        if st.button("Show Items"):
            st.info(st.session_state.class_dict.items())
        st.success("🎉 Congratulations! You completed Activity 1!")

# ---------------- ACTIVITY 2 ----------------
elif activity == "Emoji Translator":
    st.header("😊 Activity 2: Emoji Translator")
    st.progress(st.session_state.level_progress["activity2"]/4)

    level = st.session_state.level_progress["activity2"]

    # LEVEL 1: Show Emoji Dictionary
    if level == 1:
        st.subheader("Level 1: Create and View Emoji Dictionary")
        st.write(f"Emoji Dictionary: {st.session_state.emoji_dict}")
        if st.button("Continue"):
            st.session_state.level_progress["activity2"] += 1

    # LEVEL 2: Access Emoji
    elif level == 2:
        st.subheader("Level 2: Access Emoji by Word")
        word = st.text_input("Enter a word (e.g., happy, sad, love)")
        if st.button("Show Emoji"):
            st.info(st.session_state.emoji_dict.get(word, "Emoji not found"))
            st.session_state.level_progress["activity2"] += 1

    # LEVEL 3: Translate a Sentence
    elif level == 3:
        st.subheader("Level 3: Translate a Sentence to Emojis")
        sentence = st.text_area("Enter a sentence (e.g., I am happy and in love)")
        if st.button("Translate"):
            translation = ""
            for w in sentence.split():
                translation += st.session_state.emoji_dict.get(w, w) + " "
            st.success(f"Translated: {translation}")
            st.session_state.level_progress["activity2"] += 1

    # LEVEL 4: Add New Emoji
    elif level == 4:
        st.subheader("Level 4: Add Your Own Emoji")
        new_word = st.text_input("Enter a new word")
        new_emoji = st.text_input("Enter emoji for the word")
        if st.button("Add Emoji"):
            if new_word and new_emoji:
                st.session_state.emoji_dict[new_word] = new_emoji
                st.success(f"Updated Emoji Dictionary: {st.session_state.emoji_dict}")
            else:
                st.warning("Please enter both word and emoji.")
        st.success("🎉 Congratulations! You completed Activity 2!")
