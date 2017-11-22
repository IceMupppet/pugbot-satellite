# After you have setup your ip address and started the stream
you can quickly test to make sure it is working over RTP using VLC media player

     vlc --network-caching=100 bbb.sdp

where bbb.sdp is the file supplied and needs to be on the machine receiving the stream.
