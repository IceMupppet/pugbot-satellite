var applicationID = 'E4F91038';
var session = null;

window['__onGCastApiAvailable'] = function(loaded, errorInfo) {
	if (loaded) {
		initializeCastApi();
	}
	else {
		console.log(errorInfo);
	}
};

function initializeCastApi() {
	var sessionRequest = new chrome.cast.SessionRequest(applicationID);
	var apiConfig = new chrome.cast.ApiConfig(sessionRequest, sessionListener, receiverListener);
	chrome.cast.initialize(apiConfig, onInitSuccess, onError);
}

function receiverListener(e) {
	if (e === chrome.cast.ReceiverAvailability.AVAILABLE) {
		console.log('Receiver Found!');
	}
}

function sessionListener(e) {
	session = e;
}

function stopApp() {
	session.stop(onSuccess, onError);
}

function onInitSuccess() {
	console.log('onInitSuccess');
}

function onError(message) {
	console.log('onError: ' + message);
}

function onSuccess(message) {
	console.log('onSuccess: ' + message);
}
