import {
  showLoadingOverlay,
  hideLoadingOverlay,
} from "/src/frontend/js/components/overlay.js";

function makePost() {
  const form = document.querySelector("form");
  const url = form.action;
  const submitBtn = document.getElementById("submitBtn");

  let error_card = document.querySelector("#errorCard");
  let error_message = document.querySelector("#errorMessage");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    let title = document.getElementById("titulo");
    let content = document.getElementById("contentBody");

    const data = {
      title: title.value,
      content: content.textContent,
    };

    const jsonData = JSON.stringify(data);
    const headers = new Headers();
    headers.append("Content-Type", "application/json");

    submitBtn.disabled = true;
    showLoadingOverlay();
    console.log(content.textContent);

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: headers,
        body: jsonData,
        credentials: "include",
      });

      const result = await response.json();

      if (!response.ok) {
        error_message.textContent = result.detail || "Erro desconhecido!";

        error_card.classList.remove("opacity-0", "translate-x-full");
        error_card.classList.add("opacity-100", "translate-x-0");

        setTimeout(() => {
          error_card.classList.remove("opacity-100", "translate-x-0");
          error_card.classList.add("opacity-0", "translate-x-full");
        }, 3000);

        return;
      }

      submitBtn.disabled = false;
      console.log(result);
      localStorage.setItem("visualize_post", result.id);
    } catch (error) {
      error_message.textContent = "Erro na conexão com o servidor";
      error_card.classList.remove("opacity-0", "translate-x-full");
      error_card.classList.add("opacity-100", "translate-x-0");

      setTimeout(() => {
        error_card.classList.remove("opacity-100", "translate-x-0");
        error_card.classList.add("opacity-0", "translate-x-full");
      }, 3000);
    } finally {
      hideLoadingOverlay();
      submitBtn.disabled = false;
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  makePost();
});
