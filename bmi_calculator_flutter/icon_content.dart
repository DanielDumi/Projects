import 'package:bmi_calculator/constants.dart';
import 'package:flutter/material.dart';

class IconContent extends StatelessWidget {
  IconContent({this.icon, this.label});

  final IconData? icon;
  final String? label;

  @override
  Widget build(BuildContext context) {
    return Column(
      // center the icon and text
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Icon(icon, size: 80),
        // add some space between the icon and the text using a SizedBox
        const SizedBox(
          height: 20,
        ),
        Text(
          // at text use '!' do declare the null type
          label!,
          style: labelTextStyle,
        )
      ],
    );
  }
}
