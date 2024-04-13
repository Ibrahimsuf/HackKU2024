mapboxgl.accessToken = 'pk.eyJ1IjoiaWJyYWhpbXN1ZmkiLCJhIjoiY2x1eWZycGFvMTEzcTJtb3Q5dmk3YTJqOSJ9.6YMmCuxu-vPt0-LHZqyLrw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [0, 0],
    zoom: 2
});

var marker = new mapboxgl.Marker();

function findLocation() {
    console.log('Finding location...');
    var address = document.getElementById('location').value;

    fetch('https://api.mapbox.com/geocoding/v5/mapbox.places/' + encodeURIComponent(address) + '.json?access_token=' + mapboxgl.accessToken)
        .then(response => response.json())
        .then(data => {
            if (data.features.length > 0) {
                var coordinates = data.features[0].geometry.coordinates;
                var longitude = coordinates[0];
                var latitude = coordinates[1];

                map.setCenter([longitude, latitude]);
                marker.setLngLat([longitude, latitude]).addTo(map);

                document.getElementById('Longitude').value = longitude;
                document.getElementById('Latitude').value = latitude;
            } else {
                alert('Location not found!');
            }
        })
        .catch(error => console.error('Error:', error));
}