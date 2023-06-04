function initMap() {
    // Tạo bản đồ
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 21.012429, lng: 105.870103}, // Tọa độ trung tâm
        zoom: 15 // Mức độ zoom
    });

    // Tạo đường đi
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    // Xử lý sự kiện form submit
    document.getElementById('directions-form').addEventListener('submit', function(event) {
        event.preventDefault();
        calculateDirections(directionsService, directionsRenderer);
    });

    // Tính toán và hiển thị đường đi
    function calculateDirections(directionsService, directionsRenderer) {
        var origin = document.getElementById('origin').value;
        var destination = document.getElementById('destination').value;

        directionsService.route(
            {
                origin: origin,
                destination: destination,
                travelMode: 'DRIVING'
            },
            function(response, status) {
                if (status === 'OK') {
                    directionsRenderer.setDirections(response);
                } else {
                    window.alert('Không tìm thấy đường đi.');
                }
            }
        );
    }
}
