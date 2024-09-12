// @ts-nocheck

function overflowMenu(subtree = document) {
  subtree.querySelectorAll("[data-overflow-menu]").forEach((menuRoot) => {
    const button = menuRoot.querySelector("[aria-haspopup]");
    const menu = menuRoot.querySelector("[role=menu]");
    const items = [...menu.querySelectorAll("[role=menuitem]")];

    const isOpen = () => !menu.hidden;

    // Set all menu items to be unfocusable initially
    items.forEach((item) => item.setAttribute("tabindex", "-1"));

    // Function to toggle the menu open or closed
    function toggleMenu(open = !isOpen()) {
      if (open) {
        menu.hidden = false;
        button.setAttribute("aria-expanded", "true");
        items[0].focus(); // Focus on the first menu item when opened
      } else {
        menu.hidden = true;
        button.setAttribute("aria-expanded", "false");
      }
    }

    // Initialize the menu based on its current state
    toggleMenu(isOpen());

    // Toggle the menu when clicking the button
    button.addEventListener("click", () => toggleMenu());

    // Handle click-away (click outside to close the menu)
    window.addEventListener("click", function clickAway(event) {
      if (!menuRoot.isConnected) {
        window.removeEventListener("click", clickAway);
      }
      if (!menuRoot.contains(event.target)) {
        toggleMenu(false);
      }
    });

    // Get the current focused item index within the menu
    const currentIndex = () => {
      const idx = items.indexOf(document.activeElement);
      if (idx === -1) return 0;
      return idx;
    };

    // Handle keyboard interactions
    menuRoot.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "ArrowUp":
          e.preventDefault();
          items[currentIndex() - 1]?.focus();
          break;
        case "ArrowDown":
          e.preventDefault();
          items[currentIndex() + 1]?.focus();
          break;
        case "Space":
        case "Enter":
          e.preventDefault();
          items[currentIndex()].click();
          break;
        case "Home":
          e.preventDefault();
          items[0].focus();
          break;
        case "End":
          e.preventDefault();
          items[items.length - 1].focus();
          break;
        case "Escape":
          toggleMenu(false);
          button.focus();
          break;
        case "Tab":
          toggleMenu(false);
          break;
      }
    });

    // Use `focusout` instead of `blur` to handle when focus moves out of the menu
    menuRoot.addEventListener("focusout", (e) => {
      // If the new focused element is outside the menu, close it
      if (!menuRoot.contains(e.relatedTarget)) {
        toggleMenu(false);
      }
    });
  });
}

// Trigger overflowMenu on 'htmx:load' event
addEventListener("htmx:load", (e) => overflowMenu(e.target));
