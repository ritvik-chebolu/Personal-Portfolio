import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fonts and Variables
css = css.replace(
    "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');",
    "@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');"
)

css = css.replace(
    """:root {
    --bg-primary: #18181b;
    /* zinc-900 */
    --bg-secondary: #27272a;
    /* zinc-800 */
    --text-primary: #f4f4f5;
    /* zinc-100 */
    --text-secondary: #a1a1aa;
    /* zinc-400 */
    --text-muted: #71717a;
    /* zinc-500 */

    --accent-indigo: #818cf8;
    --accent-cyan: #22d3ee;

    --border-color: rgba(255, 255, 255, 0.08);
    --border-hover: rgba(255, 255, 255, 0.2);

    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-bg-hover: rgba(255, 255, 255, 0.06);
    --glass-border: rgba(255, 255, 255, 0.05);
}""",
    """:root {
    --bg-primary: #18181b;
    --bg-secondary: #27272a;
    --text-primary: #f4f4f5;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;

    --accent-indigo: #226cff;
    --accent-cyan: #ff6f00;

    --border-color: #4a4a4a;
    --border-hover: #747878;

    --card-bg: #18181b;
    --card-bg-hover: #27272a;
}

[data-theme="light"] {
    --bg-primary: #fbf9f8;
    --bg-secondary: #f5f3f3;
    --text-primary: #1a1a1a;
    --text-secondary: #444748;
    --text-muted: #5f5e5e;

    --accent-indigo: #226cff;
    --accent-cyan: #ff6f00;

    --border-color: #4a4a4a;
    --border-hover: #1a1a1a;

    --card-bg: #fbf9f8;
    --card-bg-hover: #f5f3f3;
}"""
)

# 2. Font family Outfitters to Space Grotesk
css = css.replace("font-family: 'Outfit', sans-serif;", "font-family: 'Space Grotesk', sans-serif;")

# 3. Cards
css = css.replace(
"""/* Custom Card (Glassmorphism) */
.custom-card {
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 24px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.custom-card:hover {
    transform: translateY(-4px);
    background: var(--glass-bg-hover);
    border: 1px solid var(--border-hover);
    box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.4);
}""",
"""/* Custom Card (Flat Neo-Industrial) */
.custom-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 24px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.custom-card:hover {
    transform: translateY(-4px);
    background: var(--card-bg-hover);
    border: 1px solid var(--border-hover);
}"""
)

# 4. Hero Name
css = css.replace(
""".hero-name {
    font-size: 3.5rem;
    font-weight: 800;
    margin: 0 0 12px 0;
    background: linear-gradient(270deg, var(--text-primary), var(--accent-indigo), var(--accent-cyan), var(--text-primary));
    background-size: 300% 300%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientFlow 6s ease infinite;
}""",
""".hero-name {
    font-size: 3.5rem;
    font-weight: 800;
    margin: 0 0 12px 0;
    color: var(--text-primary);
}"""
)

# 5. Skills group
css = css.replace(
""".skills-group {
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s ease;
}""",
""".skills-group {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s ease;
}"""
)

# 6. Hero container
css = css.replace(
""".hero-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 60px 40px;
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    margin-bottom: 40px;
    gap: 40px;
    margin-top: 20px;
}""",
""".hero-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 60px 40px;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 24px;
    margin-bottom: 40px;
    gap: 40px;
    margin-top: 20px;
}"""
)

# 7. Button shapes & generic background
css = css.replace(
""".social-button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 16px;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.social-button:hover {
    background: var(--glass-bg-hover);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}""",
""".social-button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 16px;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 9999px;
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.social-button:hover {
    background: var(--card-bg-hover);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}"""
)

css = css.replace(
""".btn-card-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.btn-card-link:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}""",
""".btn-card-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: var(--card-bg);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 9999px;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease;
    border: 1px solid var(--border-color);
}

.btn-card-link:hover {
    background: var(--card-bg-hover);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}"""
)

css = css.replace(
""".btn-credentials {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 24px;
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 8px;
    font-weight: 500;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.2s ease;
}

.btn-credentials:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}""",
""".btn-credentials {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 24px;
    background: var(--card-bg);
    color: var(--text-primary);
    text-decoration: none !important;
    border-radius: 9999px;
    font-weight: 500;
    border: 1px solid var(--border-color);
    transition: all 0.2s ease;
}

.btn-credentials:hover {
    background: var(--card-bg-hover);
    border-color: var(--border-hover);
    transform: translateY(-2px);
}"""
)

css = css.replace(
""".cert-card {
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 24px;
    transition: all 0.3s ease;
}""",
""".cert-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 24px;
    transition: all 0.3s ease;
}"""
)

css = css.replace(
""".nav-brand {
    font-family: 'Outfit', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #f4f4f5 30%, #a1a1aa 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-decoration: none !important;
}""",
""".nav-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    text-decoration: none !important;
}"""
)

css = css.replace(
""".top-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    background: rgba(24, 24, 27, 0.85);
    /* zinc-900 with transparency */
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    z-index: 1000;
    box-sizing: border-box;
}""",
""".top-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    background: var(--bg-primary);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    z-index: 1000;
    box-sizing: border-box;
}"""
)

# Add theme toggle button CSS at the end
css += """

/* Theme Toggle Button */
.theme-toggle-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 1.2rem;
    cursor: pointer;
    transition: color 0.2s ease;
    padding: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.theme-toggle-btn:hover {
    color: var(--text-primary);
}
"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
