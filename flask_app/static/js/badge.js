const ratingSelect = document.getElementById("rating-select");
ratingSelect.value = ratingSelect.dataset.rating;

const badgeDetails = document.getElementById("badge-details");
badgeDetails.addEventListener("focusout", (ev) => {
  const newValue = ev.target.value;
  const badgeId = badgeDetails.dataset.badgeId;

  fetch(`http://127.0.0.1:5000/badge/${badgeId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: badgeId,
      [ev.target.dataset.columnId]: newValue,
    }),
  });
});

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
