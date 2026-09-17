/* ==========================================
   NETRADR — COMPLETE JAVASCRIPT
   ========================================== */

// ===== LOADING SCREEN =====
document.addEventListener('DOMContentLoaded', () => {
    const progressFill = document.getElementById('progressFill');
    const loadingScreen = document.getElementById('loadingScreen');
    let progress = 0;

    const loadInterval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress >= 100) {
            progress = 100;
            clearInterval(loadInterval);
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
                initAnimations();
            }, 500);
        }
        progressFill.style.width = progress + '%';
    }, 200);
});

// ===== CUSTOM CURSOR =====
const cursorFollower = document.getElementById('cursorFollower');
const cursorDot = document.getElementById('cursorDot');

if (window.innerWidth > 768) {
    document.addEventListener('mousemove', (e) => {
        cursorFollower.style.left = e.clientX + 'px';
        cursorFollower.style.top = e.clientY + 'px';
        cursorDot.style.left = e.clientX + 'px';
        cursorDot.style.top = e.clientY + 'px';
    });

    document.querySelectorAll('a, button, .feature-card, .about-card, .rural-card, .team-card').forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorFollower.style.width = '60px';
            cursorFollower.style.height = '60px';
            cursorFollower.style.borderColor = 'var(--accent)';
        });
        el.addEventListener('mouseleave', () => {
            cursorFollower.style.width = '40px';
            cursorFollower.style.height = '40px';
            cursorFollower.style.borderColor = 'var(--primary)';
        });
    });
}

// ===== NAVBAR =====
const navbar = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    updateActiveNav();
});

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

// Close mobile menu on link click
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const scrollY = window.scrollY + 200;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + sectionId) {
                    link.classList.add('active');
                }
            });
        }
    });
}

function scrollToSection(id) {
    const el = document.getElementById(id);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
    }
}

// ===== SCROLL ANIMATIONS =====
function initAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay * 150);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Animate stat counters
    animateCounters();
}

// ===== COUNTER ANIMATION =====
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number[data-count]');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.dataset.count);
                let current = 0;
                const increment = target / 60;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    entry.target.textContent = Math.floor(current);
                }, 30);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));
}

// ===== 3D BACKGROUND (THREE.JS) =====
function init3DBackground() {
    const canvas = document.getElementById('bgCanvas');
    if (!canvas) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Create particles
    const particlesGeometry = new THREE.BufferGeometry();
    const particleCount = 1500;
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
        positions[i] = (Math.random() - 0.5) * 20;
        positions[i + 1] = (Math.random() - 0.5) * 20;
        positions[i + 2] = (Math.random() - 0.5) * 20;

        // Mix of purple and teal colors
        const colorChoice = Math.random();
        if (colorChoice < 0.5) {
            colors[i] = 0.39;     // R
            colors[i + 1] = 0.4;  // G
            colors[i + 2] = 0.95; // B
        } else {
            colors[i] = 0.02;
            colors[i + 1] = 0.84;
            colors[i + 2] = 0.63;
        }
    }

    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.02,
        vertexColors: true,
        transparent: true,
        opacity: 0.8,
        sizeAttenuation: true
    });

    const particles = new THREE.Points(particlesGeometry, particlesMaterial);
    scene.add(particles);

    // Create connecting lines
    const lineGeometry = new THREE.BufferGeometry();
    const linePositions = new Float32Array(300 * 3);
    for (let i = 0; i < 300 * 3; i++) {
        linePositions[i] = (Math.random() - 0.5) * 15;
    }
    lineGeometry.setAttribute('position', new THREE.BufferAttribute(linePositions, 3));

    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0x6366f1,
        transparent: true,
        opacity: 0.08
    });

    const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
    scene.add(lines);

    // Add floating geometric shapes
    const geometries = [
        new THREE.IcosahedronGeometry(0.5, 0),
        new THREE.OctahedronGeometry(0.4, 0),
        new THREE.TetrahedronGeometry(0.3, 0)
    ];

    const shapeMaterial = new THREE.MeshBasicMaterial({
        color: 0x6366f1,
        wireframe: true,
        transparent: true,
        opacity: 0.15
    });

    const shapes = [];
    for (let i = 0; i < 5; i++) {
        const geo = geometries[Math.floor(Math.random() * geometries.length)];
        const mesh = new THREE.Mesh(geo, shapeMaterial.clone());
        mesh.position.set(
            (Math.random() - 0.5) * 15,
            (Math.random() - 0.5) * 15,
            (Math.random() - 0.5) * 10
        );
        mesh.userData = {
            rotSpeed: {
                x: (Math.random() - 0.5) * 0.02,
                y: (Math.random() - 0.5) * 0.02
            },
            floatSpeed: Math.random() * 0.005 + 0.002,
            floatOffset: Math.random() * Math.PI * 2
        };
        scene.add(mesh);
        shapes.push(mesh);
    }

    camera.position.z = 8;

    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });

    function animate() {
        requestAnimationFrame(animate);

        particles.rotation.y += 0.0005;
        particles.rotation.x += 0.0002;
        lines.rotation.y += 0.0003;

        shapes.forEach(shape => {
            shape.rotation.x += shape.userData.rotSpeed.x;
            shape.rotation.y += shape.userData.rotSpeed.y;
            shape.position.y += Math.sin(Date.now() * shape.userData.floatSpeed + shape.userData.floatOffset) * 0.003;
        });

        camera.position.x += (mouseX * 0.5 - camera.position.x) * 0.02;
        camera.position.y += (-mouseY * 0.5 - camera.position.y) * 0.02;
        camera.lookAt(scene.position);

        renderer.render(scene, camera);
    }

    animate();

    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}

