import 'package:audio_waveforms/audio_waveforms.dart';
import 'package:flutter/material.dart';
import 'AudioManager.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  //! Booleans
  bool isRecording = false;
  bool isPlaying = false;
  bool isLoading = false;
  bool isRecordingCompleted = false;

  //! Response and Files
  String? path;
  String? musicFile;
  String response = "Assistant Response Here";

  //! Controllers
  RecorderController controller = RecorderController();

  //! Audio Manager
  AudioManager audioManager = AudioManager();

  Widget audioWaveform() {
    return AudioWaveforms(
      enableGesture: true,
      size: Size(MediaQuery.of(context).size.width, 80),
      recorderController: controller,
      waveStyle: const WaveStyle(
        waveColor: Colors.white,
        extendWaveform: true,
        showMiddleLine: false,
      ),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(12.0),
        color: Colors.teal.withOpacity(0.5),
      ),
      padding: const EdgeInsets.all(5),
      // margin: const EdgeInsets.symmetric(horizontal: 15),
    );
  }

  void _refreshWave() {
    if (isRecording) controller.refresh();
  }

  void toggleRecording() async {
    if (isRecording) {
      //!Controllers only
      controller.reset();
      controller.stop(false);

      //Everything else
      response = "Stopped Recording, Sending Data to AI";
      final filePath = await audioManager.stopRecording();
      if (filePath != null) {
        print(filePath);
        setState(() {
          path = filePath;
        });
      }
    } else {
      //! Controllers only
      controller.record();

      //Everything else
      response = "Is Recording";
      audioManager.startRecording();
    }
    setState(() {
      isRecording = !isRecording;
      print("ISRECORDING changed to: $isRecording");
    });
  }

  void togglePlayback() async {
    if (isPlaying) {
      response = "Stopped Playing";
      // await audioManager.stopPlaying();
    } else {
      response = "Is Playing";
      // await audioManager.startPlaying(path!);
    }
    setState(() {
      isPlaying = !isPlaying;
      isRecording = !isRecording;
      print("ISPLAYING changed to: $isPlaying");
    });
  }

  Widget buildButton() {
    return GestureDetector(
      onTap: () {
        // if (isRecording || isPlaying) {
        //   if (path != null) {
        //     togglePlayback();
        //   }
        // } else {
        //   toggleRecording();
        // }
        toggleRecording();
      },
      child: Container(
        padding: EdgeInsets.all(20),
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: Colors.white,
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.5),
              spreadRadius: 4,
              blurRadius: 7,
              offset: Offset(0, 3),
            ),
          ],
        ),
        child: AnimatedSwitcher(
          duration: Duration(milliseconds: 300),
          transitionBuilder: (Widget child, Animation<double> animation) {
            return ScaleTransition(
              scale: animation,
              child: child,
            );
          },
          child: Icon(
            isRecording
                ? Icons.stop
                //     : isPlaying
                //         ? Icons.pause
                //         : path != null
                //             ? Icons.play_arrow
                : Icons.mic,
            // if(isRecording){
            //   Icons.stop;
            // }else{
            //   if(isPlaying){
            //     Icons.pause;
            //   }else{
            //     if(path!=null){
            //       Icons.play_arrow;
            //     }else{
            //       Icons.mic;
            //     }
            //   }
            // }
            size: 40,
            color: Colors.teal.withOpacity(0.8),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    audioManager.dispose();
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'VOICE ASSISTANT',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.teal.withOpacity(0.5),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Expanded(
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  buildButton(),
                  SizedBox(height: 50),
                  Text(
                    response,
                    style: TextStyle(
                      fontSize: 18,
                      color: Colors.black,
                    ),
                  ),
                ],
              ),
            ),
          ),
          isRecording || isPlaying
              ? _buildLoadingTray()
              : SizedBox(height: 100),
        ],
      ),
    );
  }

  Widget _buildLoadingTray() {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        height: 100.0,
        width: double.infinity,
        child: Center(
          child: audioWaveform(),
        ),
      ),
    );
  }
}
