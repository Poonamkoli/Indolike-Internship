document.getElementById('searchBtn').addEventListener('click', getWeather);

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    const apiKey = 'YOUR_API_KEY';  // Replace with your OpenWeatherMap API key
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.cod === '404') {
            throw new Error('City not found');
        }

        // Display weather data
        document.getElementById('cityName').textContent = `City: ${data.name}`;
        document.getElementById('temperature').textContent = `Temperature: ${data.main.temp}°C`;
        document.getElementById('condition').textContent = `Condition: ${data.weather[0].description}`;
        document.getElementById('humidity').textContent = `Humidity: ${data.main.humidity}%`;
        document.getElementById('error').textContent = '';  // Clear any previous errors

    } catch (error) {
        document.getElementById('error').textContent = error.message;
        document.getElementById('weatherInfo').innerHTML = '';  // Clear previous weather data
    }
}
