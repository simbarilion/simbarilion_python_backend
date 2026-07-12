document.addEventListener('DOMContentLoaded', () => {
    initNav();
    initScrollReveal();
    initProjectFilters();
    initParticles();
    initHeroNetwork();
    initSkillBars();
    initMediaModal();
});

function initNav() {
    const header = document.getElementById('header');
    const toggle = document.getElementById('nav-toggle');
    const menu = document.getElementById('nav-menu');
    const links = menu.querySelectorAll('.nav__link');

    window.addEventListener('scroll', () => {
        header.classList.toggle('header--scrolled', window.scrollY > 50);
    });

    toggle.addEventListener('click', () => {
        const isOpen = menu.classList.toggle('nav__menu--open');
        toggle.setAttribute('aria-expanded', isOpen);
    });

    links.forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.remove('nav__menu--open');
            toggle.setAttribute('aria-expanded', 'false');
        });
    });

    const sections = document.querySelectorAll('section[id]');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                links.forEach(link => {
                    link.classList.toggle(
                        'nav__link--active',
                        link.getAttribute('href') === `#${id}`
                    );
                });
            }
        });
    }, { rootMargin: '-40% 0px -55% 0px' });

    sections.forEach(section => observer.observe(section));
}

function initScrollReveal() {
    const elements = document.querySelectorAll(
        '.section__header, .about__card, .about__text, .skill-card, ' +
        '.timeline-card, .project-card, .contact-item, .contacts__actions'
    );

    elements.forEach(el => el.classList.add('reveal'));

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal--visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(el => observer.observe(el));
}

function initProjectFilters() {
    const filters = document.getElementById('project-filters');
    if (!filters) return;

    const buttons = filters.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.project-card');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            buttons.forEach(b => b.classList.remove('filter-btn--active'));
            btn.classList.add('filter-btn--active');

            const filter = btn.dataset.filter;

            cards.forEach(card => {
                const categories = card.dataset.categories.split(' ');
                const show = filter === 'all' || categories.includes(filter);
                card.classList.toggle('project-card--hidden', !show);
                if (show) {
                    card.classList.remove('reveal--visible');
                    requestAnimationFrame(() => card.classList.add('reveal--visible'));
                }
            });
        });
    });
}

function initSkillBars() {
    const bars = document.querySelectorAll('.skill-card__fill');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fill = entry.target;
                const level = fill.style.getPropertyValue('--level');
                fill.style.width = '0';
                requestAnimationFrame(() => {
                    fill.style.width = level;
                });
                observer.unobserve(fill);
            }
        });
    }, { threshold: 0.5 });

    bars.forEach(bar => observer.observe(bar));
}

function initHeroNetwork() {
    const canvas = document.getElementById('hero-network');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const parent = canvas.parentElement;
    let nodes = [];
    let animId;

    function resize() {
        canvas.width = parent.offsetWidth;
        canvas.height = parent.offsetHeight;
    }

    function createNodes() {
        const count = Math.min(24, Math.floor(canvas.width / 60));
        nodes = Array.from({ length: count }, () => ({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height * 0.85,
            vx: (Math.random() - 0.5) * 0.25,
            vy: (Math.random() - 0.5) * 0.15,
            radius: Math.random() * 1.5 + 1,
            color: Math.random() > 0.6 ? '#ff8c00' : '#00d4ff',
        }));
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const maxDist = 140;

        nodes.forEach(node => {
            node.x += node.vx;
            node.y += node.vy;

            if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
            if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
        });

        for (let i = 0; i < nodes.length; i++) {
            for (let j = i + 1; j < nodes.length; j++) {
                const dx = nodes[i].x - nodes[j].x;
                const dy = nodes[i].y - nodes[j].y;
                const dist = Math.hypot(dx, dy);

                if (dist < maxDist) {
                    const alpha = (1 - dist / maxDist) * 0.35;
                    ctx.beginPath();
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(nodes[j].x, nodes[j].y);
                    ctx.strokeStyle = `rgba(0, 212, 255, ${alpha})`;
                    ctx.lineWidth = 0.8;
                    ctx.stroke();
                }
            }
        }

        nodes.forEach(node => {
            ctx.beginPath();
            ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
            ctx.fillStyle = node.color;
            ctx.globalAlpha = 0.7;
            ctx.fill();
            ctx.globalAlpha = 1;
        });

        animId = requestAnimationFrame(draw);
    }

    resize();
    createNodes();
    draw();

    window.addEventListener('resize', () => {
        cancelAnimationFrame(animId);
        resize();
        createNodes();
        draw();
    });
}

