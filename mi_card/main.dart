import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color.fromARGB(255, 11, 153, 209),
        body: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              // making a circle avatar and adding an image
              CircleAvatar(
                radius: 50.0,
                backgroundImage: AssetImage('images/Dark_Connection.jpg'),
              ),
              Text(
                'Dark Connection',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  fontSize: 30.0,
                  color: Color.fromARGB(255, 30, 5, 91),
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                'BEAST IN BLACK',
                style: TextStyle(
                  fontFamily: 'Protest Revolution',
                  fontSize: 15.0,
                  letterSpacing: 2.5,
                  color: Color.fromARGB(255, 30, 5, 91),
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(
                height: 20.0,
                width: 150.0,
                child: Divider(
                  color: Colors.cyan.shade100,
                ),
              ),
              Card(
                color: Color.fromRGBO(207, 220, 231, 1),
                margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 20.0),
                child: ListTile(
                  leading: Icon(
                    Icons.phone,
                    color: Color.fromARGB(255, 30, 5, 91),
                  ),
                  title: Text(
                    '076 307 6242',
                    style: TextStyle(
                      color: Color.fromARGB(255, 30, 5, 91),
                      fontFamily: 'Pacifico',
                      fontSize: 20.0,
                    ),
                  ),
                ),
              ),
              Card(
                color: Color.fromRGBO(207, 220, 231, 1),
                margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 20.0),
                child: ListTile(
                  leading: Icon(
                    Icons.map,
                    color: Color.fromARGB(255, 30, 5, 91),
                  ),
                  title: Text(
                    'Finland',
                    style: TextStyle(
                      color: Color.fromARGB(255, 30, 5, 91),
                      fontFamily: 'Pacifico',
                      fontSize: 20.0,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
