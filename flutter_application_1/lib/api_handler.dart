import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiHandler {
  final String baseUrl;

  ApiHandler({required this.baseUrl});

  Future<dynamic> sendPostRequest(Map<String, dynamic> data) async {
    final response = await http.post(
      Uri.parse(baseUrl),
      body: json.encode(data),
      headers: {
        'Content-Type': 'application/json',
      },
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to send request');
    }
  }

  Future<dynamic> sendGetRequest() async {
    final response = await http.get(Uri.parse(baseUrl));

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to fetch data');
    }
  }
}
