import streamlit as st
import random
import time
import base64

# Page Configuration
st.set_page_config(
    page_title="For Tisha 💖",
    page_icon="💖",
    layout="centered"
)

# Function to convert local image to base64 for HTML display
def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded}"
    except:
        return ""

img1 = get_image_base64("photo1.jpeg")
img2 = get_image_base64("photo2.jpeg")
img3 = get_image_base64("photo3.jpeg")
img4 = get_image_base64("photo4.jpeg")
img5 = get_image_base64("photo5.jpeg")
img6 = get_image_base64("photo6.jpeg")

# Custom CSS for Multi-Color Glow & Global Pink Touch Effects
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #120309 0%, #2a0818 50%, #120309 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
        overflow-x: hidden;
    }

    .glowing-title {
        font-family: 'Great Vibes', cursive;
        font-size: 45px;
        text-align: center;
        animation: colorGlow 6s infinite alternate;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    @keyframes colorGlow {
        0% { color: #ffb3d9; text-shadow: 0 0 10px #ff3399, 0 0 20px #ff3399; }
        25% { color: #ffff99; text-shadow: 0 0 10px #ffcc00, 0 0 20px #ff9900; }
        50% { color: #99ffff; text-shadow: 0 0 10px #00ccff, 0 0 20px #0099ff; }
        75% { color: #ff99ff; text-shadow: 0 0 10px #cc33ff, 0 0 20px #9900cc; }
        100% { color: #ff9999; text-shadow: 0 0 10px #ff0033, 0 0 20px #cc0000; }
    }

    .sub-title {
        text-align: center;
        font-size: 14px;
        color: #e6b8c8;
        font-style: italic;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }

    div.stButton > button {
        background-color: #2b0c1b;
        color: #ff99dd;
        border: 2px solid #ff3399;
        border-radius: 12px;
        font-size: 20px;
        height: 55px;
        width: 100%;
        box-shadow: 0 0 10px rgba(255, 51, 153, 0.3);
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #ff3399;
        color: white;
        box-shadow: 0 0 20px rgba(255, 51, 153, 0.9);
    }

    .heart-bg {
        position: fixed;
        top: -10%;
        font-size: 22px;
        animation: fall 7s linear infinite;
        z-index: 998;
        pointer-events: none;
    }

    @keyframes fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
        100% { top: 105%; transform: translateX(90px) rotate(360deg); opacity: 0.2; }
    }

    .h1 { left: 8%; animation-duration: 6s; animation-delay: 0s; color: #ff3399; }
    .h2 { left: 24%; animation-duration: 8s; animation-delay: 2s; color: #ff66b2; }
    .h3 { left: 42%; animation-duration: 5s; animation-delay: 1s; color: #ff99cc; }
    .h4 { left: 62%; animation-duration: 7s; animation-delay: 3s; color: #ff0055; }
    .h5 { left: 80%; animation-duration: 6s; animation-delay: 1.5s; color: #ff3388; }
    .h6 { left: 92%; animation-duration: 9s; animation-delay: 0.5s; color: #ff99bb; }

    .rising-heart {
        position: fixed;
        bottom: -50px;
        font-size: 32px;
        animation: rise 4s ease-out forwards;
        z-index: 9999;
        pointer-events: none;
    }

    @keyframes rise {
        0% { bottom: -50px; opacity: 1; transform: scale(0.8) rotate(0deg); }
        50% { opacity: 0.9; transform: scale(1.3) rotate(20deg); }
        100% { bottom: 110vh; opacity: 0; transform: scale(1.5) rotate(-20deg); }
    }

    .gift-box {
        background: linear-gradient(145deg, #2b0c1b, #4a102f);
        border: 3px solid #ff3399;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 35px rgba(255, 51, 153, 0.8);
        margin-top: 15px;
    }
    </style>

    <div class="heart-bg h1">💖</div>
    <div class="heart-bg h2">💗</div>
    <div class="heart-bg h3">💓</div>
    <div class="heart-bg h4">🌸</div>
    <div class="heart-bg h5">💕</div>
    <div class="heart-bg h6">❤️</div>

    <!-- Enhanced Global Pink Touch Effect Script -->
    <script>
    document.addEventListener('click', function(e) {
        const pinkHearts = ['💖', '💗', '💓', '💕', '🩷', '✨', '🌸'];
        for(let i = 0; i < 9; i++) {
            const heart = document.createElement('div');
            heart.innerHTML = pinkHearts[Math.floor(Math.random() * pinkHearts.length)];
            heart.style.position = 'fixed';
            heart.style.left = (e.clientX + (Math.random() * 60 - 30)) + 'px';
            heart.style.top = (e.clientY + (Math.random() * 60 - 30)) + 'px';
            heart.style.fontSize = (Math.random() * 18 + 18) + 'px';
            heart.style.pointerEvents = 'none';
            heart.style.zIndex = '99999';
            heart.style.transition = 'all 1.4s ease-out';
            document.body.appendChild(heart);

            setTimeout(() => {
                heart.style.transform = `translate(${(Math.random() - 0.5) * 160}px, -${Math.random() * 140 + 60}px) scale(1.6) rotate(${Math.random() * 360}deg)`;
                heart.style.opacity = '0';
            }, 20);

            setTimeout(() => { heart.remove(); }, 1400);
        }
    });
    </script>
""", unsafe_allow_html=True)

def trigger_rising_hearts():
    st.markdown("""
        <div class="rising-heart" style="left: 10%;">💖</div>
        <div class="rising-heart" style="left: 25%; animation-delay: 0.3s;">💗</div>
        <div class="rising-heart" style="left: 40%; animation-delay: 0.1s;">💕</div>
        <div class="rising-heart" style="left: 55%; animation-delay: 0.4s;">💓</div>
        <div class="rising-heart" style="left: 70%; animation-delay: 0.2s;">🩷</div>
        <div class="rising-heart" style="left: 85%; animation-delay: 0.5s;">💖</div>
    """, unsafe_allow_html=True)

# Audio Player (Tomar pochhondo moto ganer file name ekhane diye dio)
audio_file = "my_song.mpeg"
try:
    st.audio(audio_file, format="audio/mp3", autoplay=True)
except:
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

# --- 1. HEADER SECTION ---
st.markdown('<div class="sub-title">✨ BEFORE ANYTHING ELSE OPENS... ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="glowing-title">A little game before your surprise... 💌</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #e6b8c8; font-size: 13px;">Tisha, match all the pairs of love to unlock something made only for you. Every match brings you closer to my heart 💖</p>', unsafe_allow_html=True)

st.write("---")

# --- 2. MATCHING PUZZLE GAME SETUP ---
if 'cards' not in st.session_state:
    emojis = ['💖', '🌹', '👑', '🎀', '💖', '🌹', '👑', '🎀']
    random.shuffle(emojis)
    st.session_state.cards = emojis
    st.session_state.revealed = [False] * 8
    st.session_state.matched = [False] * 8
    st.session_state.selected = []

st.markdown("<h3 style='text-align: center; color: #ffb3d9; font-size: 16px;'>Match all the pairs of love to unlock! 💕</h3>", unsafe_allow_html=True)

cols = st.columns(4)

for i in range(8):
    col = cols[i % 4]
    with col:
        if st.session_state.matched[i] or st.session_state.revealed[i]:
            card_label = st.session_state.cards[i]
        else:
            card_label = "❓"

        if st.button(card_label, key=f"card_{i}"):
            if not st.session_state.matched[i] and not st.session_state.revealed[i]:
                if len(st.session_state.selected) < 2:
                    st.session_state.revealed[i] = True
                    st.session_state.selected.append(i)
                    st.rerun()

# Check Matches Logic
if len(st.session_state.selected) == 2:
    idx1, idx2 = st.session_state.selected
    if st.session_state.cards[idx1] == st.session_state.cards[idx2]:
        st.session_state.matched[idx1] = True
        st.session_state.matched[idx2] = True
        st.session_state.selected = []
        st.rerun()
    else:
        time.sleep(0.8)
        st.session_state.revealed[idx1] = False
        st.session_state.revealed[idx2] = False
        st.session_state.selected = []
        st.rerun()

# --- 3. UNLOCKED CONTENT ---
if all(st.session_state.matched):
    trigger_rising_hearts()
    st.success("🎉 Yay! You unlocked the main surprise, Tisha!")
    
    st.markdown('<div class="sub-title">27 · 07 · 2026 — A DAY JUST FOR YOU</div>', unsafe_allow_html=True)
    st.markdown('<div class="glowing-title">Happy Girlfriend Day in Advance<br>Tisha 💖</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 14px; color: #e6b8c8;">For Tisha — my favourite person, today & always.<br>From the luckiest man alive — yours, always & only.</p>', unsafe_allow_html=True)
    
    st.write("---")

    # --- COMPACT PHOTO SLIDER WITH EMBEDDED BASE64 IMAGES & 2S INTERVAL ---
    st.markdown('<div class="glowing-title" style="font-size: 35px;">Why I Love You 💕</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #e6b8c8; font-size: 12px;">Some of Your Favorite Pictures — six heartbeats, one forever love...</p>', unsafe_allow_html=True)

    slider_html = f"""
        <style>
            .slider-outer {{
                max-width: 270px;
                margin: auto;
                padding: 10px;
                border-radius: 20px;
                background: #1a0510;
                border: 4px solid #ff3399;
                box-shadow: 0 0 30px #ff3399, inset 0 0 15px #ff3399;
                animation: fullFrameGlow 8s infinite;
            }}
            @keyframes fullFrameGlow {{
                0% {{ border-color: #ff3399; box-shadow: 0 0 25px #ff3399, inset 0 0 12px #ff3399; }}
                33% {{ border-color: #ff66b2; box-shadow: 0 0 25px #ff66b2, inset 0 0 12px #ff66b2; }}
                66% {{ border-color: #ff99cc; box-shadow: 0 0 25px #ff99cc, inset 0 0 12px #ff99cc; }}
                100% {{ border-color: #ff3399; box-shadow: 0 0 25px #ff3399, inset 0 0 12px #ff3399; }}
            }}
            .slide {{
                display: none;
                text-align: center;
                animation: fadeIn 0.8s ease-in-out;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0.4; transform: scale(0.97); }}
                to {{ opacity: 1; transform: scale(1); }}
            }}
            .slide img {{
                width: 100%;
                height: 330px;
                object-fit: cover;
                border-radius: 12px;
                display: block;
            }}
            .caption {{
                color: #ffb3d9;
                font-family: 'Poppins', sans-serif;
                font-size: 12px;
                font-style: italic;
                margin-top: 8px;
            }}
            .dots {{
                text-align: center;
                margin-top: 8px;
            }}
            .dot {{
                height: 7px;
                width: 7px;
                margin: 0 3px;
                background-color: #551535;
                border-radius: 50%;
                display: inline-block;
            }}
            .active-dot {{
                background-color: #ff3399;
                box-shadow: 0 0 6px #ff3399;
            }}
        </style>

        <div class="slider-outer">
            <div class="slide"><img src="{img1}"><div class="caption">Crowned with flowers, ruling my heart 🌸</div></div>
            <div class="slide"><img src="{img2}"><div class="caption">Main character energy, always ✨</div></div>
            <div class="slide"><img src="{img3}"><div class="caption">The smile that started it all ❤️</div></div>
            <div class="slide"><img src="{img4}"><div class="caption">Elegance has a name — Tisha 👑</div></div>
            <div class="slide"><img src="{img5}"><div class="caption">Grace wrapped in pink 💕</div></div>
            <div class="slide"><img src="{img6}"><div class="caption">My forever golden hour 🌅</div></div>
        </div>
        <div class="dots">
            <span class="dot"></span><span class="dot"></span><span class="dot"></span>
            <span class="dot"></span><span class="dot"></span><span class="dot"></span>
        </div>

        <script>
            let index = 0;
            autoSlide();
            function autoSlide() {{
                let slides = document.getElementsByClassName("slide");
                let dots = document.getElementsByClassName("dot");
                for (let i = 0; i < slides.length; i++) {{ slides[i].style.display = "none"; }}
                index++;
                if (index > slides.length) {{ index = 1; }}
                for (let i = 0; i < dots.length; i++) {{ dots[i].className = dots[i].className.replace(" active-dot", ""); }}
                slides[index-1].style.display = "block";
                dots[index-1].className += " active-dot";
                setTimeout(autoSlide, 2000);
            }}
        </script>
    """

    st.components.v1.html(slider_html, height=410)

    st.write("---")

    # --- LETTER SECTION WITH INCREASED HEIGHT & SCROLL TRIGGER ---
    st.markdown('<div class="glowing-title" style="font-size: 35px;">A Letter For You 💌</div>', unsafe_allow_html=True)
    
    letter_html = """
        <style>
        .glowing-letter-box {
            background: rgba(30, 8, 20, 0.9);
            border: 2px solid #ff3399;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 0 30px rgba(255, 51, 153, 0.5), inset 0 0 15px rgba(255, 51, 153, 0.2);
            margin: 10px auto;
            max-width: 600px;
            min-height: 480px;
            color: #fce4ec;
            font-family: 'Poppins', sans-serif;
            font-size: 14px;
            line-height: 1.7;
            white-space: pre-line;
            overflow-y: auto;
        }
        </style>
        <div class="glowing-letter-box" id="letterBox"></div>
        <script>
            const text = "My dearest Tisha,\\n\\nToday the world calls it Girlfriend Day — but honestly, every single day has quietly been about you for a long time now. You walked into my life and, without even trying, rearranged everything inside me. My plans, my dreams, my future — somewhere along the way, they all started including you.\\n\\nI love how you laugh with your whole heart. I love how you scold me and care for me in the same breath. I love the comfort of talking to you about everything and nothing. With you, I don't have to pretend, perform, or be anyone else — and that freedom is the greatest gift you've ever given me.\\n\\nI can't promise a life without problems. But I promise you a hand that will never let go of yours, a heart that will choose you every morning, and a love that will keep growing older — and softer — with us.\\n\\nThank you for being mine. Thank you for choosing me, on my best days and my worst ones. You are, and will always be, my favourite person, my peace, my home, my Tisha.\\n\\n— Forever yours ❤️";

            let i = 0;
            let typed = false;

            function typeWriter() {
                if (i < text.length && typed) {
                    let char = text.charAt(i);
                    if (char === '\\\\' && text.charAt(i+1) === 'n') {
                        document.getElementById("letterBox").innerHTML += '<br>';
                        i += 2;
                    } else {
                        document.getElementById("letterBox").innerHTML += char;
                        i++;
                    }
                    setTimeout(typeWriter, 12);
                }
            }

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !typed) {
                        typed = true;
                        typeWriter();
                    }
                });
            }, { threshold: 0.2 });

            observer.observe(document.getElementById("letterBox"));
        </script>
    """
    st.components.v1.html(letter_html, height=530)

    st.write("---")

    # --- THIS OR THAT QUIZ SECTION ---
    st.markdown('<div class="glowing-title" style="font-size: 35px;">This or That 💭</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #e6b8c8; font-size: 12px;">Just for fun - tap your answer.</p>', unsafe_allow_html=True)
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        if st.button("☕ Coffee", key="q1"):
            trigger_rising_hearts()
            st.success("Coffee dates with Tisha! 💕")
    with t_col2:
        if st.button("🍵 Tea", key="q2"):
            trigger_rising_hearts()
            st.success("A warm cup of tea together! 🌸")

    t_col3, t_col4 = st.columns(2)
    with t_col3:
        if st.button("🏖️ Beach", key="q3"):
            trigger_rising_hearts()
            st.success("Walking by the beach with you! 🌊")
    with t_col4:
        if st.button("⛰️ Mountains", key="q4"):
            trigger_rising_hearts()
            st.success("Mountain views and you! 🏔️")

    st.write("---")

    # --- LOVE METER SECTION ---
    st.markdown('<div class="glowing-title" style="font-size: 35px;">The Love Meter 💖</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #e6b8c8; font-size: 12px;">Press and slide your love level.</p>', unsafe_allow_html=True)
    
    love_percentage = st.slider("Love Level", 0, 100, 50, key="love_slider")
    
    if love_percentage > 50:
        trigger_rising_hearts()
    
    if love_percentage == 100:
        trigger_rising_hearts()
        st.markdown("<h3 style='text-align: center; color: #ff3399;'>100% — completely, hopelessly yours, Tisha! 💕</h3>", unsafe_allow_html=True)
    elif love_percentage > 70:
        trigger_rising_hearts()
        st.markdown("<p style='text-align: center; color: #ff99dd; font-size: 13px;'>You are definitely loved beyond words! 🥰</p>", unsafe_allow_html=True)

    st.write("---")

    # --- GRAND SURPRISE GIFT SECTION ---
    st.markdown('<div class="glowing-title" style="font-size: 35px;">A Surprise Gift 🎁</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #e6b8c8; font-size: 12px;">One special thing I\'ve been holding just for you...</p>', unsafe_allow_html=True)

    if st.button("🎁 Tap to Open Your Gift Box", key="final_gift_btn"):
        trigger_rising_hearts()
        st.balloons()
        st.markdown("""
            <div class="gift-box">
                <div style="font-size: 50px; animation: bounce 1.5s infinite;">💍 💖 🌹 👑</div>
                <h2 style="font-family: 'Great Vibes', cursive; font-size: 45px; color: #ffb3d9; text-shadow: 0 0 15px #ff3399;">
                    Will You Stay With Me Forever, Tisha? 💍
                </h2>
                <p style="color: #ffd6e7; font-size: 15px; font-style: italic;">
                    Not just today — but every single ordinary day after this one too.
                </p>
                <div style="font-size: 30px; margin-top: 15px;">💕 🩵 💛 💜 💕</div>
            </div>
        """, unsafe_allow_html=True)
        st.success("You are my favourite person, today and always. ❤️")