function initMediaModal() {
    const modal = document.getElementById('media-modal');
    if (!modal) return;

    const titleEl = document.getElementById('media-modal-title');
    const urlEl = document.getElementById('media-modal-url');
    const contentEl = document.getElementById('media-modal-content');

    function closeModal() {
        modal.classList.remove('media-modal--open');
        modal.setAttribute('aria-hidden', 'true');
        contentEl.innerHTML = '';
        document.body.style.overflow = '';
    }

    function openModal(title, type, src, pending) {
        titleEl.textContent = title;
        urlEl.textContent = type === 'readme' ? 'project.overview' : 'project.demo';
        contentEl.innerHTML = '';

        if (type === 'video') {
            if (pending === 'true' || !src) {
                contentEl.innerHTML = `
                    <div class="media-placeholder">
                        <span class="media-placeholder__icon">🎬</span>
                        <p class="media-placeholder__text">Видеообзор скоро появится здесь</p>
                        <span class="media-placeholder__hint">// запись в процессе</span>
                    </div>`;
            } else if (src.includes('youtube.com') || src.includes('youtu.be')) {
                const embedUrl = toYouTubeEmbed(src);
                contentEl.innerHTML = `<iframe src="${embedUrl}" allowfullscreen allow="autoplay; encrypted-media"></iframe>`;
            } else if (src.includes('rutube.ru')) {
                const embedUrl = toRutubeEmbed(src);
                contentEl.innerHTML = `<iframe src="${embedUrl}" allow="clipboard-write; autoplay; encrypted-media" allowfullscreen webkitallowfullscreen mozallowfullscreen loading="lazy"></iframe>`;
                urlEl.textContent = 'rutube.ru/demo';
            } else {
                contentEl.innerHTML = `<video controls playsinline src="${src}"></video>`;
            }
        } else if (type === 'readme' && src) {
            contentEl.innerHTML = `<iframe src="${src}" title="${title}"></iframe>`;
        }

        modal.classList.add('media-modal--open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }

    function toYouTubeEmbed(url) {
        let id = '';
        if (url.includes('youtu.be/')) {
            id = url.split('youtu.be/')[1].split('?')[0];
        } else if (url.includes('v=')) {
            id = url.split('v=')[1].split('&')[0];
        } else if (url.includes('/embed/')) {
            return url;
        }
        return `https://www.youtube.com/embed/${id}`;
    }

    function toRutubeEmbed(url) {
        if (url.includes('/play/embed/')) {
            return normalizeRutubeEmbedUrl(url);
        }

        const match = url.match(/rutube\.ru\/video\/(?:private\/)?([a-f0-9]+)/i);
        if (!match) {
            return url;
        }

        const videoId = match[1];
        const accessKey = new URL(url, 'https://rutube.ru').searchParams.get('p');

        // RuTube: для видео «по ссылке» ключ добавляется через /?p= после ID
        // https://rutube.ru/play/embed/VIDEO_ID/?p=ACCESS_KEY
        if (accessKey) {
            return `https://rutube.ru/play/embed/${videoId}/?p=${encodeURIComponent(accessKey)}`;
        }

        return `https://rutube.ru/play/embed/${videoId}/`;
    }

    function normalizeRutubeEmbedUrl(url) {
        const parsed = new URL(url, 'https://rutube.ru');
        const match = parsed.pathname.match(/\/play\/embed\/([a-f0-9]+)/i);
        if (!match) {
            return url;
        }

        const videoId = match[1];
        const accessKey = parsed.searchParams.get('p');
        if (accessKey) {
            return `https://rutube.ru/play/embed/${videoId}/?p=${encodeURIComponent(accessKey)}`;
        }

        return `https://rutube.ru/play/embed/${videoId}/`;
    }

    document.querySelectorAll('.media-open').forEach(btn => {
        btn.addEventListener('click', () => {
            openModal(
                btn.dataset.mediaTitle,
                btn.dataset.mediaType,
                btn.dataset.mediaSrc,
                btn.dataset.mediaPending || 'false'
            );
        });
    });

    modal.querySelectorAll('[data-media-close]').forEach(el => {
        el.addEventListener('click', closeModal);
    });

    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && modal.classList.contains('media-modal--open')) {
            closeModal();
        }
    });
}

function initParticles() {
    const canvas = document.getElementById('particles');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let particles = [];
    let animId;

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    function createParticles() {
        const count = Math.min(60, Math.floor(window.innerWidth / 25));
        particles = Array.from({ length: count }, () => ({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 2 + 0.5,
            speedY: Math.random() * 0.3 + 0.1,
            speedX: (Math.random() - 0.5) * 0.2,
            opacity: Math.random() * 0.5 + 0.1,
            color: Math.random() > 0.7 ? '#ff8c00' : '#00d4ff',
        }));
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach(p => {
            p.y -= p.speedY;
            p.x += p.speedX;

            if (p.y < -10) {
                p.y = canvas.height + 10;
                p.x = Math.random() * canvas.width;
            }

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.opacity;
            ctx.fill();
        });

        ctx.globalAlpha = 1;
        animId = requestAnimationFrame(animate);
    }

    resize();
    createParticles();
    animate();

    window.addEventListener('resize', () => {
        resize();
        createParticles();
    });
}
