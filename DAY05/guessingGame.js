document.addEventListener('DOMContentLoaded', function () {
    let randomnumber = Math.floor(Math.random() * 100);
    let rand_int = randomnumber.toString();
    document.querySelector('h2').innerHTML = rand_int;

    document.querySelector('form').onsubmit = function me() {
        const guess = document.querySelector('#useinput').value;

        if (rand_int === guess) {
            document.querySelector('h1').innerHTML = "Congratulations! ";
        }
        else {
            document.querySelector('h1').innerHTML = "Sorry! guess again!";


        }
        return false;

    }


});