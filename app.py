import streamlit as st

# Configure the page for a modern, mobile-first look
st.set_page_config(
    page_title="Vocational Student Wellness & Strategy Guide",
    page_icon="🚀",
    layout="centered"
)

# Initialize states to track navigation and inputs
if 'step' not in st.session_state:
    st.session_state.step = "welcome"
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Corrected style injection
st.markdown("<style>.stButton>button { width: 100%; border-radius: 8px; }</style>", unsafe_allow_html=True)

st.title("🚀 Vocational Student Journey Guide")
st.caption("A standalone reflective tool built to match your unique mindset, goals, and daily reality.")
st.write("---")

# ==========================================
# SCREEN: WELCOME & MAIN SCREENER
# ==========================================
if st.session_state.step == "welcome":
    st.header("Welcome to the Check-In")
    st.write(
        "No lectures, no corporate fluff, and completely anonymous. "
        "Choose the statement below that honestly describes your relationship with school right now."
    )
    
    main_profile = st.radio(
        "Where is your head at this semester?",
        [
            "🅰️ I'm just trying to survive. It's hard to find the energy to show up, get out of bed, or care.",
            "🅱️ I'm driven. I want to excel, hit big goals, level up my skills, or secure a great future."
        ]
    )
    
    st.write("")
    if st.button("Let's Go 🚀"):
        if "🅰️" in main_profile:
            st.session_state.step = "path1_step1"
        else:
            st.session_state.step = "path2_screener"
        st.rerun()

