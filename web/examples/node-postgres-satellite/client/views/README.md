# Some JSON examples to Remember

````
            // *************************************
            // JSON EXAMPLES

            // TURN TO STRING OF JSON
            //var jsonstring = JSON.stringify(data);

            // SET the DIV
            //document.getElementById("coords").innerHTML = "<p>json string: " + jsonstring + "</p>";

            // APPEND the DIV
            //$("#coords").append('<p>json string: ' + jsonstring + '</p>');

            // TURN TO JSON OBJECT
            //var jsonobject = JSON.parse(jsonstring);
            //$("#coords").append('<p>json object: ' + jsonobject[0].latitude + '</p>');
            // *************************************
````





### Getting City/Country info for Maps

````
         // UPDATE CITY/COUNTRY INFO
          var url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="
             +newLat+","+newLng+"&sensor=false";
          $.get(url).success(function(data) {
             var loc1 = data.results[0];
             var county, city;
               $.each(loc1, function(k1,v1) {
                  if (k1 == "address_components") {
                     for (var i = 0; i < v1.length; i++) {
                        for (k2 in v1[i]) {
                           if (k2 == "types") {
                              var types = v1[i][k2];
                              if (types[0] =="sublocality_level_1") {
                                  county = v1[i].long_name;
                                  //alert ("county: " + county);
                              } 
                              if (types[0] =="locality") {
                                 city = v1[i].long_name;
                                 //alert ("city: " + city);
                             } 
                           }
                        }          
                     }
                  }
               });
               $('#current').append("<b>Showing: [" + newLat + "," + newLng + "]</b> (" + city + ") "); 
             }); 

             ````