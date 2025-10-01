import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SINERGI",
    page_icon="🗃",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **SINERGI** adalah platform integrasi cerdas yang menghubungkan kecerdasan buatan (AI), Internet of Things (IoT), dan Big Data dalam satu ekosistem digital. SINERGI dirancang untuk memudahkan kolaborasi lintas tim, mempercepat integrasi data, serta menyediakan infrastruktur enterprise-ready untuk transformasi digital berbasis analitik, automasi, dan visualisasi canggih. Melalui fitur multi-tenant, AutoML, real-time collaboration, serta dukungan data streaming, SINERGI mendukung kebutuhan industri, peneliti, dan developer dalam membangun solusi teknologi masa depan yang transparan dan scalable.

    ---
    #### 🔮 Vision Statement
    
    Menjadi fondasi utama integrasi AI, IoT, dan Big Data di Indonesia dan dunia, dengan menyediakan platform terbuka dan adaptif yang memungkinkan kolaborasi, inovasi, dan transformasi digital di berbagai sektor. SINERGI berkomitmen untuk mempercepat adopsi teknologi pintar, memberdayakan talenta dan perusahaan, serta mewujudkan ekosistem digital yang inklusif, efisien, dan berkelanjutan.
    
   ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/sinergi)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

iframe_url = "https://sinergi.elpeef.com/"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=5, hide_bottom_px = -110, height=800)
