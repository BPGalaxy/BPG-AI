/**
 * theme-switcher.js
 * Lightweight dynamic theme switcher
 */

(function () {

  const STORAGE_KEY = 'site-theme';
  const GOLD = 'gold';

  // --------------------------
  // Theme
  // --------------------------

  function currentTheme() {
    return localStorage.getItem(STORAGE_KEY) === GOLD
      ? GOLD
      : 'purple';
  }

  function applyTheme(theme) {

    if (theme === GOLD) {
      document.documentElement.setAttribute('data-theme', GOLD);
    } else {
      document.documentElement.removeAttribute('data-theme');
    }

    localStorage.setItem(STORAGE_KEY, theme);

    updateButtons();
  }

  function toggleTheme() {
    applyTheme(
      currentTheme() === GOLD
        ? 'purple'
        : GOLD
    );
  }

  // --------------------------
  // Buttons
  // --------------------------

  function updateButtons() {

    const buttons =
      document.querySelectorAll('#theme-toggle-btn');

    const isGold =
      currentTheme() === GOLD;

    buttons.forEach(btn => {

      const inner =
        btn.querySelector('.btn-inner');

      if (isGold) {

        btn.classList.remove('purple-mode');

        if (inner) {
          inner.textContent =
            '✦ Switch to Purple';
        }

      } else {

        btn.classList.add('purple-mode');

        if (inner) {
          inner.textContent =
            '✦ Switch to Gold';
        }
      }
    });
  }

  // --------------------------
  // Click Handler
  // --------------------------

  document.addEventListener('click', (e) => {

    const btn =
      e.target.closest('#theme-toggle-btn');

    if (!btn) return;

    toggleTheme();
  });

  // --------------------------
  // Init
  // --------------------------

  applyTheme(currentTheme());

  // Tiny interval to detect newly injected buttons
  // Extremely lightweight
  setInterval(updateButtons, 500);

})();