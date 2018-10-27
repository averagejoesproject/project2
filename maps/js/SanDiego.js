// Creating map object
var myMap = L.map("map", {
    center: [32.71, -117.16],
    zoom: 10,
  });
  
  // Adding tile layer to the map
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  }).addTo(myMap);
  
  // Build API query URL (base URL, date range, complaint type, limit)
  var url = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=381&apikey=5lftloDOe5TaHbiiqPuyxe2mFoB5ThQY";
  
  d3.json(url, function(data){
      console.log(data)
      var markers = L.markerClusterGroup();

      data["_embedded"]["events"].forEach(d => {
        console.log(d._embedded.venues[0].location)
        var location = d._embedded.venues[0].location
        if (location) {
            markers.addLayer(
                L.marker([
                    parseFloat(location.latitude),
                    parseFloat(location.longitude)
                    // parseInt(location.latitude)
                ]).bindPopup("<img style=max-height:400px;max-width:310px; src=" + d.images[1].url + "><h3>" + d.name + "</h3><hr><p><strong>Venue: </strong>" + d._embedded.venues[0].name + "<br><strong>Date: </strong>" + new Date(d.dates.start.localDate) + '<br/><br/><input type="button" onclick="window.open(' + "'" + d.url + "')" + '" value="Buy Tickets" /></p>').addTo(myMap)
            );
        }
      });

      myMap.addLayer(markers);
  });