function getCircle(magnitude) {
      var circle = {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: 'red',
        fillOpacity: .2,
        scale: magnitude,
        strokeColor: 'white',
        strokeWeight: .5
      };
      return circle;
    }

