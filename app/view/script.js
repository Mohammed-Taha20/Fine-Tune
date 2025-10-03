document.getElementById("send").addEventListener("click", async () => {
  const prompt = document.getElementById("prompt").value;
  const targeted_language = "English"; // or get from a user input

  const res = await fetch("/compare/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt, targeted_language })
  });

  const data = await res.json();
  document.getElementById("base").innerText = data.base_model;
  document.getElementById("finetuned").innerText = data.finetuned_model;
});