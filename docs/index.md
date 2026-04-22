---
comments: false
hide:
  - navigation
  - toc
---

<style>
  /* Personalization & Beauty Layer */
  .hero-gradient {
    background: radial-gradient(circle at top right, rgba(138, 43, 226, 0.1), transparent),
                radial-gradient(circle at bottom left, rgba(0, 122, 255, 0.05), transparent);
    border-radius: 24px;
    padding: 3rem 2rem;
    margin-top: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
  }

  .viki-title {
    font-weight: 900;
    font-size: 3.5rem;
    letter-spacing: -2px;
    background: linear-gradient(to right, var(--md-primary-fg-color), #bc13fe, #448aff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
  }

  .md-typeset .grid.cards > :is(ul, ol) > li {
    border-radius: 16px;
    transition: all 0.3s ease;
    border: 1px solid var(--md-default-fg-color--lightest);
  }

  .md-typeset .grid.cards > :is(ul, ol) > li:hover {
    transform: translateY(-5px);
    border-color: var(--md-primary-fg-color);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    background: var(--md-primary-fg-color--transparent);
  }

  .status-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    background: rgba(0, 200, 83, 0.1);
    color: #00c853;
    font-size: 0.8rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }
</style>

<div class="hero-gradient">
  <div class="md-grid" style="display: flex; align-items: center; gap: 3rem; flex-wrap: wrap;">
    
    <div style="flex: 1.5; min-width: 300px;">
      <div class="status-badge">● Open for collaboration</div>
      <h1 class="viki-title">Hey, I'm Viki.</h1>
      <p style="font-size: 1.25rem; line-height: 1.5; color: var(--md-default-fg-color);">
        A software enthusiast building <span style="color: var(--md-primary-fg-color); font-weight: 600;">Study Saathi</span>—my personal second brain for all things code, architecture, and logic.
      </p>
      <p style="color: var(--md-default-fg-color--light); margin-bottom: 2rem;">
        This isn't just documentation; it's a living library of my technical journey. Dig in, explore the patterns, and let's build something better together.
      </p>
      
      <div style="display: flex; gap: 15px; flex-wrap: wrap;">
        <a href="getting-started/" class="md-button md-button--primary" style="border-radius: 8px; padding: 0.6rem 2rem;">Start Exploring</a>
        <a href="https://github.com/Vikramadtya/study-saathi" class="md-button" style="display: inline-flex; align-items: center; gap: 8px; border-radius: 8px;">
        GitHub
        </a>
      </div>
    </div>

    <div style="flex: 1; min-width: 250px; text-align: center;">
      <div style="position: relative; display: inline-block;">
        <img src="https://illustrations.popsy.co/gray/fogg-uploading-1.png" width="400" style="z-index: 2; position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80%; height: 80%; background: var(--md-primary-fg-color); filter: blur(80px); opacity: 0.15; z-index: 1;"></div>
      </div>
    </div>
  </div>
</div>

---

## 🧠 The Second Brain

<div class="grid cards" markdown>

-   :material-chart-line-variant:{ .lg .middle } __Algorithmic Patterns__
    ---
    Decoding data structures and the logic of efficiency.
    [:octicons-arrow-right-24: View Notes](algorithms/)

-   :material-drawing-box:{ .lg .middle } __Design Patterns__
    ---
    Standardized solutions to architect robust software.
    [:octicons-arrow-right-24: View Notes](patterns/)

-   :material-cloud-sync:{ .lg .middle } __System Design__
    ---
    How big systems talk to each other at scale.
    [:octicons-arrow-right-24: View Notes](system-design/)

-   :material-flask-outline:{ .lg .middle } __Coding Problem Solution__
    ---
    Breakdowns of complex LeetCode and real-world bugs.
    [:octicons-arrow-right-24: View Notes](solutions/)

</div>

---

### 🌐 Beyond the Code
<div class="grid cards" markdown>

-   :material-account-circle-outline: **Portfolio**
    Visit my home on the web.
    [Let's connect :octicons-arrow-right-24:](https://www.vikramaditya-singh.in)

-   :material-feather: **Blog**
    Long-form thoughts on tech and life.
    [Read more :octicons-arrow-right-24:](https://www.neuralcook.com/home)

</div>