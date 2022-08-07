window.onload = function(){
    function extract_position(latitude, longitude){
        document.getElementById("la").value = latitude;
        document.getElementById("lo").value = longitude;
        document.getElementById("formid").submit();
    }

    function success(position) {
        extract_position(position.coords.latitude, position.coords.longitude);
    }

    function error() {
    }
      
    const watchID = navigator.geolocation.watchPosition(success, error);
}