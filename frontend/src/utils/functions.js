import { useDate } from "vuetify";

export function handleChange(ev, field, id) {
  let value = null;
  switch (field) {
    case "complete":
      value = ev.target.checked;
      break;
    case "notes":
      value = ev.target.value;
  }

  const body = {
    id,
  };
  body[field] = value;

  fetch(`http://127.0.0.1:5000/badge/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

export const colorShade = (col, amt) => {
  if (col === undefined) {
    return "grey";
  }
  col = col.replace(/^#/, "");
  if (col.length === 3)
    col = col[0] + col[0] + col[1] + col[1] + col[2] + col[2];

  let [r, g, b] = col.match(/.{2}/g);
  [r, g, b] = [
    parseInt(r, 16) + amt,
    parseInt(g, 16) + amt,
    parseInt(b, 16) + amt,
  ];

  r = Math.max(Math.min(255, r), 0).toString(16);
  g = Math.max(Math.min(255, g), 0).toString(16);
  b = Math.max(Math.min(255, b), 0).toString(16);

  const rr = (r.length < 2 ? "0" : "") + r;
  const gg = (g.length < 2 ? "0" : "") + g;
  const bb = (b.length < 2 ? "0" : "") + b;

  return `#${rr}${gg}${bb}`;
};

export function parseISODate(s) {
  const adapter = useDate();
  if (s === null) {
    return null;
  }
  return adapter.parseISO(s.substring(0, 10));
}

export function dateToString(date) {
  const offset = date.getTimezoneOffset();
  date = new Date(date.getTime() - offset * 60 * 1000);
  return date.toISOString().split("T")[0];
}
