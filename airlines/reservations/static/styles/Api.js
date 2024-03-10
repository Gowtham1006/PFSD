// Flight search form submission
document.getElementById('flight-search-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Get form values
    const origin = document.getElementById('origin').value;
    const destination = document.getElementById('destination').value;
    const departure = document.getElementById('departure').value;
    const returnDate = document.getElementById('return').value;

    // Display flight results
    const flightResults = document.getElementById('flight-results');
    flightResults.innerHTML = `
      <p>Origin: ${origin}</p>
      <p>Destination: ${destination}</p>
      <p>Departure Date: ${departure}</p>
      <p>Return Date: ${returnDate}</p>
    `;
});

// Booking form submission
document.getElementById('booking-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Get form values
    const flight = document.getElementById('flight').value;
    const seats = document.getElementById('seats').value;
    const passenger = document.getElementById('passenger').value;

    // Display booking confirmation
    const bookingConfirmation = document.getElementById('booking-confirmation');
    bookingConfirmation.innerHTML = `
      <p>Flight: ${flight}</p>
      <p>Seats: ${seats}</p>
      <p>Passenger: ${passenger}</p>
    `;
});

// Manage booking form submission