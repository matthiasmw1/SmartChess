#include <Wire.h>

const int CHANNELS_PER_MUX = 16;
const float CHANGE_THRESHOLD = 0.6;

// Pin definitions for MUX 1
const int MUX_1_S3 = 22;
const int MUX_1_S2 = 24;
const int MUX_1_S1 = 26;
const int MUX_1_S0 = 28;
const int MUX_1_OUT = A0;

// Pin definitions for MUX 2
const int MUX_2_S3 = 30;
const int MUX_2_S2 = 32;
const int MUX_2_S1 = 34;
const int MUX_2_S0 = 36;
const int MUX_2_OUT = A1;

// Pin definitions for MUX 3
const int MUX_3_S3 = 47;
const int MUX_3_S2 = 49;
const int MUX_3_S1 = 51;
const int MUX_3_S0 = 53;
const int MUX_3_OUT = A3;

// Pin definitions for MUX 4
const int MUX_4_S3 = 38;
const int MUX_4_S2 = 40;
const int MUX_4_S1 = 42;
const int MUX_4_S0 = 44;
const int MUX_4_OUT = A2;

bool half = 0;

void setup() {
    Serial.begin(9600);

    // Set pin modes for MUX 1
    pinMode(MUX_1_S3, OUTPUT);
    pinMode(MUX_1_S2, OUTPUT);
    pinMode(MUX_1_S1, OUTPUT);
    pinMode(MUX_1_S0, OUTPUT);
    pinMode(MUX_1_OUT, INPUT);

    // Set pin modes for MUX 2
    pinMode(MUX_2_S3, OUTPUT);
    pinMode(MUX_2_S2, OUTPUT);
    pinMode(MUX_2_S1, OUTPUT);
    pinMode(MUX_2_S0, OUTPUT);
    pinMode(MUX_2_OUT, INPUT);

    // Set pin modes for MUX 3
    pinMode(MUX_3_S3, OUTPUT);
    pinMode(MUX_3_S2, OUTPUT);
    pinMode(MUX_3_S1, OUTPUT);
    pinMode(MUX_3_S0, OUTPUT);
    pinMode(MUX_3_OUT, INPUT);

    // Set pin modes for MUX 4
    pinMode(MUX_4_S3, OUTPUT);
    pinMode(MUX_4_S2, OUTPUT);
    pinMode(MUX_4_S1, OUTPUT);
    pinMode(MUX_4_S0, OUTPUT);
    pinMode(MUX_4_OUT, INPUT);

    pinMode(4, INPUT_PULLUP); // Button pin
}

void loop() {
  String move = "";
    // Define arrays to store values for all MUX channels
    int list1[4][CHANNELS_PER_MUX];
    int list2[4][CHANNELS_PER_MUX];

    // Step 1: Save the values in list1
    for (int muxNum = 1; muxNum <= 4; muxNum++) {
        for (int channel = 0; channel < CHANNELS_PER_MUX; channel++) {
            selectMuxChannel(muxNum, channel);
            list1[muxNum - 1][channel] = analogRead(getMuxOutPin(muxNum));
        }
    }

    // Wait for the button to be released
    while (digitalRead(4) == LOW) {
        // Wait for the button to be released
    }
    delay(1000);
    
    // Step 2: Save the values in list2
    for (int muxNum = 1; muxNum <= 4; muxNum++) {
        for (int channel = 0; channel < CHANNELS_PER_MUX; channel++) {
            selectMuxChannel(muxNum, channel);
            list2[muxNum - 1][channel] = analogRead(getMuxOutPin(muxNum));
        }
    }
    
    // Step 3: Compare values between list1 and list2 for all MUX channels
    for (int muxNum = 1; muxNum <= 4; muxNum++) {
        for (int channel = 0; channel < CHANNELS_PER_MUX; channel++) {
            // Calculate 20% increase and decrease
            int thresholdIncrease = list1[muxNum - 1][channel] * 1.2;
            int thresholdDecrease = list1[muxNum - 1][channel] * 0.8;

            // Check if the current value is within the thresholds
            if (list2[muxNum - 1][channel] >= thresholdDecrease && list2[muxNum - 1][channel] <= thresholdIncrease) {
                // Do nothing if the value is within the threshold
            } else {
                // Print a message if the value is outside the threshold
                char letter = getLetterForMux(muxNum);
                int rank = 1 + channel;
                if (rank > 8) {
                    rank -= 8;
                    half = 1;
                    letter = getLetterForMux(muxNum) + 1;
                }
                String message = String(letter) + String(rank);
                move += message;
                
            }
        }
    }
    if (move != NULL){Serial.println(move);}
    
    
}

void selectMuxChannel(int muxNum, int channel) {
    switch (muxNum) {
        case 1:
            digitalWrite(MUX_1_S0, bitRead(channel, 0));
            digitalWrite(MUX_1_S1, bitRead(channel, 1));
            digitalWrite(MUX_1_S2, bitRead(channel, 2));
            digitalWrite(MUX_1_S3, bitRead(channel, 3));
            break;
        case 2:
            digitalWrite(MUX_2_S0, bitRead(channel, 0));
            digitalWrite(MUX_2_S1, bitRead(channel, 1));
            digitalWrite(MUX_2_S2, bitRead(channel, 2));
            digitalWrite(MUX_2_S3, bitRead(channel, 3));
            break;
        case 3:
            digitalWrite(MUX_3_S0, bitRead(channel, 0));
            digitalWrite(MUX_3_S1, bitRead(channel, 1));
            digitalWrite(MUX_3_S2, bitRead(channel, 2));
            digitalWrite(MUX_3_S3, bitRead(channel, 3));
            break;
        case 4:
            digitalWrite(MUX_4_S0, bitRead(channel, 0));
            digitalWrite(MUX_4_S1, bitRead(channel, 1));
            digitalWrite(MUX_4_S2, bitRead(channel, 2));
            digitalWrite(MUX_4_S3, bitRead(channel, 3));
            break;
    }
}

int getMuxOutPin(int muxNum) {
    switch (muxNum) {
        case 1: return MUX_1_OUT;
        case 2: return MUX_2_OUT;
        case 3: return MUX_3_OUT;
        case 4: return MUX_4_OUT;
        default: return -1; // Invalid muxNum
    }
}

char getLetterForMux(int muxNum) {
    switch (muxNum) {
        case 1: return 'g';
        case 2: return 'e';
        case 3: return 'c';
        case 4: return 'a';
        default: return ' '; // Invalid muxNum
    }
}
