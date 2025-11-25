import streamlit as st

st.title("Interactive Learning Activities – Advanced Software Engineering Concepts")

st.write("""
This Streamlit app guides students through hands-on classroom activities for the following concepts:
- Software Reuse
- Component-Based Software Engineering
- Distributed Software Engineering
- Service-Oriented Architecture
- Embedded Software
- Aspect-Oriented Software Engineering
""")

menu = st.sidebar.selectbox("Select Concept",[
    "Software Reuse",
    "Component-Based Software Engineering",
    "Distributed Software Engineering",
    "Service-Oriented Architecture",
    "Embedded Software",
    "Aspect-Oriented Software Engineering"
])

if menu == "Software Reuse":
    st.header("Software Reuse – LEGO Code Blocks Activity")
    st.write("""
### Activity Instructions:
1. Form small groups.
2. Task 1: Build a system from scratch (analogous to writing new code).
3. Task 2: Build the same system using pre-made blocks (reusable components).
4. Compare time, errors, and effort.

### Reflection:
- How did reuse improve productivity?
- What reusable components can be created for your current project?
""")

if menu == "Component-Based Software Engineering":
    st.header("Component-Based Software Engineering – App Assembly Activity")
    st.write("""
### Activity Instructions:
1. You are given components: Login, Payment, Search, Orders, Profile.
2. Assemble a working app workflow using these components.
3. Draw a component diagram (use paper/draw.io).
4. Present how each component interacts.

### Reflection:
- Why are components independent?
- Which components can be reused across different apps?
""")

if menu == "Distributed Software Engineering":
    st.header("Distributed Software Engineering – Remote Team Simulation")
    st.write("""
### Activity Instructions:
1. Team members sit in different corners (simulate remote teams).
2. Communicate only through chat/Google Docs.
3. Each person handles: UI, backend, database, API, testing.
4. Integrate everything and observe challenges.

### Reflection:
- What integration issues did you face?
- How did communication limitations affect development?
""")

if menu == "Service-Oriented Architecture":
    st.header("Service-Oriented Architecture – Microservices Marketplace")
    st.write("""
### Activity Instructions:
1. Each group becomes a service: Payment, Orders, Notifications, User, Inventory.
2. Exchange request cards to simulate API calls.
3. Complete a transaction (e.g., place order).

### Reflection:
- How do services communicate?
- What makes services loosely coupled?
""")

if menu == "Embedded Software":
    st.header("Embedded Software – Smart Home Simulation")
    st.write("""
### Activity Instructions:
1. Each station is a device: smart bulb, fan, lock, sensor.
2. Receive input cards representing sensor data.
3. Decide output actions with hardware constraints.

### Reflection:
- How do constraints affect software design?
- How is embedded software different from general software?
""")

if menu == "Aspect-Oriented Software Engineering":
    st.header("Aspect-Oriented Software Engineering – Cross-Cutting Sticker Activity")
    st.write("""
### Activity Instructions:
1. Distribute function cards: Login, Checkout, Add to Cart, Update Profile.
2. Use stickers/tags for logging, security, authentication.
3. Observe repeated stickers and discuss cross-cutting concerns.
4. Introduce the AOP idea: manage concerns from one central aspect.

### Reflection:
- Why are cross-cutting concerns scattered?
- How does AOP reduce duplication?
""")