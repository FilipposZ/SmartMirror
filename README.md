# Smart Mirror - Eng Auth 2020

## A health focused smart mirror diploma thesis

The goal of the master's thesis is to develop a [smart mirror](https://en.wikipedia.org/wiki/Virtual_mirror) product. The hardware consists of a Raspberry Pi 4, a mirror-computer screen, speakers, microphone and a camera. The software is an os-like application, featuring voice commands and rich extendability.

### Exercisor Widget

The [Exercisor](/widgets/exercisor/) is an application widget on top of the smart mirror. It plays the role of the user's personal trainer, providing realtime feedback, corrective guidance and qualitative scoring while the user is exercising at home or at a clinic.

### Features

The exercisor allows the user to:

- save videos with reference exercises
- playback the reference exercises in a game-like environment, that displays:
  1. a human model performing the reference exercise, rendered with the [Skinned Multi-Person Linear Model (SMPL)](https://smpl.is.tue.mpg.de/)
  2. the user's body as detected by the computer vision framework [Human Mesh Recovery (HMR)](https://akanazawa.github.io/hmr/)
  3. corrective arrows, providing realtime feedback and guidance
  4. a performance score, depending on the correctness of the exercise
