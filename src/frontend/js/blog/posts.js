function redirectToPost(postId) {
  localStorage.setItem("visualize_post", postId);
  window.location.href = `http://127.0.0.1:5500/src/frontend/html/blog/visualize_post.html`;
}
document.addEventListener("DOMContentLoaded", () => {
  const url = "http://localhost:8000/posts/show";
  let error_card = document.querySelector("#errorCard");
  let error_message = document.querySelector("#errorMessage");

  async function get_posts() {
    let response = await fetch(url, {
      method: "GET",
    });

    const result = await response.json();
    console.log(result);

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

    const postsContainer = document.getElementById("posts-container");
    let html = "";

    let date = new Date();
    let hours = date.getHours();

    function getTimeSincePost(postDateTimeString) {
      const now = new Date();
      const postDate = new Date(postDateTimeString);

      if (postDate > now) {
        return { error: "Post date is in the future" };
      }

      const diffMs = now - postDate;
      const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
      const diffHours = Math.floor(
        (diffMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      const diffMinutes = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));

      return { diffDays, diffHours, diffMinutes };
    }

    for (let post = 0; post < result.length; post++) {
      const { diffDays, diffHours, diffMinutes } = getTimeSincePost(
        result[post].post_hour
      );
      html += `
            <div class="bg-gray-800 rounded-md px-3 py-3 shadow-md hover:shadow-lg transition-shadow mb-3">
            <div class="flex flex-col gap-2">
                <!-- Título principal -->
                <button onclick="redirectToPost(${
                  result[post].id
                })" class="font-semibold text-white text-base mb-0.5 text-left">
                ${post + 1}. ${result[post].title}
            </button>

                
                <!-- Metadados compactos -->
                <div class="flex items-center gap-2 text-gray-500 text-xs flex-wrap">
                    <span class="text-gray-500">·</span>
                    <span>3 comentários</span>
                    <span class="text-gray-500">·</span>
                    <span>${result[post].author_name}</span>
                    <span class="text-gray-500">·</span>
                    <span>Há ${diffDays} dias, ${diffHours} horas e ${diffMinutes} minutos atrás.</span>
                </div>
            </div>
        </div>
        `;
    }

    postsContainer.innerHTML = html;
  }

  get_posts();
});