// ===== NEURAL NETWORK VISUALIZATION =====
function initNeuralNetworkViz() {
    const canvas = document.getElementById('nnCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = rect.width * 2;
    canvas.height = rect.height * 2;
    ctx.scale(2, 2);

    const width = rect.width;
    const height = rect.height;

    const layers = [4, 8, 12, 8, 6];
    const nodes = [];
    const connections = [];

    // Create nodes
    layers.forEach((count, layerIndex) => {
        const x = (layerIndex + 1) * (width / (layers.length + 1));
        for (let i = 0; i < count; i++) {
            const y = (i + 1) * (height / (count + 1));
            nodes.push({
                x, y,
                layer: layerIndex,
                radius: 4,
                pulse: Math.random() * Math.PI * 2,
                active: false
            });
        }
    });

    // Create connections
    let prevLayerStart = 0;
    layers.forEach((count, layerIndex) => {
        if (layerIndex > 0) {
            const prevCount = layers[layerIndex - 1];
            for (let i = 0; i < prevCount; i++) {
                for (let j = 0; j < count; j++) {
                    connections.push({
                        from: prevLayerStart - prevCount + i,
                        to: prevLayerStart + j,
                        opacity: Math.random() * 0.3 + 0.05,
                        signal: 0,
                        signalSpeed: Math.random() * 0.02 + 0.005
                    });
                }
            }
        }
        prevLayerStart += count;
    });

    let time = 0;

    function drawNN() {
        ctx.clearRect(0, 0, width, height);
        time += 0.016;

        // Draw connections
        connections.forEach(conn => {
            const fromNode = nodes[conn.from];
            const toNode = nodes[conn.to];

            conn.signal += conn.signalSpeed;
            if (conn.signal > 1) conn.signal = 0;

            ctx.beginPath();
            ctx.moveTo(fromNode.x, fromNode.y);
            ctx.lineTo(toNode.x, toNode.y);
            ctx.strokeStyle = `rgba(99, 102, 241, ${conn.opacity})`;
            ctx.lineWidth = 0.5;
            ctx.stroke();

            // Signal dot
            const signalX = fromNode.x + (toNode.x - fromNode.x) * conn.signal;
            const signalY = fromNode.y + (toNode.y - fromNode.y) * conn.signal;
            ctx.beginPath();
            ctx.arc(signalX, signalY, 1.5, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(6, 214, 160, ${0.8 - conn.signal * 0.6})`;
            ctx.fill();
        });

        // Draw nodes
        nodes.forEach(node => {
            node.pulse += 0.03;
            const pulseRadius = node.radius + Math.sin(node.pulse) * 2;

            // Glow
            ctx.beginPath();
            ctx.arc(node.x, node.y, pulseRadius + 4, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(99, 102, 241, 0.1)`;
            ctx.fill();

            // Node
            ctx.beginPath();
            ctx.arc(node.x, node.y, pulseRadius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(99, 102, 241, 0.8)`;
            ctx.fill();

            // Inner dot
            ctx.beginPath();
            ctx.arc(node.x, node.y, 2, 0, Math.PI * 2);
            ctx.fillStyle = '#06d6a0';
            ctx.fill();
        });

        requestAnimationFrame(drawNN);
    }

    drawNN();
}

// ===== HERO PARTICLES =====
function createHeroParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;

    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: absolute;
            width: ${Math.random() * 4 + 2}px;
            height: ${Math.random() * 4 + 2}px;
            background: ${Math.random() > 0.5 ? 'rgba(99, 102, 241, 0.3)' : 'rgba(6, 214, 160, 0.3)'};
            border-radius: 50%;
            top: ${Math.random() * 100}%;
            left: ${Math.random() * 100}%;
            animation: floatParticle ${Math.random() * 10 + 10}s linear infinite;
            animation-delay: ${Math.random() * 5}s;
        `;
        container.appendChild(particle);
    }

    const style = document.createElement('style');
    style.textContent = `
        @keyframes floatParticle {
            0% { transform: translateY(0) translateX(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) translateX(${Math.random() * 200 - 100}px); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}

// ===== TIMELINE PROGRESS =====
function initTimelineProgress() {
    const timeline = document.querySelector('.workflow-timeline');
    const progress = document.getElementById('timelineProgress');
    if (!timeline || !progress) return;

    window.addEventListener('scroll', () => {
        const rect = timeline.getBoundingClientRect();
        const windowHeight = window.innerHeight;

        if (rect.top < windowHeight && rect.bottom > 0) {
            const scrolled = (windowHeight - rect.top) / (rect.height + windowHeight);
            const percentage = Math.min(Math.max(scrolled * 100, 0), 100);
            progress.style.height = percentage + '%';
        }
    });
}

// ===== INITIALIZE EVERYTHING =====
init3DBackground();
createHeroParticles();
initTimelineProgress();

// Delay neural network visualization until section is visible
const nnObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            initNeuralNetworkViz();
            nnObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

const nnSection = document.getElementById('ai-engine');
if (nnSection) nnObserver.observe(nnSection);

// ===== SMOOTH SCROLL FOR ALL ANCHOR LINKS =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// ===== PAGE VISIBILITY — PAUSE ANIMATIONS WHEN TAB IS HIDDEN =====
document.addEventListener('visibilitychange', () => {
    // Three.js and canvas animations auto-pause with requestAnimationFrame
    // when tab is not visible — no extra code needed
});

console.log('%c🩺 NetraDR', 'font-size: 24px; font-weight: bold; color: #6366f1;');
console.log('%cAI-Powered Diabetic Retinopathy Screening for India', 'font-size: 12px; color: #06d6a0;');
console.log('%cSmart India Hackathon 2024', 'font-size: 10px; color: #a5b4fc;');