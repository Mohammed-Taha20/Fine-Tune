document.getElementById("send").addEventListener("click", async () => {
  const prompt = document.getElementById("prompt").value;
  
  const res = await fetch("/compare/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });

  const data = await res.json();
  document.getElementById("base").innerText = data.base_output;
  document.getElementById("finetuned").innerText = data.finetuned_output;
});
