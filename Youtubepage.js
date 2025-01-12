document.querySelector('header input').addEventListener('input', function() {
    const searchQuery = this.value.toLowerCase();
    const videos = document.querySelectorAll('.video');
    videos.forEach(video => {
        const title = video.querySelector('p').textContent.toLowerCase();
        if (title.includes(searchQuery)) {
            video.style.display = 'block';
        } else {
            video.style.display = 'none';
        }
    });
});
