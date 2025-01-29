async function fetchData() {
    const idk = document.getElementById('idk');

    const url = 'http://localhost:8000/home';
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Some error occurred.');
        }

        const json = await response.json();
        console.log(json);
        idk.textContent = json.title;
    } catch (error) {
        console.error('Error:', error);
    }
}

fetchData();
