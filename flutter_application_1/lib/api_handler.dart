import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

class ApiManager {
  final String baseUrl;

  ApiManager({required this.baseUrl});

  Future<void> sendAudio(File audioFile) async {
    final url = Uri.parse('$baseUrl/process_audio');
    final request = http.MultipartRequest('POST', url);
    request.files
        .add(await http.MultipartFile.fromPath('file', audioFile.path));

    final response = await request.send();

    if (response.statusCode == 200) {
      // Audio sent successfully
      print('Audio sent successfully');
    } else {
      throw Exception('Failed to send audio');
    }
  }

  Future<String> getReplyText() async {
    final response = await http.get(Uri.parse('$baseUrl/get_reply'));

    if (response.statusCode == 200) {
      final jsonResponse = json.decode(response.body);
      return jsonResponse['text'] as String;
    } else {
      throw Exception('Failed to get reply text');
    }
  }

  Future<File> getAudioFile() async {
    final response = await http.get(Uri.parse('$baseUrl/get_audio'));

    if (response.statusCode == 200) {
      final bytes = response.bodyBytes;
      final audioFile = File('output_audio.wav');
      await audioFile.writeAsBytes(bytes, flush: true);
      return audioFile;
    } else {
      throw Exception('Failed to get audio file');
    }
  }
}
