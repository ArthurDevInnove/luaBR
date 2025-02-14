const id = localStorage.getItem('visualize_post');
const url = `http://localhost:8000/posts/get/${id}`;
let error_card = document.querySelector("#errorCard");
let error_message = document.querySelector("#errorMessage");


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
    const diffMinutes = Math.floor(
    (diffMs % (1000 * 60 * 60)) / (1000 * 60)
    );

    return { diffDays, diffHours, diffMinutes };
}

async function get_posts() {
    try {
    let response = await fetch(url, {
        method: "GET",
    });

    const result = await response.json();
    
    if (!response.ok) {
        throw new Error(result.detail || "Erro desconhecido!");
    }

    const {diffDays, diffHours, diffMinutes} = getTimeSincePost(
        result.post_hour
    )

    // Preenchendo apenas os elementos com IDs específicos
    document.querySelector("#author").textContent = result.author_name || "Autor desconhecido";
    document.querySelector("#time").textContent = `Há ${diffDays} dias, ${diffHours} horas e ${diffMinutes} minutos. ` || "Data desconhecida";
    document.querySelector("#title").textContent = result.title || "Título não disponível";
    document.querySelector("#content").textContent = result.content || "Conteúdo não disponível";
    } catch (error) {
    console.error(error);
    error_message.textContent = error.message;
    error_card.classList.remove("opacity-0", "translate-x-full");
    error_card.classList.add("opacity-100", "translate-x-0");

    setTimeout(() => {
        error_card.classList.remove("opacity-100", "translate-x-0");
        error_card.classList.add("opacity-0", "translate-x-full");
    }, 3000);
    }
}

// Chama a função ao carregar a página
document.addEventListener("DOMContentLoaded", () => {
    get_posts()

    const postMenuButton = document.getElementById('postMenuButton');
    const postMenu = document.getElementById('postMenu');

    // Alternar menu
    postMenuButton.addEventListener('click', (e) => {
    e.stopPropagation();
    postMenu.classList.toggle('hidden');
    });

    // Fechar menu ao clicar fora
    document.addEventListener('click', () => {
    postMenu.classList.add('hidden');
    });

    // Prevenir fechamento ao clicar no menu
    postMenu.addEventListener('click', (e) => {
    e.stopPropagation();
    });
});