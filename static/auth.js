$(".info-item .btn").click(function(){
  $(".container").toggleClass("log-in");
});
$(".container-form .btn").click(function(){
  $(".container").addClass("active");
});
//
//const login = document.querySelector('input[name="Username"]');
//const password = document.querySelector('input[name="Password"]');
function myFunction() {
  let text = document.getElementById("myInput").value;
  window.location = '/'
}
function delay(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}
function GoToHomePage()
  {
    delay(1000).then(() => window.location = '/');
  }
var button = document.getElementById(".btn");
button.addEventListener("click", function() {
  document.getElementById("main").innerHTML = data;
});

login.addEventListener("change", (e) => {
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
});
document.getElementById('input').addEventListener('submit', function(e) {
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
