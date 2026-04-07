<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
content="width=device-width, initial-scale=1.0">
<title>python weather app</title>
<link rel="stylesheet"
href="{{ url_for('static' , filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>weather app</h1>   

        <form method="POST">
            <input type="text"name="city" placeholder="Enter city name..." required>
            <button
type="submit">search</button>
        </form>
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif% }
        {% if weather %}
        <div class="weather-info"></div>
        <h2>{{weather.city }}</h2>
        <img class="icon"
        src="http://openweathermap.org/img/wn/{{ weather.icon }}@2x.png" alt="weather icon">
    <p class="temp">{{ weather.temperature }}celsius</p>  
    <p class="desc">{{ weather.description }}</p>
    <div class="details"> <p> humidity:<strong>{{ weather.humandity }} %</strong></p>
    <p> wind:<strong>{{ weather.wind_speed }} m/s</strong></p>    
    </div>
    </div>
    {% endif %}
</div>
</body>
</html>    