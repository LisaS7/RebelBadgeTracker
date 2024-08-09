// ------------ EDITABLE ELEMENTS ------------
const tableDiv = document.getElementById("badge-table");

let savedValue;

tableDiv.addEventListener("focusin", (ev) => {
  if (
    ev.target.tagName === "TD" ||
    ev.target.tagName === "SELECT" ||
    ev.target.tagName === "TEXTAREA"
  ) {
    savedValue = ev.target.textContent || ev.target.value;
  }
});

tableDiv.addEventListener("focusout", (ev) => {
  let newValue;
  if (ev.target.tagName === "TD") {
    newValue = ev.target.textContent;
  }
  if (ev.target.tagName === "SELECT" || ev.target.tagName === "TEXTAREA") {
    newValue = ev.target.value;
  }

  if (newValue) {
    if (savedValue !== newValue) {
      fetch(`http://127.0.0.1:5000/badge/${ev.target.dataset.elementId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: ev.target.dataset.elementId,
          [ev.target.dataset.columnId]: newValue,
        }),
      });
    }
    savedValue = undefined;
  }
});

// ------------ POPULATE RATINGS ------------
// For some reason the dom isn't loading before this runs, so added time delay
setTimeout(function () {
  const ratingSelect = document.getElementsByClassName("ratingSelect");
  Array.from(ratingSelect).forEach((element) => {
    element.value = element.dataset.elementValue;
  });
}, 2000);
