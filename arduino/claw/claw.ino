#include <Servo.h>

// Max buffer size expected for one input command
#define SERVO_PIN 9
#define BAUD_RATE 9600
#define BUFFER_SIZE 10

// Angle Limiting
#define DEFAULT_ANGLE 90
#define MAX_ANGLE 180
#define MIN_ANGLE 0

Servo servo;

int current_angle = 0;
int max_angle = 180;
int min_angle = 0;

void setup() {
  // Servo pin
  servo.attach(SERVO_PIN);
  // Serial baud rate
  Serial.begin(BAUD_RATE);
  // During setup, the servo will be initialized to 90 by default
  servo.write(DEFAULT_ANGLE);
}

void loop() {
  // Wait until there is input received
  while (!Serial.available());

  // Create buffer to retrieve command
  char buffer[BUFFER_SIZE + 1];
  // Read bytes into buffer
  Serial.readBytesUntil('\n', buffer, BUFFER_SIZE);
  // Add null terminator to avoid buffer overflow
  buffer[BUFFER_SIZE] = '\0';

  char* command = strtok(buffer, ":");
  char* value = strtok(NULL, ":");
  
  if (strcmp(command, "AUTO") == 0) auto_angle();
  else if (strcmp(command, "SET") == 0) set_angle(value);
  else if (strcmp(command, "MAX") == 0) set_max_angle(value);
  else if (strcmp(command, "MIN") == 0) set_min_angle(value);
}

// Trigger the servo to open/close without manually setting the servo
void auto_angle() {
  if ((current_angle - min_angle) >= (max_angle - current_angle)) {
    Serial.write("Opening...\n");

    while (current_angle >= min_angle) {
      delay(5);
      servo.write(current_angle--);
    }
  } else {
    Serial.write("Closing...\n");

    while (current_angle <= max_angle) {
      delay(5);
      servo.write(current_angle++);
    }
  }
}

// Trigger the servo to move to a specific value (degree)
void set_angle(char* value) {
  int new_angle = atoi(value);

  if (current_angle != new_angle && new_angle >= MIN_ANGLE && new_angle <= MAX_ANGLE) {
    current_angle = new_angle;
    servo.write(current_angle);
    write_action_with_value("Servo set: ", value);
  }
}

// Set the max value the servo can achieve
void set_max_angle(char* value) {
  int new_angle = atoi(value);
  
  // Check bounds before proceeding
  if (max_angle != new_angle && new_angle <= MAX_ANGLE) {
    max_angle = new_angle;
    write_action_with_value("Maximum updated: ", value);
  }
}

// Set the min value the servo can achieve
void set_min_angle(char* value) {
  int new_angle = atoi(value);

  // Check bounds before proceeding
  if (min_angle != new_angle && new_angle >= MIN_ANGLE) {
    min_angle = new_angle;
    write_action_with_value("Minimum updated: ", value);
  }
}

// Send message to application through serial output
void write_action_with_value(char* action, char* value) {
    Serial.write(action);
    Serial.write(value);
    Serial.write('\n');
}
