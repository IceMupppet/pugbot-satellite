require "Sphero"

Sphero.start '/dev/rfcomm0' do
    roll 60, Sphero::FORWARD
    keep_going 3

    roll 60, RIGHT
    keep_going 3

    roll 60, BACKWARD
    keep_going 3

    roll 60, LEFT
    keep_going 3

    stop
end
