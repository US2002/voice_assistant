import 'package:flutter_application_1/fileManager.dart';
import 'package:flutter_sound/flutter_sound.dart';
// import 'package:permission_handler/permission_handler.dart';

class AudioManager {
  FlutterSoundRecorder recorder = FlutterSoundRecorder();
  FlutterSoundPlayer player = FlutterSoundPlayer();

  FileManager fileManager = FileManager();

  AudioManager() {
    recorder.openRecorder();
    recorder.setSubscriptionDuration(const Duration(milliseconds: 500));
  }

  // Future<bool> initRecorder() async {
  //   final status = await Permission.microphone.request();
  //   if (status != PermissionStatus.granted) {
  //     throw 'Permission not granted';
  //   }
  //   recorder.openRecorder();
  //   recorder.setSubscriptionDuration(const Duration(milliseconds: 500));
  //   return true;
  // }

  Future<void> startRecording() async {
    await recorder.startRecorder(toFile: "audio");
    print("RECORDING STARTED!!!!!!!!!!!");
  }

  Future<String?> stopRecording() async {
    final filePath = await recorder.stopRecorder();
    //! TO SAVE FILE LOCALLY
    // await fileManager.saveFile(filePath!);
    print("RECORDING STOPPED and SAVED!!!!!!!!!!!");
    return filePath;
  }

  Future<void> startPlaying(String filePath) async {
    await player.startPlayer(fromURI: filePath);
  }

  Future<void> stopPlaying() async {
    await player.stopPlayer();
  }

  void dispose() {
    recorder.closeRecorder();
    player.closePlayer();
  }
}
