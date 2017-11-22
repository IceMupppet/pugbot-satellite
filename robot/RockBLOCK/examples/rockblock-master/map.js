/* map.js - display map and update position as reported by web service */

var interval = 5000;

// View objects
var map, infowindow, drawingManager;
var contentString = '<span id="msg"></span><br id="msg"/><span id="lat">?</span>, <span id="lng">?</span><br/>\
<span id="speed">?</span> mph, <span id="course">?</span>&deg<br/>\
Last Updated: <span id="last">?</span>';
var currentIcon = 'images/jeep-icon.png';
var trailIcon = 'images/circle.png';

// TODO: modify for extended format parameters

var maxLength = 30

// Model
// Status: lat, long, course, speed, marker, infowindow
var report = [];
var lastTime = 0; // timestamp of most recent report
// Message:
var message = [];

function recenter() {
	var lat, lng;
	if (report.length > 0) {
		current = report[report.length-1];
		lat = current.lat;
		lng = current.lng;
	} else {
		// Default home
		lat = -104.932838;
		lng = 39.597550;
	}
	try {
		map.panTo(new google.maps.LatLng(lat, lng));
	} catch (e) {
		console.log(e);
	}
}

///////////////////////////////////////////////////////////////////////
// Inserts a new report object if id is new
function addReport(time, lat, lng, course, speed, text) {	
	mytime = Date.parse(time);
	if (mytime <= lastTime)
		return;
	// change icon
	if (report.length > 0)
		report[report.length-1].marker.setIcon(trailIcon);
	var newReport = {
		'time': mytime,
		'lat': parseFloat(lat).toFixed(6),
		'lng': parseFloat(lng).toFixed(6),
		'course': parseInt(course),
		'speed': parseInt(speed),
		'text': text
	}
	console.log(newReport);
	newReport.marker = new google.maps.Marker({
				position: new google.maps.LatLng(newReport.lat, newReport.lng),
				map: map,
				icon: currentIcon
	});
	report[report.length] = newReport;
	recenter();
	lastTime = newReport.time;
}


///////////////////////////////////////////////////////////////////////
// 
function updateInfoWindow() {
	$("span#lat").text(lat);
	$("span#lng").text(lng);
	$("span#speed").text(r.speed);
	$("span#course").text(r.course);
	$("span#msg").text(r.text);
	if (r.msg != "") {
		$("br#msg").show();
	} else {
		$("br#msg").hide();
	}
	$("span#last").text(r.time);
}

///////////////////////////////////////////////////////////////////////
// polls for most recent status
function pollForUpdate() {
	$.getJSON("status.py", function(resp) {
		s = resp[0];
		console.log(s);
		addReport(s.time, s.lat, s.lng, s.course, s.speed);
	});
}


function escapeHtml(text) {
    'use strict';
    return text.replace(/[\"&<>]/g, function (a) {
        return { '"': '&quot;', '&': '&amp;', '<': '&lt;', '>': '&gt;' }[a];
    });
}


///////////////////////////////////////////////////////////////////////
// Initializes map application
function initMap() {
	map = new google.maps.Map(document.getElementById('map'));
  map.setZoom(14);
  recenter();
	infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	$.getJSON("status.py?history="+maxLength, function(resp) {
		for (s of resp) {
			console.log(s);
            addReport(s.time, s.lat, s.lng, s.course, s.speed, s.text);
		}
		setInterval(pollForUpdate, interval);
	});

	//TODO: move messaging into separate function/file/module/etc
	$.getJSON("messages.py", function(response) {
        console.log(response);
        var msgs = '';
        for (m of response) {
            console.log(m.text);
            if (m.type == "MO") {
                msgs += "<span class='mo'><b>mobile:</b> ";
            } else {
                msgs += "<span class='mt'><b>home:</b> "
            }
            msgs += (escapeHtml(m.text) + "</span><br/>");
        }
        $("div#msgs").html(msgs);
	});
}

$(window).resize(function() {
	recenter();
});

$(function() {
	
	///////////////////////////////////////////////////////////////////////
	// Handle message submit/send
	$("form").submit(function(event) {
		msg = $("#message").val();
		console.log("Message send: " + msg);

		data = { 'message': msg };

		$.post('/rock/send.py', data, function(response) {
			r = response[0];
			console.log(r);
			if (r.status == "OK") {
				$("#message").val('');
				$("div#status").text('OK');
			} else {
				$("div#status").text(r.errno + " " + r.error);
			}
		}, 'json');
		event.preventDefault();

	});
		
});
