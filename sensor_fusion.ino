//-7050.0  -5150.0
#include "HX711.h" //This library can be obtained here http://librarymanager/All#Avia_HX711
#define calibration_factor -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define calibration_factor1 -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define calibration_factor2 -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define calibration_factor3 -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define calibration_factor4 -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define calibration_factor5 -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

HX711 scale;
HX711 scale1;
HX711 scale2;
HX711 scale3;
HX711 scale4;
HX711 scale5;

float a,b,c,d,e,f,sa,sb,sc,sd,se,sf;
void setup() {
  Serial.begin(9600);
  scale.begin(3,2);//S1
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
 // scale.tare();	//Assuming there is no weight on the scale at start up, reset the scale to 0
  scale1.begin(5,4);//S2
  scale1.set_scale(calibration_factor1); //This value is obtained by using the SparkFun_HX711_Calibration sketch
 // scale1.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0 
  scale2.begin(7,6);//S3
  scale2.set_scale(calibration_factor2); //This value is obtained by using the SparkFun_HX711_Calibration sketch
//  scale2.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  scale3.begin(31,30); //S4                         //Only for yash others dont carry SWAPPED (31,30) WITH (9,8) ;
  scale3.set_scale(calibration_factor3); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  //scale3.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  scale4.begin(11,10);  //S5
  scale4.set_scale(calibration_factor4); //This value is obtained by using the SparkFun_HX711_Calibration sketch
 // scale4.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0
  scale5.begin(9,8);  //S6 //31,30
  scale5.set_scale(calibration_factor5); //This value is obtained by using the SparkFun_HX711_Calibration sketch
 // scale5.tare();  //Assuming there is no weight on the scale at start up, reset the scale to 0 
  /*Serial.println("Readings:");*/
  sa = scale.get_units();
  sd = scale3.get_units();
  sb = scale1.get_units();
  sc = scale2.get_units();
  sf = scale5.get_units();
  se = scale4.get_units();
}
//147.32,449.45,888.50,35.67,176.30,121.99  142.83,-450.37,882.32,37.63,113.69,-178.76

//145.08,-450.75,879.30,40.05,275.29,846.77
//144.98,-450.72,878.91,40.03,266.97,848.35
//144.83,-450.82,878.38,39.64,265.74,859.91


void loop() {
   float buff[0];
   a=scale.get_units();
   a=fabsf(fabsf(a)-fabsf(144.88));
//   a=fabsf(fabsf(a)-fabsf(sa));
   Serial.print(a);                //S1

   d=scale3.get_units();
   d=fabsf(fabsf(d)-fabsf(-450.37));
//   d=fabsf(fabsf(d)-fabsf(sd));
   Serial.print(",");              //S2
   Serial.print(d);

   b=scale1.get_units();
   b=fabsf(fabsf(b)-fabsf(878.81));
//   b=fabsf(fabsf(b)-fabsf(sb));
   Serial.print(",");              //S3
   Serial.print(b);

   c=scale2.get_units();
   c=fabsf(fabsf(c)-fabsf(39.03));
//   c=fabsf(fabsf(c)-fabsf(sc));
   Serial.print(",");              //S4
   Serial.print(c);

   f=scale5.get_units();
   f=fabsf(fabsf(f)-fabsf(262.50));
//   f=fabsf(fabsf(f)-fabsf(sf));
   Serial.print(",");              //S6
   Serial.print(f);

   
   e=scale4.get_units();
   e=fabsf(fabsf(e)-fabsf(867.78));
//   e=fabsf(fabsf(e)-fabsf(se));
   Serial.print(",");              //S5
   Serial.println(e);

  
   delay(990);

}
