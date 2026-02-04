name: Build Android APK

on:
  push:
    branches: [ "main", "master" ]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 90

    steps:
      # 1. سحب الكود من المستودع
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. بناء التطبيق باستخدام Buildozer
      - name: Build with Buildozer
        uses: ArtemSerebrennkov/buildozer-action@v1
        with:
          buildozer_version: stable
          workdir: ${{ github.workspace }}

      # 3. رفع ملف APK الناتج
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-app-apk
          path: bin/*.apk
