class Sphero
  class Response
    SOP1 = 0
    SOP2 = 1
    MRSP = 2
    SEQ  = 3
    DLEN = 4

    CODE_OK = 0
    SIMPLE_RESPONSE = 0xFF
    ASYNC_RESPONSE = 0xFE

    def self.simple?(header)
      header[SOP2] == SIMPLE_RESPONSE
    end

    def self.async?(header)
      header[SOP2] == ASYNC_RESPONSE
    end

    def initialize header, body
      @header = header
      @body   = body
    end

    def valid?
      @header && @body  
    end

    def empty?
      valid? && @header[DLEN] == 1
    end

    def success?
      valid? && @header[MRSP] == CODE_OK
    end

    def seq
      valid? && @header[SEQ]
    end

    def body
      @body.unpack 'C*'
    end

    class GetAutoReconnect < Response
      def time
        body[1]
      end
    end

    class GetPowerState < Response
      # constants for power_state
      CHARGING = 0x01
      OK       = 0x02
      LOW      = 0x03
      CRITICAL = 0x04

      def body
        @body.unpack 'CCnnnC'
      end

      def rec_ver
        body[0]
      end

      def power_state
        body[1]
      end

      # Voltage * 100
      def batt_voltage
        body[2]
      end

      def num_charges
        body[3]
      end

      # Time since awakened in seconds
      def time_since_charge
        body[4]
      end
    end

    class GetBluetoothInfo < Response
      def name
        body.take(16).slice_before(0x00).first.pack 'C*'
      end

      def bta
        body.drop(16).slice_before(0x00).first.pack 'C*'
      end
    end

    class GetRGB < Response
      def r; body[0]; end
      def g; body[1]; end
      def b; body[2]; end
    end

    class AsyncResponse < Response
      ID_CODE = 2
      DLEN_MSB = 3
      DLEN_LSB = 4

      POWER_NOTIFICATION = 0x01
      LEVEL_1_DIAGNOSTIC = 0x02
      SENSOR_DATA = 0x03
      CONFIG_BLOCK = 0x04
      PRESLEEP_WARNING = 0x05
      MACRO_MARKERS = 0x06
      COLLISION_DETECTED = 0x07

      VALID_REPONSES = {POWER_NOTIFICATION => 'Sphero::Response::PowerNotification',
                        #LEVEL_1_DIAGNOSTIC => 'AsyncResponse',
                        SENSOR_DATA => 'Sphero::Response::SensorData',
                        #CONFIG_BLOCK => 'AsyncResponse',
                        #PRESLEEP_WARNING => 'AsyncResponse',
                        #MACRO_MARKERS => 'AsyncResponse',
                        COLLISION_DETECTED => 'Sphero::Response::CollisionDetected'}

      def self.valid?(header)
        VALID_REPONSES.keys.include?(header[ID_CODE])
      end

      def self.response header, body
        raise "no good" unless self.valid?(header)
        constantize(VALID_REPONSES[header[ID_CODE]]).new(header, body)
      end

      def self.constantize(camel_cased_word)
        names = camel_cased_word.split('::')
        names.shift if names.empty? || names.first.empty?

        constant = Object
        names.each do |name|
          constant = constant.const_defined?(name) ? constant.const_get(name) : constant.const_missing(name)
        end
        constant
      end

      def empty?
        @header[DLEN_LSB] == 1
      end

      def success?
        AsyncResponse.valid?(@header)
      end

      def seq
        1
      end
    end

    class PowerNotification < GetPowerState
    end

    class SensorData < AsyncResponse
      def body
        @body.unpack 's*'
      end
    end

    class CollisionDetected < AsyncResponse
      def body
        @body.unpack 'nnnCnnCN'
      end

      def x
        body[0]
      end

      def y
        body[1]
      end

      def z
        body[2]
      end

      def axis
        body[3]
      end

      def x_magnitude
        body[4]
      end

      def y_magnitude
        body[5]
      end

      def speed
        body[6]
      end

      def timestamp
        body[7]
      end
    end
  end
end
