document.addEventListener('DOMContentLoaded', function() {
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
