// Update rating select element to show current rating
const ratingSelect = document.getElementById("rating-select");
ratingSelect.value = ratingSelect.dataset.rating;

// Badge details - rating, date and textarea POST
const notesText = document.getElementById("notes-text");
const badgeDate = document.getElementById("badge-date");
const elements = [ratingSelect, badgeDate, notesText];
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

// Badge complete checkbox POST
const badgeCheckbox = document.getElementById("badge-checkbox");
badgeCheckbox.addEventListener("focusout", function (ev) {
  const badgeId = badgeCheckbox.dataset.badgeId;
  fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: badgeId,
      ["complete"]: ev.target.checked,
    }),
  });
});

// Tags POST
const tagButtons = document.getElementsByClassName("tag-button");
Array.from(tagButtons).forEach((element) =>
  element.addEventListener("focusout", function (ev) {
    const field = ev.target.dataset.columnId;
    const badgeId = ev.target.dataset.badgeId;
    fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: badgeId,
        [field]: ev.target.checked,
      }),
    });
  })
);

// Edit link display input field
const editBtn = document.getElementById("edit-link-btn");
const saveBtn = document.getElementById("save-link-btn");
const inputField = document.getElementById("input-link");
const displayLink = document.getElementById("link-text");

inputField.style.display = "none";
saveBtn.style.display = "none";

editBtn.addEventListener("click", function (ev) {
  if (inputField.style.display === "none") {
    inputField.style.display = "block";
    saveBtn.style.display = "block";
    displayLink.style.display = "none";
  } else {
    inputField.style.display = "none";
    saveBtn.style.display = "none";
    displayLink.style.display = "block";
  }
});

saveBtn.addEventListener("click", function (ev) {
  const badgeId = saveBtn.dataset.badgeId;
  fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: badgeId,
      ["link"]: inputField.value,
    }),
  });
  displayLink.textContent = inputField.value;
  document.getElementById("badge-link").setAttribute("href", inputField.value);
  inputField.style.display = "none";
  saveBtn.style.display = "none";
  displayLink.style.display = "block";
});

// Clause checkboxes POST
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
const datePickers = document.getElementsByClassName("clause-date");
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
