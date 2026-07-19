import streamlit as st
import streamlit.components.v1 as components
import os

# --- Path Setup ---
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Page Configuration
st.set_page_config(layout="wide", page_title="Zeinab Hassan Portfolio")

# Styling and Spacing
st.markdown("""
    <style>
        header { visibility: hidden !important; }
        [data-testid="stSidebar"] { display: none !important; }
        .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; max-width: 100% !important; }
        .stIframe { margin-bottom: -60px !important; }
        .paint-wrapper { position: relative; padding: 20px; margin-top: 0px !important; }
        .floating-shape {
            position: absolute; width: 60px; height: 60px;
            border: 2px solid #00F0FF;
            animation: float-paint 10s infinite linear;
            opacity: 0.4; z-index: 1; pointer-events: none;
        }
        @keyframes float-paint {
            0% { transform: translateY(100px) rotate(0deg); }
            100% { transform: translateY(-50px) rotate(360deg); }
        }
    </style>
""", unsafe_allow_html=True)

# --- Main Interface (3D & Matrix) ---
html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400&display=swap" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            body { margin:0; padding:0; background:#000; font-family:Arial, sans-serif; overflow: hidden; }
            #canvas-3d { position: fixed; top: 0; left: 0; z-index: 0; width: 100vw; height: 100vh; }
            #matrix-canvas { position:fixed; top:0; left:0; z-index:-1; width:100%; height:100%; }
            .content { position:absolute; top:15%; width:100%; text-align:center; z-index:2; pointer-events: none; }
            .name-text { font-family:'Arial Black', sans-serif; margin:0; line-height: 1.1; }
            .zeinab-large { font-size: 4.5em; color: #00F0FF; text-shadow: 0 0 10px #00F0FF; } 
            .hassan-small { font-size: 1.5em; color: #888888; }
            .sub-text { font-family: 'Montserrat', sans-serif; color:#ffffff; font-size:0.85em; letter-spacing:2.5px; margin-top:20px; opacity: 0.9; max-width: 750px; margin-left: auto; margin-right: auto; text-transform: uppercase; }
            .btn-container { margin-top: 35px; pointer-events: auto; }
            .btn { display: inline-block; padding: 12px 35px; margin: 0 12px; color: #00F0FF; border: 2px solid #00F0FF; text-decoration: none; font-weight: bold; text-transform: uppercase; border-radius: 5px; cursor: pointer; background: transparent; transition: all 0.3s ease; }
            .btn:hover { background: #00F0FF; color: #000; box-shadow: 0 0 15px #00F0FF; }
        </style>
    </head>
    <body>
        <canvas id="matrix-canvas"></canvas>
        <div id="canvas-3d"></div>
        <div class="content">
            <h1 class="name-text">
                <span class="zeinab-large">ZEINAB</span><br>
                <span class="hassan-small">HASSAN MOHAMMED</span>
            </h1>
            <p class="sub-text">
                VISUAL ARTIST & RESEARCHER | TEACHING ASSISTANT, FACULTY OF ART EDUCATION, DEPT. OF DRAWING AND PAINTING, HELWAN UNIVERSITY
            </p>
            <div class="btn-container">
                <a href="javascript:void(0);" onclick="window.parent.document.getElementById('painting-section').scrollIntoView({behavior: 'smooth'});" class="btn">PAINTING</a>
                <a href="javascript:void(0);" onclick="window.parent.document.getElementById('digital-section').scrollIntoView({behavior: 'smooth'});" class="btn">DIGITAL</a>
            </div>
        </div>
        <script>
            var mc = document.getElementById("matrix-canvas");
            var ctx = mc.getContext("2d");
            mc.width = window.innerWidth; mc.height = window.innerHeight;
            var matrix = "01".split(""); var fontSize = 16; var columns = mc.width / fontSize;
            var drops = []; for(var x = 0; x < columns; x++) drops[x] = 1;
            function draw() {
                ctx.fillStyle = "rgba(0, 0, 0, 0.05)"; ctx.fillRect(0, 0, mc.width, mc.height);
                ctx.fillStyle = "#00F0FF"; ctx.font = fontSize + "px monospace";
                for(var i = 0; i < drops.length; i++) {
                    var text = matrix[Math.floor(Math.random()*matrix.length)];
                    ctx.fillText(text, i*fontSize, drops[i]*fontSize);
                    if(drops[i]*fontSize > mc.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                }
            }
            setInterval(draw, 50);
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({alpha: true});
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('canvas-3d').appendChild(renderer.domElement);
            const geometry = new THREE.BoxGeometry(3.5, 3.5, 3);
            const material = new THREE.MeshBasicMaterial({color: 0x00F0FF, wireframe: true});
            const cube = new THREE.Mesh(geometry, material);
            cube.position.x = -8.5; cube.position.y = 2.5; cube.position.z = -1;
            scene.add(cube);
            camera.position.z = 8;
            function animate() {
                requestAnimationFrame(animate);
                cube.rotation.x += 0.01; cube.rotation.y += 0.01;
                renderer.render(scene, camera);
            }
            animate();
        </script>
    </body>
    </html>
"""

components.html(html_code, height=600)

# --- Painting Section ---
st.markdown("<div id='painting-section'></div>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="paint-wrapper">
            <div class="floating-shape" style="left: 10%; top: 50px;"></div>
            <div class="floating-shape" style="right: 10%; top: 150px; animation-delay: 3s; border-color: #FFD700;"></div>
        </div>
    """, unsafe_allow_html=True)

sub_view = st.query_params.get("sub", "main")

if sub_view == "main":
    # --- Painting Part ---
    st.markdown("<h2 style='color:#00F0FF; text-align:center; margin-bottom:40px;'>PAINTING ART WORK</h2>", unsafe_allow_html=True)
    projects = [
        {"name": "The Passage (2026)", "path": "painting_files/the passage project/cover.jpeg", "id": "the_passage"},
        {"name": "Portrait Studies", "path": "painting_files/portrait_studies/cover.jpeg", "id": "portrait_studies"},
        {"name": "The Fallen Body (2025)", "path": "painting_files/The Fallen Body project/cover.png", "id": "fallen_body"},
        {"name": "Lines (2025)", "path": "painting_files/Lines/cover.png", "id": "lines"},
        {"name": "Life Paths(2024)", "path": "painting_files/Life Paths/cover.jpeg", "id": "life_paths"},
        {"name": "The Tilt (2024)", "path": "painting_files/The Tilt/cover.jpeg", "id": "the_tilt"},
        {"name": "Egyptian Vision (2023)", "path": "painting_files/Egyptian_Vision_Project/cover.jpg", "id": "egyptian_vision"},
        {"name": "A Nation Born of Pain (2023)", "path": "painting_files/A Nation Born of Pain project/cover.jpeg", "id": "nation_born_of_pain"},
        {"name": "Entanglement (2022)", "path": "painting_files/Entanglement Project/cover.jpeg", "id": "entanglement"}
    ]

    cols = st.columns(9)
    for i, proj in enumerate(projects):
        with cols[i]:
            if os.path.exists(proj["path"]):
                with st.container(border=True):
                    st.image(proj["path"], use_container_width=True)
                    st.markdown(f"<h4 style='text-align:center;'>{proj['name']}</h4>", unsafe_allow_html=True)
                    if st.button(f"View Project", key=proj["id"], use_container_width=True):
                        st.query_params["sub"] = proj["id"]
                        st.rerun()

    # --- Digital Art Part ---
    st.markdown("<div id='digital-section'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#00F0FF; text-align:center; margin-bottom:40px;'>DIGITAL ART WORKS</h2>", unsafe_allow_html=True)

    digital_projects = [
     {"name": "Camera-Based Interactive", "folder": "Camera-Based Interactive Experiments", "id": "digital_camera"},
    {"name": "EEG Visualization", "folder": "EEG Visualization & Sonification Experiments", "id": "digital_eeg"},
    {"name": "Generative Art", "folder": "Generative Audio-Visual Art Experiments", "id": "digital_generative"},
]

    cols_dig = st.columns(3) 
    for i, proj in enumerate(digital_projects):
     with cols_dig[i]:
        # البحث عن صورة غلاف داخل المجلد
        folder_path = os.path.join("digital_files", proj["folder"])
        cover_path = os.path.join(folder_path, "cover.jpg") # تأكدي من وجود ملف باسم cover.jpg في كل مجلد
        
        with st.container(border=True):
            if os.path.exists(cover_path):
                st.image(cover_path, use_container_width=True)
            st.markdown(f"<h4 style='text-align:center;'>{proj['name']}</h4>", unsafe_allow_html=True)
            if st.button("View Project", key=f"btn_dig_{proj['id']}", use_container_width=True):
                st.query_params["sub"] = proj["id"]
                st.rerun()
# --- Egyptian Vision ---
elif sub_view == "egyptian_vision":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>Egyptian Vision Project</h2>", unsafe_allow_html=True)
    col_text, col_images = st.columns([1.5, 2.5])
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0;">Egyptian Vision</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2023 | 60 x 80 cm | Gouache on Paper</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd; text-align: left;">Egyptian Vision (2023) is a 60 x 80 cm gouache painting on paper that celebrates the deep bond between the Egyptian environment and the unwavering strength of the Egyptian woman.</p>
            </div>
            <div id="3d-face-container" style="width: 100%; height: 300px; margin-top: 20px;"></div>
            """, unsafe_allow_html=True)
        components.html("""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = window.parent.document.getElementById('3d-face-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true});
                renderer.setSize(400, 300);
                container.appendChild(renderer.domElement);
                const geometry = new THREE.IcosahedronGeometry(2.2, 2);
                const material = new THREE.MeshBasicMaterial({color: 0x00F0FF, wireframe: true});
                const face = new THREE.Mesh(geometry, material);
                scene.add(face);
                camera.position.z = 4;
                function animate() { requestAnimationFrame(animate); face.rotation.y += 0.01; face.rotation.x += 0.005; renderer.render(scene, camera); }
                animate();
            </script>
            """, height=300)
    with col_images:
        folder = "painting_files/Egyptian_Vision_Project"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg')) and f.lower() != "cover.jpg"]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder, img), use_container_width=True)

# --- Portrait Studies ---
elif sub_view == "portrait_studies":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>Portrait Studies</h2>", unsafe_allow_html=True)
    folder = "painting_files/portrait_studies"
    if os.path.exists(folder):
        images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg', '.png')) and f.lower() != "cover.jpeg"]
        cols = st.columns(4)
        for i, img in enumerate(images):
            with cols[i % 4]:
                st.image(os.path.join(folder, img), use_container_width=True)

# --- Entanglement ---
elif sub_view == "entanglement":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>Entanglement Project</h2>", unsafe_allow_html=True)
    col_text, col_images = st.columns([1.5, 2.5])
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0;">Entanglement</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2022 | Acrylic on Canvas</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd; text-align: left;">
                    <strong>Entanglement (2022)</strong> is a series of acrylic on canvas works, 
                    featuring two pieces in the dimensions of <strong>60 x 80 cm</strong> and <strong>50 x 70 cm</strong>. 
                    This project explores deep emotional connections, embodying the statement: 
                    <em>"For every bird, an anchor; for every heart, a beloved."</em>
                </p>
            </div>
            <div id="3d-entanglement-container" style="width: 100%; height: 300px; margin-top: 20px;"></div>
            """, unsafe_allow_html=True)
        components.html("""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = window.parent.document.getElementById('3d-entanglement-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true});
                renderer.setSize(400, 300);
                const geometry = new THREE.TorusGeometry(2.2, 1.8, 16, 100);
                const material = new THREE.MeshBasicMaterial({color: 0x00F0FF, wireframe: true});
                const torus = new THREE.Mesh(geometry, material);
                scene.add(torus);
                camera.position.z = 7;
                container.appendChild(renderer.domElement);
                function animate() { requestAnimationFrame(animate); torus.rotation.x += 0.01; torus.rotation.y += 0.005; renderer.render(scene, camera); }
                animate();
            </script>
            """, height=300)
    with col_images:
        folder = "painting_files/Entanglement Project"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg')) and f.lower() != "cover.jpeg"]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder, img), use_container_width=True)
 # --- Lines ---
elif sub_view == "lines":
    st.markdown("<h2 style='color:#FFD700; text-align:center;'>Lines (2025)</h2>", unsafe_allow_html=True)
    
    # تقسيم الصفحة: اليسار للبيانات، اليمين للميديا (فيديو وصور)
    col_text, col_media = st.columns([1, 1.5])
    
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #FFD700; margin-bottom: 20px;">
                <h3 style="color: #FFD700; margin-top: 0;">Lines</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2025 | Mixed Media</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd;">
                 
                </p>
            </div>
            """, unsafe_allow_html=True)

    with col_media:
        # مسار مجلد المشروع الحالي فقط
        project_folder = os.path.join("painting_files", "Lines")
        
        # 1. عرض الفيديو الخاص بالمشروع فقط
        video_path = os.path.join(project_folder, "Line.mp4")
        if os.path.exists(video_path):
            st.video(video_path)
        
        # 2. عرض الصور الموجودة داخل مجلد Lines فقط
        if os.path.exists(project_folder):
            # نأخذ الملفات التي تنتهي بصيغ صور ونستثني الفيديو أو أي ملفات غريبة
            images = [f for f in os.listdir(project_folder) 
                      if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            # عرض الصور في شبكة (مثلاً عمودين)
            if images:
                sub_cols = st.columns(2)
                for i, img in enumerate(images):
                    with sub_cols[i % 2]:
                        st.image(os.path.join(project_folder, img), use_container_width=True)
#life pathes
elif sub_view == "life_paths":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>Life Paths</h2>", unsafe_allow_html=True)
    
    # --- CSS للعنصر ثلاثي الأبعاد (المكعب) ---
    # هذا الكود يحدد شكل المكعب، الألوان، والحركة الدوارة
    st.markdown("""
    <style>
        /* الحاوية الرئيسية للمشهد ثلاثي الأبعاد */
        .scene {
            perspective: 600px; /* عمق المنظور */
            width: 150px;
            height: 150px;
            position: absolute; /* لوضعه بحرية */
            right: 10px; /* يبعد عن اليمين 50 بكسل */
            top: 150px; /* يبعد عن الأعلى 150 بكسل */
            z-index: 1; /* ليكون فوق الخلفية */
        }
        
        /* المكعب نفسه */
        .cube {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            animation: rotateCube 15s infinite linear; /* حركة الدوران */
        }
        
        /* وجوه المكعب */
        .cube__face {
            position: absolute;
            width: 150px;
            height: 150px;
            border: 2px solid rgba(0, 240, 255, 0.5); /* لون الحدود */
            background: rgba(0, 240, 255, 0.05); /* لون خلفية شفافة */
            display: flex;
            align-items: center;
            justify-content: center;
            color: #00F0FF;
            font-family: monospace;
            font-size: 0.8em;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3); /* تأثير توهج */
        }
        
        /* تحديد أماكن الوجوه الستة */
        .cube__face--front  { transform: rotateY(  0deg) translateZ(75px); }
        .cube__face--back   { transform: rotateY(180deg) translateZ(75px); }
        .cube__face--right  { transform: rotateY( 90deg) translateZ(75px); }
        .cube__face--left   { transform: rotateY(-90deg) translateZ(75px); }
        .cube__face--top    { transform: rotateX( 90deg) translateZ(75px); }
        .cube__face--bottom { transform: rotateX(-90deg) translateZ(75px); }
        
        /* كي‌إف ريم للدوران */
        @keyframes rotateCube {
            from { transform: translateZ(-100px) rotateX(0deg) rotateY(0deg); }
            to   { transform: translateZ(-100px) rotateX(360deg) rotateY(360deg); }
        }
        
        /* تعديل بسيط على col_images لجعل المساحة مناسبة للعنصر الجديد */
        [data-testid="column"]:nth-of-type(2) {
             position: relative;
        }
    </style>
    """, unsafe_allow_html=True)



    # توزيع الأعمدة (النص + الصور)
    col_text, col_images = st.columns([1, 3]) 
    
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0; font-size: 1.3em;">Life Paths</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2024 | Mixed Media</p>
                <p style="font-size: 1em; line-height: 1.6; color: #ddd; text-align: left;">
                    An exploration of the intricate human journeys, mapping the intersection of choice, chance, and the paths that define our existence.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
    with col_images:
        folder = "painting_files/Life Paths"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg', '.png')) and f.lower() != "cover.jpeg"]
            
            spacer, main_content = st.columns([0.1, 3.9])
            
            with main_content:
                sub_cols = st.columns(2) 
                for i, img in enumerate(images):
                    with sub_cols[i % 3]:
                        st.image(os.path.join(folder, img), use_container_width=True, output_format="JPEG")
                        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅ BACK TO PAINTING"):
        st.query_params["sub"] = "main"
        st.rerun()
# the tilt
elif sub_view == "the_tilt":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>The Tilt (2024)</h2>", unsafe_allow_html=True)
    
    col_text, col_media = st.columns([1, 1.5])
    
    with col_text:
        # 1. عرض النص
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0;">The Tilt</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2024 | Mixed Media</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd; text-align: left;">
                    <strong>The Tilt</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)

        # 2. تشغيل كود الشكل العضوي (الحاوية الآن بداخل الـ components)
        components.html("""
            <div id="organic-3d-container" style="width: 100%; height: 300px;"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = document.getElementById('organic-3d-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
                renderer.setSize(500, 100);
                container.appendChild(renderer.domElement);

                const geometry = new THREE.IcosahedronGeometry(6, 4); 
                const material = new THREE.MeshBasicMaterial({
                    color: 0x00F0FF, 
                    wireframe: true, 
                    transparent: true, 
                    opacity: 3
                });
                const organicShape = new THREE.Mesh(geometry, material);
                scene.add(organicShape);

                camera.position.z = 5;

                function animate() { 
                    requestAnimationFrame(animate); 
                    organicShape.rotation.y += 0.005; 
                    organicShape.rotation.x += 0.002;
                    const scale = 1 + Math.sin(Date.now() * 0.002) * 0.1;
                    organicShape.scale.set(scale, scale, scale);
                    renderer.render(scene, camera); 
                }
                animate();
            </script>
        """, height=500)
            
    with col_media:
        # عرض الفيديو
        video_path = os.path.join("painting_files", "The Tilt", "tilt_video.mp4")
        if os.path.exists(video_path):
            st.video(video_path)
            
        # عرض الصور
        folder = "painting_files/The Tilt"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) 
                      if f.lower().endswith(('.jpeg', '.jpg', '.png')) 
                      and f.lower() != "cover.jpeg"]
            
            # تصحيح: استخدمنا 3 أعمدة، لذا يجب استخدام [i % 3]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder, img), use_container_width=True)      

# --- The Passage ---
elif sub_view == "the_passage":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>The Passage Project</h2>", unsafe_allow_html=True)
    col_text, col_images = st.columns([1.5, 2.5])
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0;">The Passage</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2026 | 100 x 70 cm | Oil on Canvas</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd; text-align: left;">
                    <strong>The Passage (2026)</strong> is a 100 x 70 cm oil painting on canvas. 
                    The project investigates the concept of "the passage" as both a physical space and a temporal state, 
                    navigating the fluidity of transition and the bridge between internal consciousness and external reality.
                </p>
            </div>
            <div id="3d-passage-container" style="width: 100%; height: 300px; margin-top: 20px;"></div>
            """, unsafe_allow_html=True)
        components.html("""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = window.parent.document.getElementById('3d-passage-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true});
                renderer.setSize(1000, 600);
                const geometry = new THREE.TorusKnotGeometry(9.8, 0.5, 128, 16);
                const material = new THREE.MeshBasicMaterial({color: 0x00F0FF, wireframe: true});
                const shape = new THREE.Mesh(geometry, material);
                scene.add(shape);
                camera.position.z = 6;
                container.appendChild(renderer.domElement);
                function animate() { requestAnimationFrame(animate); shape.rotation.y += 0.01; shape.rotation.z += 0.01; renderer.render(scene, camera); }
                animate();
            </script>
            """, height=300)
    with col_images:
        folder = "painting_files/the passage project"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg')) and f.lower() != "cover.jpeg"]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder, img), use_container_width=True)
elif sub_view in ["digital_camera", "digital_eeg", "digital_generative"]:
    # تحديد المجلد بناءً على الـ ID
    project_map = {
        "digital_camera": "Camera-Based Interactive Experiments",
        "digital_eeg": "EEG Visualization & Sonification Experiments",
        "digital_generative": "Generative Audio-Visual Art Experiments"
    }
    base_path = r"D:\pictures\portfolio\digital_files"
    folder_name = project_map[sub_view]
    folder_path = os.path.join("digital_files", folder_name)
    
    st.markdown(f"<h2 style='color:#00F0FF; text-align:center;'>{folder_name}</h2>", unsafe_allow_html=True)
    
    col_text, col_media = st.columns([1, 2])
    
    with col_text:
        st.markdown(f"""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF;">
                <h3 style="color: #00F0FF;">About this Project</h3>
                <p>Welcome to <strong>{folder_name}</strong>. This project explores the boundaries of digital expression and new media.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("⬅ BACK TO MAIN"):
            st.query_params["sub"] = "main"
            st.rerun()

    with col_media:
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            # عرض الفيديوهات
            for f in files:
                if f.lower().endswith('.mp4'):
                    st.video(os.path.join(folder_path, f))
            # عرض الصور
            images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png')) and f.lower() != "cover.jpg"]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder_path, img), use_container_width=True)
            
    with col_media:
    # 1. استخدام المسار الكامل الصحيح الذي عرفناه سابقاً (folder_path)
    # 2. التحقق من وجود المجلد قبل محاولة القراءة
     if os.path.exists(folder_path):
        # عرض فيديوهات المشروع
        videos = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp4')]
        for v in videos:
            st.video(os.path.join(folder_path, v))
        
        # عرض صور المشروع (استثناء غطاء المشروع)
        images = [f for f in os.listdir(folder_path) 
                  if f.lower().endswith(('.jpg', '.jpeg', '.png')) 
                  and f.lower() != "cover.jpg"]
        
        if images:
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder_path, img), use_container_width=True)
        else:
            st.warning(f"عذراً، المجلد غير موجود في المسار: {folder_path}")
    

# --- The Fallen Body ---
elif sub_view == "fallen_body":
    st.markdown("<h2 style='color:#00F0FF; text-align:center;'>The Fallen Body Project</h2>", unsafe_allow_html=True)
    col_text, col_images = st.columns([1.5, 2.5])
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.3); padding: 25px; border-radius: 5px; border: 1px solid #00F0FF; margin-top: 30px;">
                <h3 style="color: #00F0FF; margin-top: 0;">The Fallen Body</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2025 | 60 x 80 cm | Oil on Canvas</p>
                <p style="font-size: 1.1em; line-height: 1.6; color: #ddd; text-align: left;">
                    The Fallen Body (2025) is a 60 x 80 cm oil painting. It explores the physical and emotional weight of falling, 
                    turning the moment of hitting the ground into a quiet and powerful piece of art.
                </p>
            </div>
            <div id="3d-fallen-container" style="width: 100%; height: 350px; margin-top: 20px;"></div>
            """, unsafe_allow_html=True)
        components.html("""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = window.parent.document.getElementById('3d-fallen-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 1.2, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
                renderer.setSize(1300, 250);
                container.appendChild(renderer.domElement);
                const geometry = new THREE.TorusKnotGeometry(5, 1, 200, 32, 2, 2);
                const material = new THREE.MeshBasicMaterial({color: 0x00F0FF, wireframe: true});
                const shape = new THREE.Mesh(geometry, material);
                scene.add(shape);
                camera.position.z = 6;
                function animate() { 
                    requestAnimationFrame(animate); 
                    shape.rotation.y += 0.005; 
                    shape.rotation.x += 0.002;
                    shape.scale.set(1 + Math.sin(Date.now()*0.001)*0.1, 1 + Math.cos(Date.now()*0.001)*0.1, 1);
                    renderer.render(scene, camera); 
                }
                animate();
            </script>
            """, height=350)
    with col_images:
        folder = "painting_files/The Fallen Body project"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg', '.png')) and f.lower() != "cover.png"]
            sub_cols = st.columns(2)
            for i, img in enumerate(images):
                with sub_cols[i % 2]:
                    st.image(os.path.join(folder, img), use_container_width=True)

# --- A Nation Born of Pain ---
elif sub_view == "nation_born_of_pain":
    st.markdown("<h2 style='color:#FF0000; text-align:center;'>A Nation Born of Pain</h2>", unsafe_allow_html=True)
    col_text, col_images = st.columns([1.5, 2.5])
    with col_text:
        st.markdown("""
            <div style="background-color: rgba(0, 0, 0, 0.4); padding: 30px; border-radius: 10px; border: 1px solid #FF0000; margin-top: 30px;">
                <h3 style="color: #FF0000; margin-top: 0;">A Nation Born of Pain</h3>
                <p style="font-size: 0.9em; color: #888; font-style: italic; margin-bottom: 15px;">2023 | Mixed Media</p>
                <p style="font-size: 1.1em; line-height: 1.8; color: #fff; font-style: italic; text-align: justify;">
                    "I was here, with every breath and every long night of pain. With every crack, parts of me eroded, 
                    and the stain grew larger. There, the pain and I were like a fetus in the womb, and from that womb, 
                    the homeland emerged. It reached out to me, offering a soul, a life, and a lifeline of insight. 
                    There, the homeland was the light, the love, the truth, the salvation, and the life."
                </p>
            </div>
            <div id="3d-nation-container" style="width: 100%; height: 300px; margin-top: 20px;"></div>
            """, unsafe_allow_html=True)
        components.html("""
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = window.parent.document.getElementById('3d-nation-container');
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, 10, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({alpha: true});
                renderer.setSize(1250, 500);
                const geometry = new THREE.SphereGeometry(30, 32, 32);
                const material = new THREE.MeshBasicMaterial({color: 0xff0000, wireframe: true});
                const sphere = new THREE.Mesh(geometry, material);
                scene.add(sphere);
                camera.position.z = 6;
                container.appendChild(renderer.domElement);
                function animate() { requestAnimationFrame(animate); sphere.rotation.y += 0.005; renderer.render(scene, camera); }
                animate();
            </script>
            """, height=300)
    with col_images:
        folder = "painting_files/A Nation Born of Pain project"
        if os.path.exists(folder):
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpeg', '.jpg')) and f.lower() != "cover.jpeg"]
            sub_cols = st.columns(2)
            for i in range(min(2, len(images))):
                with sub_cols[i]:
                    st.image(os.path.join(folder, images[i]), use_container_width=True)
            if len(images) > 2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.image(os.path.join(folder, images[2]), use_container_width=True)

# --- Button Navigation ---
st.markdown("<br><br>", unsafe_allow_html=True)
if sub_view != "main":
    if st.button("⬅️ BACK TO PAINTING"):
        st.query_params["sub"] = "main"
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)