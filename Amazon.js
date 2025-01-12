// Example search functionality (not connected to an API)
document.querySelector('.search-bar button').addEventListener('click', function() {
    const searchQuery = document.querySelector('.search-bar input').value;
    if (searchQuery) {
        alert(`Searching for: ${searchQuery}`);
    }
});
