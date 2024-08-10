// Update rating select element to show current rating
const ratingSelect = document.getElementById("rating-select");
ratingSelect.value = ratingSelect.dataset.rating;

// Rating and textarea POST
const notesText = document.getElementById("notes-text");
const elements = [ratingSelect, notesText];
elements.forEach((element) =>
  element.addEventListener("focusout", function (ev) {
    const newValue = ev.target.value;
    const badgeId = element.dataset.badgeId;

    fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: badgeId,
        [ev.target.dataset.columnId]: newValue,
      }),
    });
  })
);

// General event listeners for all elements in badge details list
// const badgeDetails = document.getElementById("badge-details");
// badgeDetails.addEventListener("focusout", (ev) => {
//   const newValue = ev.target.value;
//   const badgeId = badgeDetails.dataset.badgeId;

//   fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({
//       id: badgeId,
//       [ev.target.dataset.columnId]: newValue,
//     }),
//   });
// });

// Separate logic for clause checkboxes POST
// (note that they use target.checked instead of target.value)
const checkboxes = document.getElementsByClassName("clause-checkbox");
Array.from(checkboxes).forEach((element) =>
  element.addEventListener("change", function (ev) {
    const clauseId = ev.target.dataset.clauseId;
    fetch(`http://127.0.0.1:5000/clause/${clauseId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: clauseId,
        ["complete"]: ev.target.checked,
      }),
    });
  })
);

// Datepickers POST
const datePickers = document.querySelectorAll("input[type=date]");
Array.from(datePickers).forEach((element) =>
  element.addEventListener("change", function (ev) {
    const clauseId = ev.target.dataset.clauseId;
    fetch(`http://127.0.0.1:5000/clause/${clauseId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: clauseId,
        ["date"]: ev.target.value,
      }),
    });
  })
);
