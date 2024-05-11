document.addEventListener('DOMContentLoaded', function () {
    var checkIn = document.getElementById('check_in');
    var checkOut = document.getElementById('check_out');

    checkIn.addEventListener('change', function() {
        var minCheckOutDate = new Date(checkIn.value);
        checkOut.min = minCheckOutDate.toISOString().split('T')[0];
        if (checkOut.value < checkIn.value) {
            checkOut.value = checkIn.value;
        }
    });
});


window.onload = function() {
    var today = new Date().toISOString().split('T')[0];
    document.getElementById('check_in').setAttribute('min', today);
    document.getElementById('check_out').setAttribute('min', today);
}