
window.onload = function(){
    
    console.log("hello");

    function extract_position(longitude, latitude){
        document.getElementById("lo").value = latitude;
        document.getElementById("la").value = longitude;
        document.getElementById("formlL").submit();
        console.log(longitude,latitude);
    }

    function success(position) {
        extract_position(position.coords.latitude, position.coords.longitude);
    }

    function error() {

              //  alert('Sorry, no position available.');
        var success_url = "{% url 'index' %}"
			// Redirect to URL
			window.location.replace(success_url)
       
    }
      
    const watchID = navigator.geolocation.watchPosition(success, error);
    console.log(watchID);
}

