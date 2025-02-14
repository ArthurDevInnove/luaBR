function showLoadingOverlay() {
  const overlay = document.getElementById("loadingOverlay");
  overlay.classList.remove("hidden");
}

function hideLoadingOverlay() {
  const overlay = document.getElementById("loadingOverlay");
  overlay.classList.add("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const url = "http://localhost:8000/auth/register";
  const submitBtn = document.getElementById("submitBtn");
  const btnText = document.getElementById("btnText");
  const loadingIcon = document.getElementById("loadingIcon");

  let error_card = document.querySelector("#errorCard");
  let error_message = document.querySelector("#errorMessage");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    let public_name = document.getElementById("public_name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    const data = {
      name: public_name,
      password: password,
      email: email,
    };

    const jsonData = JSON.stringify(data);
    const headers = new Headers();
    headers.append("Content-Type", "application/json");

    submitBtn.disabled = true;
    loadingIcon.classList.remove("hidden");
    showLoadingOverlay();
    try {
      let response = await fetch(url, {
        method: "POST",
        headers: headers,
        body: jsonData,
      });

      const result = await response.json();

      if (!response.ok) {
        console.log(result);
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
      btnText.classList.remove("hidden");
      loadingIcon.classList.add("hidden");

      window.location.href =
        "http://127.0.0.1:5500/src/frontend/html/auth/success_register.html";
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
      loadingIcon.classList.add("hidden");
    }
  });
});
