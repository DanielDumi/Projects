import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  return runApp(
    MaterialApp(
      home: Scaffold(
        backgroundColor: const Color.fromARGB(255, 29, 101, 111),
        appBar: AppBar(
          title: Center(
            child: Text(
              'Magic ball',
            ),
          ),
          backgroundColor: Color.fromARGB(255, 47, 187, 195),
        ),
        body: BallPage(),
      ),
    ),
  );
}

class BallPage extends StatefulWidget {
  @override
  _BallPageState createState() => _BallPageState();
}

class _BallPageState extends State<BallPage> {
  int fortuneNumber = 1;

  void getFortune() {
    fortuneNumber = Random().nextInt(5) + 1;
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Row(
        children: <Widget>[
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: GestureDetector(
                onTap: () {
                  setState(() {
                    getFortune();
                  });
                },
                child: Image.asset('images/ball$fortuneNumber.png'),
              ),
            ),
          )
        ],
      ),
    );
  }
}
