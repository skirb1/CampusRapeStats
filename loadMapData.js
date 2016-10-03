function loadMapData(value, map) {
    var name = "map" + value + ".geojson";

    //remove features
	map.data.forEach(function(feature) {
        map.data.remove(feature);
    });

	//load features
    map.data.loadGeoJson(name);
}