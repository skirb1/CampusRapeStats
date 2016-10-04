function getCircleCapita(magnitude, sz) {
    var percapita = (magnitude / sz) * 10000;
      var circle = {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: 'red',
        fillOpacity: .2,
        scale: sz,
        strokeColor: 'white',
        strokeWeight: .5
      };
      return circle;
    }