document.getElementById('recommendationForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let category = document.getElementById('category').value;
    let recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = '';

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'News Category': category })
    })
    .then(response => response.json())
    .then(data => {
        if (Array.isArray(data) && data.length > 0) {
            data.forEach(item => {
                let card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <div class="card-content">
                        <h2>${item}</h2>
                    </div>
                `;
                recommendationsDiv.appendChild(card);
            });
        } else {
            recommendationsDiv.innerHTML = '<p>No recommendations found for this category.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        recommendationsDiv.innerHTML = '<p>An error occurred while fetching recommendations.</p>';
    });
});
