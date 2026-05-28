(function () {
  const storageKey = "icol-theme";
  const root = document.documentElement;

  const storage = {
    get() {
      try {
        return localStorage.getItem(storageKey);
      } catch (error) {
        return null;
      }
    },
    set(value) {
      try {
        localStorage.setItem(storageKey, value);
      } catch (error) {}
    },
  };

  const applyTheme = (theme) => {
    const isDark = theme === "dark";
    root.classList.toggle("dark", isDark);

    document.querySelectorAll("[data-theme-toggle], #theme-toggle").forEach((button) => {
      button.setAttribute("aria-pressed", String(isDark));
      button.setAttribute("aria-label", isDark ? "Alternar para modo claro" : "Alternar para modo escuro");
    });

    document.querySelectorAll("[data-theme-icon], #theme-icon").forEach((icon) => {
      icon.textContent = isDark ? "☀" : "☾";
    });
  };

  applyTheme(storage.get() || "light");

  document.addEventListener("DOMContentLoaded", () => {
    applyTheme(storage.get() || "light");

    document.querySelectorAll("[data-theme-toggle], #theme-toggle").forEach((button) => {
      button.addEventListener("click", () => {
        const nextTheme = root.classList.contains("dark") ? "light" : "dark";
        storage.set(nextTheme);
        applyTheme(nextTheme);
        window.dispatchEvent(new CustomEvent("icol-theme-change", { detail: { theme: nextTheme } }));
      });
    });
  });
})();
