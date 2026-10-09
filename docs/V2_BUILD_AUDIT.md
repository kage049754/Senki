# Naruto Senki V2 Source Build Audit

Audit date: 2026-10-10  
Candidate: https://github.com/Zx-Akito/NarutoSenki-V2  
Target release reference: https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix

## Source structure verified

- Repository has Cocos2d-x engine and dependency directories, C++ source structure, Lua scripts, game resources, and platform projects.
- Android project path: `projects/NarutoSenki/proj.android-studio`.
- Android Gradle project has `settings.gradle`, root `build.gradle`, app module build file, wrapper scripts, and Gradle wrapper properties.
- The repository documentation describes Android build instructions and a game source tree with Classes, lua, Resources, sprites, and proj.android-studio.
- Repository metadata identifies it as a fork of `real-re/NarutoSenki-V2-old`; the parent was marked private in the metadata available during this audit.

## Android build configuration observed

- Android Gradle Plugin: `com.android.tools.build:gradle:3.3.3`.
- Gradle wrapper: `5.6.4`.
- compileSdkVersion: 31.
- buildToolsVersion: 31.0.0.
- minSdkVersion: 21.
- targetSdkVersion: 31.
- Version in app build file: 2.1.
- Native build uses ndk-build and requests legacy `NDK_TOOLCHAIN_VERSION=4.9`.
- ABI filters and native module paths are configured via Gradle properties.

## Compatibility risks to test once an authorized source copy is available

1. This is a legacy Gradle/Android Gradle Plugin combination; current hosted build images may not have the required compatible Java, Android SDK/build tools, or old NDK toolchain.
2. The requested NDK toolchain 4.9 is old and may not be available in modern Android build environments.
3. The Gradle build uses old Cocos2d-x native libraries, so current NDK/compiler compatibility and ABI output must be checked.
4. The source tree's exact relationship to the selected v2.1.6-fix release is not proven.
5. No actual build was run from this candidate in the user's central repository during this audit.

## Permission gate

The candidate repository has no root LICENSE in the inspected tree and GitHub metadata reports no declared license. Separate rights for sprites, character art, animations, sound, music, and bundled dependencies are also not established. Do not copy the source tree or package its assets into a redistributed APK until the relevant permissions are established.

## Status

- Source structure: verified by remote repository inspection.
- Android build configuration: inspected.
- Actual build result: not tested.
- Source import into `kage049754/Senki`: not done.
- Code/asset permission: unresolved.
- Unified modded APK: not built.