# ==========================================
# PATH 1: THE SURVIVAL ROUTE
# ==========================================
elif st.session_state.step == "path1_step1":
    st.header("🛌 Step 1: The Morning Battle")
    p1_q1 = st.multiselect(
        "When your alarm goes off for morning classes or practical labs, what usually happens? (Select all that apply)",
        [
            "I physically cannot open my eyes (I stay up way too late).",
            "I look at my phone and decide it's simply not worth the commute.",
            "I try to rush out, but transport/logistics always mess up my timing.",
            "I get up fine, but I spend the whole day running on complete empty."
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Start"):
            st.session_state.step = "welcome"
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.answers['p1_q1'] = p1_q1
            st.session_state.step = "path1_step2"
            st.rerun()

elif st.session_state.step == "path1_step2":
    st.header("🔋 Step 2: The Energy Drain")
    p1_q2 = st.multiselect(
        "Honestly, what is the biggest thing killing your vibe to show up to campus? (Select all that apply)",
        [
            "The material feels boring or irrelevant to my actual future.",
            "I am working late part-time shifts/jobs and I am exhausted.",
            "Personal or family things outside of school are draining my headspace.",
            "I don't really feel connected to my classmates or lecturers."
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path1_step1"
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.answers['p1_q2'] = p1_q2
            st.session_state.step = "path1_step3"
            st.rerun()

elif st.session_state.step == "path1_step3":
    st.header("🎮 Step 3: The Default Outlet")
    p1_q3 = st.multiselect(
        "When you decide to skip class or when you finally get home, where does your energy go? (Select all that apply)",
        [
            "Gaming, streaming, or scrolling social media deep into the night.",
            "Working outside of school to earn money.",
            "Pure, uninterrupted sleep to try and catch up.",
            "Hands-on hobbies, hanging out with friends, or just zoning out."
        ]
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path1_step2"
            st.rerun()
    with col2:
        if st.button("Generate My Survival Strategy 📋"):
            st.session_state.answers['p1_q3'] = p1_q3
            st.session_state.step = "results_path1"
            st.rerun()

# ==========================================
# PATH 2: THE EXCEL SCREENER (THE SUB-SPLIT)
# ==========================================
elif st.session_state.step == "path2_screener":
    st.header("🎯 The Driven Path")
    st.write("Love to see the ambition. To give you the right playbook, how is the journey treating you right now?")
    
    sub_profile = st.radio(
        "Be completely real:",
        [
            "🟢 Smooth sailing. I'm feeling good and want optimization strategies to crush my goals.",
            "🟡 I'm motivated, but I've hit a roadblock/obstacle that is holding me back."
        ]
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Start"):
            st.session_state.step = "welcome"
            st.rerun()
    with col2:
        if st.button("Continue ➡️"):
            if "🟢" in sub_profile:
                st.session_state.step = "path2a_step1"
            else:
                st.session_state.step = "path2b_step1"
            st.rerun()

# ==========================================
# PATH 2A: EXCEL - OPTIMIZATION ROUTE
# ==========================================
elif st.session_state.step == "path2a_step1":
    st.header("🏆 Step 1: Your Target Milestone")
    p2a_q1 = st.multiselect(
        "What is the ultimate crown you want to claim by graduation? (Select all that apply)",
        [
            "A flawless GPA and academic accolades.",
            "A high-profile internship/attachment at a dream company.",
            "Mastering elite technical skills to step straight into a premium industry role.",
            "Securing a direct and seamless pathway into further university education."
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path2_screener"
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.answers['p2a_q1'] = p2a_q1
            st.session_state.step = "path2a_step2"
            st.rerun()

elif st.session_state.step == "path2a_step2":
    st.header("⚡ Step 2: Your Productivity Engine")
    p2a_q2 = st.multiselect(
        "How do you execute your best work? (Select all that apply)",
        [
            "Strict scheduling, calendars, and reliable daily routines.",
            "Hyper-focused, spontaneous bursts of high energy when inspired.",
            "Collaborating heavily with high-performing peers and project teams.",
            "Solitary, hands-on trial and error inside the labs or workshops."
        ]
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path2a_step1"
            st.rerun()
    with col2:
        if st.button("Build My Optimization Blueprint 📊"):
            st.session_state.answers['p2a_q2'] = p2a_q2
            st.session_state.step = "results_path2a"
            st.rerun()

# ==========================================
# PATH 2B: EXCEL - STRATEGIC SUPPORT (ROADBLOCK)
# ==========================================
elif st.session_state.step == "path2b_step1":
    st.header("🚧 Step 1: The Roadblock")
    p2b_q1 = st.multiselect(
        "What is currently trying to bottleneck your potential? (Select all that apply)",
        [
            "Imposter syndrome (Worrying if my practical skills are actually industry-grade).",
            "Physical/mental exhaustion from over-scheduling (CCAs, study, work).",
            "Time friction (Heavy workshop project deadlines colliding with theory exams)."
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path2_screener"
            st.rerun()
    with col2:
        if st.button("Next ➡️"):
            st.session_state.answers['p2b_q1'] = p2b_q1
            st.session_state.step = "path2b_step2"
            st.rerun()

elif st.session_state.step == "path2b_step2":
    st.header("🔄 Step 2: Current Defense Mechanism")
    p2b_q2 = st.multiselect(
        "How are you trying to counter this pressure right now? (Select all that apply)",
        [
            "Forcing all-nighters on heavy caffeine, but the battery is running thin.",
            "Procrastinating on the major tasks because I am overthinking the outcome.",
            "Keeping it entirely to myself and trying to solo-engineer a solution."
        ]
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = "path2b_step1"
            st.rerun()
    with col2:
        if st.button("Generate Strategic Solution 💡"):
            st.session_state.answers['p2b_q2'] = p2b_q2
            st.session_state.step = "results_path2b"
            st.rerun()

# ==========================================
# DISPLAY SYSTEM: RESULTS PAGES
# ==========================================
elif st.session_state.step == "results_path1":
    st.header("📋 Your Custom Harm-Reduction Plan")
    st.info("You're in survival mode right now, and that's okay. Let's make things easier.")
    
    # Safely extract values
    ans_q1 = st.session_state.answers.get('p1_q1', [])
    ans_q2 = st.session_state.answers.get('p1_q2', [])
    ans_q3 = st.session_state.answers.get('p1_q3', [])
    
    st.subheader("💡 Strategic Advice")
    
    # Bulletproof matching logic loops
    for item in ans_q2:
        if "boring" in item.lower():
            st.success("⚙️ **The Trade Mindset:** If the theory modules feel useless, stop chasing 'passion.' Treat school like an unpaid apprenticeship. Show up, secure the minimum pass requirements for the technical cert, build muscle memory in labs, and get out into the workforce where the real money is made.")
            
    for item in ans_q3:
        if "gaming" in item.lower():
            st.warning("🎮 **The 4 AM Loop Hack:** Gaming triggers dopamine that makes sleep impossible. If you can't stop gaming, don't try to quit—just set a hard 'Screen Down' alarm 45 minutes before your bed target. Give your brain time to cool down so morning labs don't feel physically painful.")

    if st.button("🔄 Reset Check-In"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.step == "results_path2a":
    st.header("📊 Your High-Performance Blueprint")
    st.success("System Status: Firing on all cylinders. Let's maximize your ceiling.")
    
    ans_q1 = st.session_state.answers.get('p2a_q1', [])
    ans_q2 = st.session_state.answers.get('p2a_q2', [])
    
    st.subheader("🚀 Optimization Tactics")
    
    for item in ans_q1:
        if "internship" in item.lower():
            st.info("💼 **The Digital Portfolio Play:** Since you have the drive, don't wait for your institute's attachment phase. Start snapping clean photos/videos of your practical workshop fabrications or projects now. Create a simple portfolio to display your practical craftsmanship directly to employers.")
            
    for item in ans_q2:
        if "spontaneous" in item.lower():
            st.info("⚡ **Agile Sprints:** Since routines aren't your style, lean into 'Time Box Sprints'. When a burst hits, map out exactly 3 ultra-high-impact project tasks. Execute them furiously, then allow yourself to step completely away without guilt.")

    if st.button("🔄 Reset Check-In"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.step == "results_path2b":
    st.header("💡 Your Tactical Roadmap")
    st.warning("System Status: Ambitious but bottlenecked. Let's fix the friction.")
    
    ans_q1 = st.session_state.answers.get('p2b_q1', [])
    ans_q2 = st.session_state.answers.get('p2b_q2', [])
    
    st.subheader("🛠️ Strategic Adjustments")
    
    for item in ans_q1:
        if "imposter" in item.lower():
            st.error("🛡️ **Combatting Imposter Syndrome:** High achievers assume everyone else knows exactly what they are doing. They don't. Your practical competence builds via deliberate mistakes. Next lab session, focus exclusively on mastering *one* mechanical technique rather than racing to finish the module first.")
            
    for item in ans_q2:
        if "all-nighters" in item.lower():
            st.warning("🔋 **Battery Management:** All-nighters provide a temporary high but crater your cognitive abilities during manual practical tests. Trade one late study block for a solid 7-hour sleep block—the neurological focus boost will double your task-execution speed the next day.")

    if st.button("🔄 Reset Check-In"):
        st.session_state.clear()
        st.rerun()
