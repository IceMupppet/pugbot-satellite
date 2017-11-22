/**
 * Created by Pux0r3 on 8/18/15.
 */

window.castReceiverManager = cast.receiver.CastReceiverManager.getInstance();
console.log("Created castReceiverManager");

window.onload = function() {
	cast.receiver.logger.setLevelValue(0);
	window.castReceiverManager.start();
	console.log("castReceiverManager started!");
};

window.castReceiverManager.onSenderDisconnected = function(event) {
	console.log("castReceiverManager lost connection!");
	if (window.castReceiverManager.getSenders().length == 0
		&& event.reason == cast.receiver.system.DisconnectReason.REQUESTED_BY_SENDER) {
		window.close();
	}
};
