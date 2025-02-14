import { getCookie } from "../utils/get_cookie.js";

function createAuthButtons() {
  const div_buttons = document.getElementById("div-buttons");
  let html = `
  <button
    class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-full transition-colors font-medium">
        Cadastrar
    </button>
    <button
        class="bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded-full transition-colors font-medium">
          Registrar
    </button>
  `;

  div_buttons.innerHTML += html;
}

function createAccountButtons() {
  const div_buttons = document.getElementById("div-buttons");
  let html = `
    <button class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-full transition-colors font-medium">
        <i class="bx bx-plus text-xl"></i>
    </button>
    <button class="bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded-full transition-colors font-medium">
        <i class="bx bx-menu text-xl"></i>
    </button>
    `;

  div_buttons.innerHTML += html;
}

function onLoadDocument() {
  const jwt_cookie = getCookie("token_jwt");
  console.log(jwt_cookie);

  if (jwt_cookie) {
    createAccountButtons();
  } else {
    createAuthButtons();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  onLoadDocument();
});
