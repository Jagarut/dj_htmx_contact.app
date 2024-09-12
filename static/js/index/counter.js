document.querySelectorAll("[data-counter]").forEach((el) => {
  const output = el.querySelector("[data-counter-output]"),
    increment = el.querySelector("[data-counter-increment]"),
    decrement = el.querySelector("[data-counter-decrement]");

  increment.addEventListener("click", incrementCounter);
  decrement.addEventListener("click", decrementCounter);

  // Function to update the counter
  function incrementCounter() {
    let currentValue = Number(output.textContent); // Safely convert to a number
    output.textContent = currentValue + 1; // Update the counter display
  }

  // Function to update the counter
  function decrementCounter() {
    let currentValue = Number(output.textContent); // Safely convert to a number
    output.textContent = currentValue - 1; // Update the counter display
  }
});
