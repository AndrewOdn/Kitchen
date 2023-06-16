document.getElementById('data-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Предотвращаем отправку формы

    // Получаем значения из формы
    var temperature = document.getElementById('username').value;
    var humidity = document.getElementById('password').value;

    // Отправляем данные на сервер
    fetch('/process_register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            temperature: temperature,
            humidity: humidity
        })
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(data) {
        document.getElementById('result').innerHTML = data;
    })
    .catch(function(error) {
        console.error('Произошла ошибка:', error);
    });
});
