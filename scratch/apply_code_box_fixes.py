# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fix_file(filepath):
    print(f"\n================ Processing {filepath} ================")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_len = len(content)

    # 1. Update CSS to include fallback selectors for any code-box / code-copy-btn / pre
    # Find .code-container in CSS
    old_css_pattern = """    .code-container {
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      overflow: hidden;
      margin-bottom: 0.85rem;
      background: var(--bg-code);
    }

    .code-header {
      background: #182232;
      padding: 0.35rem 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #263346;
      font-size: 0.7rem;
      font-weight: 700;
      color: #94a3b8;
      font-family: 'JetBrains Mono', monospace;
    }

    .copy-code-btn {
      background: rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 3px;
      padding: 0.12rem 0.45rem;
      font-size: 0.65rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .copy-code-btn:hover {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .code-block {
      padding: 0.75rem 0.85rem;
      margin: 0;
      overflow-x: auto;
      font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      font-size: 0.75rem;
      line-height: 1.5;
      color: #e2e8f0;
      background: #090e17;
    }
    .code-block code {
      color: inherit;
      background: transparent;
      padding: 0;
      font-family: inherit;
    }"""

    new_css_replacement = """    .code-container,
    .code-box {
      border: 1px solid #1e293b;
      border-radius: var(--radius-sm);
      overflow: hidden;
      margin-bottom: 0.85rem;
      background: #090e17;
    }

    .code-header {
      background: #182232;
      padding: 0.35rem 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #263346;
      font-size: 0.7rem;
      font-weight: 700;
      color: #94a3b8;
      font-family: 'JetBrains Mono', monospace;
    }

    .copy-code-btn,
    .code-copy-btn {
      background: rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 3px;
      padding: 0.12rem 0.45rem;
      font-size: 0.65rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .copy-code-btn:hover,
    .code-copy-btn:hover {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .code-block,
    .code-container pre,
    .code-box pre {
      padding: 0.75rem 0.85rem;
      margin: 0;
      overflow-x: auto;
      font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      font-size: 0.75rem;
      line-height: 1.5;
      color: #e2e8f0;
      background: #090e17;
    }
    .code-block code,
    .code-container pre code,
    .code-box pre code {
      color: inherit;
      background: transparent;
      padding: 0;
      font-family: inherit;
    }"""

    if old_css_pattern in content:
        content = content.replace(old_css_pattern, new_css_replacement)
        print("Updated CSS rules with unified code-box and pre selectors.")
    else:
        print("Notice: old_css_pattern not matched exactly, checking if already updated...")

    # 2. Update HTML elements:
    # Replace <div class="code-box"> with <div class="code-container">
    # Note: avoid touching dsc-box-card if any, only exact class="code-box"
    count_code_box = len(re.findall(r'<div class="code-box">', content))
    content = re.sub(r'<div class="code-box">', '<div class="code-container">', content)
    print(f"Replaced <div class=\"code-box\"> -> <div class=\"code-container\">: {count_code_box} occurrences")

    # Replace class="code-copy-btn" with class="copy-code-btn"
    count_copy_btn = len(re.findall(r'class="code-copy-btn"', content))
    content = re.sub(r'class="code-copy-btn"', 'class="copy-code-btn"', content)
    print(f"Replaced class=\"code-copy-btn\" -> class=\"copy-code-btn\": {count_copy_btn} occurrences")

    # Replace <pre> that has no class="code-block" with <pre class="code-block">
    # Specifically where <pre> is immediately followed by <code
    count_pre = len(re.findall(r'<pre>(?=\s*<code)', content))
    content = re.sub(r'<pre>(?=\s*<code)', '<pre class="code-block">', content)
    print(f"Replaced <pre> -> <pre class=\"code-block\">: {count_pre} occurrences")

    # 3. Enhance copyCode JS function to support both copyCode(this, id) and copyCode(this)
    old_copy_code = """function copyCode(btn, elementId) {
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText || el.textContent;
      navigator.clipboard.writeText(text).then(() => {
        const orig = btn.innerText;
        btn.innerText = 'Đã Copy!';
        btn.style.background = '#00bf5f';
        btn.style.borderColor = '#00bf5f';
        setTimeout(() => {
          btn.innerText = orig;
          btn.style.background = '';
          btn.style.borderColor = '';
        }, 2000);
      });
    }"""

    new_copy_code = """function copyCode(btn, elementId) {
      let text = '';
      if (elementId) {
        const el = document.getElementById(elementId);
        if (el) text = el.innerText || el.textContent;
      }
      if (!text) {
        const container = btn.closest('.code-container, .code-box');
        if (container) {
          const codeEl = container.querySelector('code, pre');
          if (codeEl) text = codeEl.innerText || codeEl.textContent;
        }
      }
      if (!text) return;
      navigator.clipboard.writeText(text).then(() => {
        const orig = btn.innerText;
        btn.innerText = 'Đã Copy!';
        btn.style.background = '#00bf5f';
        btn.style.borderColor = '#00bf5f';
        setTimeout(() => {
          btn.innerText = orig;
          btn.style.background = '';
          btn.style.borderColor = '';
        }, 2000);
      });
    }"""

    if old_copy_code in content:
        content = content.replace(old_copy_code, new_copy_code)
        print("Updated copyCode function to support container fallback.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {filepath} successfully.")

fix_file('index.html')
fix_file('BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html')
