#include <ArduinoJson.h> 
#include <LiquidCrystal.h> 
LiquidCrystal lcd(13, 3, 4, 5, 6, 7); //rs, enable, d4, d5, d6, d7

//NOTE:
//  Converting back to JSON probably was not the easiest way to do this
//   BUT on the bright side it could be good if I expand features

//Display info to LCD
void displ(const String* names, const int* nums, const size_t len) {
  lcd.setCursor(0, 0);
  lcd.print("Course Item");
  lcd.setCursor(0, 1);
  lcd.print("Amounts: ");
  delay(2000);
  lcd.clear();
  for(size_t i = 0; i < len; i += 2) {
    lcd.setCursor(0, 0);
    lcd.print(names[i] + ": " + nums[i]);
    if(i + 1 < len) {
      lcd.setCursor(0, 1);
      lcd.print(names[i+1] + ": " + nums[i+1]);
    }
    delay(2000);
    lcd.clear(); 
  }
}

//Parse course names and amt of assignments into seperate arrays
void handleJSON(JsonObject obj) {

  size_t datsize = obj.size();

  String names[datsize];
  int nums[datsize];

  size_t i = 0;
  for(JsonPair p : obj) {
    names[i] = p.key().c_str();
    nums[i] = p.value().as<int>();
    i++;
  }

  displ(names, nums, datsize);
}

void setup() { 
  
  Serial.begin(9600);
  while(!Serial);
  lcd.begin(16,2);

}

bool hasValid = false;
StaticJsonDocument<200> doc;
void loop() {

  //parse string from serial and once end is reached, convert back to json
  static String input = "";
  while(Serial.available()) {
    
    char c = Serial.read();
    if(c == '\n') {

      //Serial.println();
      //Serial.println(input);

      DeserializationError e = deserializeJson(doc, input);
      if(!e) {
        handleJSON(doc.as<JsonObject>());
        hasValid = true;
      }

      input = "";
    }
    else input += c;

  }

  if(hasValid) {    //keep running when not collecting data
    handleJSON(doc.as<JsonObject>());
  }

  delay(3000);
}