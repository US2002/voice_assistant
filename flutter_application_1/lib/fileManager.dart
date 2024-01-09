import 'dart:io';
import 'package:path_provider/path_provider.dart';

class FileManager {
  String folderName = "/storage/emulated/0/SoundRecorder";
  Future<String> getFolderPath(String folderName) async {
    final directory = await getExternalStorageDirectory();
    final folderPath = '${directory!.path}/$folderName';
    Directory(folderPath).createSync(recursive: true);
    return folderPath;
  }

  Future<File> saveFile(String filePath) async {
    final folderPath = await getFolderPath(folderName);
    final file =
        File('$folderPath/audio_${DateTime.now().millisecondsSinceEpoch}.aac');
    final originalFile = File(filePath);
    return originalFile.copy(file.path);
  }
}
