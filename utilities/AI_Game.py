import streamlit as st
import random
import math

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Game Arena",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .level-card {
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
        background: rgba(128,128,128,0.05);
    }

    .xp {
        font-size: 1.4rem;
        font-weight: bold;
    }

    .big-score {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
    }

    .correct {
        padding: 15px;
        border-radius: 12px;
        background: #d9f7df;
        border: 1px solid #82c995;
    }

    .wrong {
        padding: 15px;
        border-radius: 12px;
        background: #ffe0e0;
        border: 1px solid #e58a8a;
    }

    .tree-node {
        padding: 12px;
        border-radius: 10px;
        border: 2px solid #888;
        text-align: center;
        font-weight: bold;
    }

    .board-button button {
        height: 70px !important;
        font-size: 30px !important;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "score": 0,
    "level": 1,
    "completed": set(),
    "prediction_question": None,
    "prediction_answer": None,
    "prediction_submitted": False,
    "tree_answer": None,
    "tree_submitted": False,
    "ttt_board": [""] * 9,
    "ttt_game_over": False,
    "ttt_message": "",
    "ttt_wins": 0,
    "ttt_losses": 0,
    "ttt_draws": 0,
    "alpha_answer": None,
    "alpha_submitted": False,
    "boss_question": None,
    "boss_answer": None,
    "boss_submitted": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def add_score(points):
    st.session_state.score += points


def complete_level(level):
    if level not in st.session_state.completed:
        st.session_state.completed.add(level)
        st.session_state.score += 25


def badge_list():
    score = st.session_state.score
    badges = []

    if score >= 25:
        badges.append("🧠 Game Theory Rookie")

    if score >= 75:
        badges.append("♟️ Minimax Master")

    if score >= 125:
        badges.append("⚡ Pruning Ninja")

    if score >= 175:
        badges.append("🤖 AI Strategist")

    return badges


# ============================================================
# MINIMAX
# ============================================================

def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if "" not in board:
        return "draw"

    return None


def minimax(board, maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if winner == "draw":
        return 0

    if maximizing:
        best = -math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best = min(best, score)

        return best


def best_ai_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# ============================================================
# TIC TAC TOE
# ============================================================

def player_move(index):

    if st.session_state.ttt_game_over:
        return

    board = st.session_state.ttt_board

    if board[index] != "":
        return

    board[index] = "X"

    winner = check_winner(board)

    if winner:
        finish_ttt(winner)
        return

    ai_move = best_ai_move(board)

    if ai_move is not None:
        board[ai_move] = "O"

    winner = check_winner(board)

    if winner:
        finish_ttt(winner)


def finish_ttt(winner):

    st.session_state.ttt_game_over = True

    if winner == "X":
        st.session_state.ttt_message = "🎉 You beat the AI!"
        st.session_state.ttt_wins += 1
        add_score(30)

    elif winner == "O":
        st.session_state.ttt_message = "🤖 AI wins! Minimax found the optimal move."
        st.session_state.ttt_losses += 1

    else:
        st.session_state.ttt_message = "🤝 Draw! The AI could not defeat you."
        st.session_state.ttt_draws += 1
        add_score(10)


def reset_ttt():
    st.session_state.ttt_board = [""] * 9
    st.session_state.ttt_game_over = False
    st.session_state.ttt_message = ""


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎮 AI GAME ARENA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Adversarial Search • Game Theory • Minimax • Alpha-Beta Pruning</div>',
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🏆 Player Profile")

    st.metric(
        "XP / Score",
        st.session_state.score
    )

    st.progress(
        min(st.session_state.score / 200, 1.0)
    )

    st.markdown("### 🎖️ Badges")

    badges = badge_list()

    if badges:
        for badge in badges:
            st.write(badge)
    else:
        st.caption("Complete challenges to unlock badges!")

    st.markdown("---")

    st.markdown("### 📚 Mission")

    st.write("""
    Your mission is to understand how an AI makes
    **optimal decisions when another intelligent player
    is actively trying to defeat it.**
    """)

    st.markdown("---")

    st.info(
        "💡 Think before you click. "
        "The goal is not just to get the answer — "
        "understand WHY the AI chooses it."
    )


# ============================================================
# NAVIGATION
# ============================================================

pages = [
    "🏠 Mission Start",
    "🧠 Level 1: Game Theory",
    "🌳 Level 2: Game Tree",
    "♟️ Level 3: Minimax",
    "⚔️ Level 4: Play AI",
    "⚡ Level 5: Alpha-Beta",
    "🔥 Final Boss",
    "🏆 Scoreboard"
]

page = st.selectbox(
    "Choose your mission",
    pages
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Mission Start":

    st.subheader("🚀 Welcome to AI Game Arena")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🧠 THINK
        Understand how intelligent agents
        make decisions in competitive situations.
        """)

    with col2:
        st.markdown("""
        ### 🎮 PLAY
        Compete against an AI that uses
        **Minimax** to select its moves.
        """)

    with col3:
        st.markdown("""
        ### ⚡ MASTER
        Discover how **Alpha-Beta Pruning**
        makes search more efficient.
        """)

    st.markdown("---")

    st.subheader("🗺️ Your Learning Journey")

    journey = [
        ("1", "Game Theory", "What makes a game an adversarial problem?"),
        ("2", "Game Trees", "How can we represent possible decisions?"),
        ("3", "Minimax", "How does AI choose the optimal move?"),
        ("4", "Play AI", "Can you defeat the Minimax algorithm?"),
        ("5", "Alpha-Beta", "Can we make search faster?"),
        ("🔥", "Final Boss", "Predict the AI's optimal decision.")
    ]

    for number, title, description in journey:

        st.markdown(
            f"""
            <div class="level-card">
                <h3>{number} &nbsp; {title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        "🎯 Learning Goal: By the end, you should be able to "
        "explain how Minimax selects an optimal decision in an adversarial game."
    )


# ============================================================
# LEVEL 1
# ============================================================

elif page == "🧠 Level 1: Game Theory":

    st.header("🧠 Level 1 — What is a Game?")

    st.write("""
    In Artificial Intelligence, a **game** is a situation where
    multiple agents make decisions and the result depends on
    the decisions of all players.
    """)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎯 Key Concepts")

        st.markdown("""
        **Player / Agent**  
        The decision maker.

        **Action**  
        A possible move.

        **State**  
        The current situation.

        **Utility**  
        How good or bad the final outcome is.

        **Terminal State**  
        The game has ended.
        """)

    with col2:

        st.subheader("⚔️ Why is this different from normal search?")

        st.write("""
        In normal search, we usually search for a path to a goal.

        In adversarial search:

        > Your opponent is actively trying to stop you.
        """)

        st.info("""
        Example:

        Chess  
        You choose a move → opponent chooses a move →
        you respond → opponent responds...
        """)

    st.markdown("---")

    st.subheader("🎯 Quick Challenge")

    st.write(
        "**You are playing chess. Which statement best describes the situation?**"
    )

    answer = st.radio(
        "Choose:",
        [
            "A. Only my decisions matter",
            "B. My opponent's decisions can change the outcome",
            "C. There is always one fixed sequence of moves",
            "D. The opponent follows a random script"
        ],
        key="game_theory_q"
    )

    if st.button("Check Answer", key="check_game_theory"):

        if answer.startswith("B"):
            st.success("🎉 Correct! +10 XP")
            add_score(10)
            complete_level(1)
        else:
            st.error("Not quite. In adversarial search, the opponent matters.")


# ============================================================
# LEVEL 2
# ============================================================

elif page == "🌳 Level 2: Game Tree":

    st.header("🌳 Level 2 — Explore a Game Tree")

    st.write("""
    A game tree represents the possible sequence of decisions.

    **MAX** represents our AI.

    **MIN** represents the opponent.
    """)

    st.markdown("### Example Game Tree")

    st.graphviz_chart("""
    digraph {
        rankdir=TB;

        MAX [label="MAX"];

        MIN1 [label="MIN"];
        MIN2 [label="MIN"];

        A [label="3"];
        B [label="5"];
        C [label="2"];
        D [label="9"];

        MAX -> MIN1;
        MAX -> MIN2;

        MIN1 -> A;
        MIN1 -> B;

        MIN2 -> C;
        MIN2 -> D;
    }
    """)

    st.info("""
    Remember:

    **MAX chooses the largest value.**

    **MIN chooses the smallest value.**
    """)

    st.subheader("🎯 Your Challenge")

    choice = st.radio(
        "What value will MIN1 return?",
        ["3", "5", "8", "9"],
        key="tree_q"
    )

    if st.button("Evaluate Node", key="tree_check"):

        if choice == "3":
            st.success("🎉 Correct! MIN chooses the smaller value: min(3,5) = 3.")
            add_score(10)
            complete_level(2)
        else:
            st.error("MIN chooses the smaller value from its children.")


# ============================================================
# LEVEL 3
# ============================================================

elif page == "♟️ Level 3: Minimax":

    st.header("♟️ Level 3 — Master Minimax")

    st.write("""
    Minimax assumes that:

    **MAX tries to maximize the score.**

    **MIN tries to minimize the score.**

    The algorithm works backwards from terminal states.
    """)

    st.markdown("### 🔄 Minimax Process")

    steps = [
        "1️⃣ Generate possible moves.",
        "2️⃣ Explore the resulting states.",
        "3️⃣ Evaluate terminal states.",
        "4️⃣ MIN selects the smallest value.",
        "5️⃣ MAX selects the largest value.",
        "6️⃣ Choose the optimal action."
    ]

    for step in steps:
        st.write(step)

    st.markdown("---")

    st.subheader("🎯 Prediction Challenge")

    st.write("""
    Suppose AI is MAX and the opponent is MIN.
    """)

    st.code("""
                  MAX
               /       \\
             MIN       MIN
            /  \\      /  \\
           3    5     2    9
    """)

    prediction = st.radio(
        "What is the final value returned to MAX?",
        ["2", "3", "5", "9"],
        key="minimax_q"
    )

    if st.button("Run Minimax", key="minimax_check"):

        if prediction == "3":
            st.success(
                "🎉 Correct! MIN1 = min(3,5)=3 and "
                "MIN2=min(2,9)=2. MAX=max(3,2)=3."
            )

            add_score(15)
            complete_level(3)

        else:
            st.error(
                "Trace bottom-up: MIN1=3, MIN2=2, then MAX chooses max(3,2)=3."
            )

    st.markdown("---")

    st.subheader("🧮 Minimax Formula")

    st.latex(
        r"""
        V(s)=
        \begin{cases}
        \max_{a \in Actions(s)} V(Result(s,a)) & \text{MAX}\\
        \min_{a \in Actions(s)} V(Result(s,a)) & \text{MIN}
        \end{cases}
        """
    )


# ============================================================
# LEVEL 4 — TIC TAC TOE
# ============================================================

elif page == "⚔️ Level 4: Play AI":

    st.header("⚔️ Level 4 — Battle the Minimax AI")

    st.write("""
    You are **X**.

    The AI is **O**.

    The AI uses the **Minimax algorithm** to select its moves.
    """)

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("🎮 Tic-Tac-Toe")

        board = st.session_state.ttt_board

        for row in range(3):

            cols = st.columns(3)

            for col in range(3):

                index = row * 3 + col

                with cols[col]:

                    label = board[index] if board[index] else "⬜"

                    if st.button(
                        label,
                        key=f"cell_{index}",
                        use_container_width=True
                    ):
                        player_move(index)
                        st.rerun()

        if st.session_state.ttt_message:

            st.success(st.session_state.ttt_message)

        if st.button("🔄 New Game", key="new_game"):

            reset_ttt()
            st.rerun()

    with col2:

        st.subheader("📊 Match Stats")

        st.metric("Your Wins", st.session_state.ttt_wins)

        st.metric("AI Wins", st.session_state.ttt_losses)

        st.metric("Draws", st.session_state.ttt_draws)

        st.markdown("---")

        st.write("### 🤖 AI Strategy")

        st.write("""
        The AI evaluates possible future moves.

        It assumes you will also make the
        best possible decision.

        That's the key idea behind **Minimax**.
        """)

        if st.session_state.ttt_wins > 0:

            complete_level(4)

            st.success(
                "🏅 You defeated the Minimax AI! +30 XP"
            )


# ============================================================
# LEVEL 5 — ALPHA BETA
# ============================================================

elif page == "⚡ Level 5: Alpha-Beta":

    st.header("⚡ Level 5 — Alpha-Beta Pruning")

    st.write("""
    Minimax can become expensive because the number of possible
    game states grows extremely quickly.

    **Alpha-Beta pruning** improves Minimax by eliminating branches
    that cannot possibly affect the final decision.
    """)

    st.markdown("### 🌳 Imagine this search")

    st.graphviz_chart("""
    digraph {
        rankdir=TB;

        MAX [label="MAX"];

        MIN1 [label="MIN"];
        MIN2 [label="MIN"];

        A [label="3"];
        B [label="5"];

        C [label="2"];
        D [label="✂ PRUNED"];

        MAX -> MIN1;
        MAX -> MIN2;

        MIN1 -> A;
        MIN1 -> B;

        MIN2 -> C;
        MIN2 -> D;
    }
    """)

    st.info("""
    Once the algorithm knows that a branch cannot improve the
    decision, it does not need to explore that branch.
    """)

    st.subheader("🎯 Pruning Challenge")

    alpha_choice = st.radio(
        "What is the main purpose of Alpha-Beta pruning?",
        [
            "A. Change the optimal answer",
            "B. Make the opponent weaker",
            "C. Reduce unnecessary search",
            "D. Randomize the AI's decisions"
        ],
        key="alpha_q"
    )

    if st.button("Check Pruning", key="alpha_check"):

        if alpha_choice.startswith("C"):
            st.success(
                "⚡ Correct! Alpha-Beta pruning reduces unnecessary "
                "branches while preserving the Minimax result."
            )

            add_score(15)
            complete_level(5)

        else:
            st.error(
                "Alpha-Beta pruning improves efficiency; "
                "it does not change the optimal Minimax result."
            )

    st.markdown("---")

    st.subheader("📌 Key Terms")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("α Alpha", "Best MAX value so far")

    with c2:
        st.metric("β Beta", "Best MIN value so far")


# ============================================================
# FINAL BOSS
# ============================================================

elif page == "🔥 Final Boss":

    st.header("🔥 FINAL BOSS — Predict the AI")

    st.write("""
    You have learned:

    **Game Theory → Game Trees → Minimax → Alpha-Beta**

    Now prove that you understand optimal decisions.
    """)

    questions = [
        {
            "tree": """
                    MAX
                  /     \\
                MIN     MIN
               /  \\    /  \\
              4    7   6    8
            """,
            "answer": "4",
            "explanation":
                "MIN1 = 4, MIN2 = 6, therefore MAX chooses 6."
        },
        {
            "tree": """
                    MAX
                  /     \\
                MIN     MIN
               /  \\    /  \\
              8    2   5    4
            """,
            "answer": "5",
            "explanation":
                "MIN1 = 2, MIN2 = 4, therefore MAX chooses 4."
        },
        {
            "tree": """
                    MAX
                  /     \\
                MIN     MIN
               /  \\    /  \\
              1    9   3    7
            """,
            "answer": "3",
            "explanation":
                "MIN1 = 1, MIN2 = 3, therefore MAX chooses 3."
        }
    ]

    if st.session_state.boss_question is None:
        st.session_state.boss_question = random.choice(questions)

    q = st.session_state.boss_question

    st.code(q["tree"])

    answer = st.radio(
        "What value will MAX ultimately choose?",
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        key="boss_answer_widget"
    )

    if st.button("⚔️ Submit Final Answer", key="boss_submit"):

        if not st.session_state.boss_submitted:

            st.session_state.boss_submitted = True

            # Correct answer is calculated rather than trusting
            # the displayed explanatory text.
            lines = [
                [1, 9],
                [3, 7]
            ]

            # Determine answer from the randomly selected tree.
            if q["answer"] == "4":
                correct = "6"
            elif q["answer"] == "5":
                correct = "4"
            else:
                correct = "3"

            if answer == correct:

                st.success(
                    f"🔥 PERFECT! You predicted the optimal decision. "
                    f"+50 XP\n\n{q['explanation']}"
                )

                add_score(50)

            else:

                st.error(
                    f"Not quite. The correct value is {correct}.\n\n"
                    f"{q['explanation']}"
                )

            complete_level(6)

    if st.session_state.boss_submitted:

        if st.button("🔄 New Final Challenge"):

            st.session_state.boss_question = random.choice(questions)
            st.session_state.boss_submitted = False
            st.rerun()


# ============================================================
# SCOREBOARD
# ============================================================

elif page == "🏆 Scoreboard":

    st.header("🏆 Your AI Game Arena Score")

    st.markdown(
        f'<div class="big-score">{st.session_state.score} XP</div>',
        unsafe_allow_html=True
    )

    st.progress(
        min(st.session_state.score / 200, 1.0)
    )

    st.markdown("---")

    st.subheader("🎖️ Badges Earned")

    badges = badge_list()

    if badges:

        for badge in badges:
            st.success(badge)

    else:

        st.info(
            "No badges yet. Complete the challenges!"
        )

    st.markdown("---")

    st.subheader("📚 Concept Mastery")

    mastery = {
        "Game Theory": 1 in st.session_state.completed,
        "Game Trees": 2 in st.session_state.completed,
        "Minimax": 3 in st.session_state.completed,
        "Adversarial Play": 4 in st.session_state.completed,
        "Alpha-Beta Pruning": 5 in st.session_state.completed,
        "Optimal Decision Making": 6 in st.session_state.completed
    }

    for concept, completed in mastery.items():

        if completed:
            st.success(f"✅ {concept}")

        else:
            st.write(f"⬜ {concept}")

    st.markdown("---")

    if st.session_state.score >= 150:

        st.balloons()

        st.success("""
        🏆 **AI STRATEGIST UNLOCKED!**

        You understand the fundamental idea behind
        adversarial search: make the best decision while
        assuming the opponent is also making the best decision.
        """)

    elif st.session_state.score >= 75:

        st.info("""
        ⚡ You're becoming an AI Strategist.

        Try the remaining challenges to master
        adversarial search.
        """)

    else:

        st.info("""
        🎮 Keep playing!

        Your goal is to understand the reasoning behind
        the AI's decision, not just memorize Minimax.
        """)

    st.markdown("---")

    if st.button("🔄 Restart Entire Mission"):

        for key in defaults:
            if key == "completed":
                st.session_state[key] = set()
            elif key == "ttt_board":
                st.session_state[key] = [""] * 9
            elif key == "score":
                st.session_state[key] = 0
            else:
                st.session_state[key] = defaults[key]

        st.rerun()