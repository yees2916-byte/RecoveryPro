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

      # 2. إضافة التخزين المؤقت (Cache) لتسريع البناء
      - name: Cache Buildozer
        uses: actions/cache@v3
        with:
          path: |
            ~/.buildozer
            buildozer.spec
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}

      # 3. بناء التطبيق باستخدام Buildozer
      - name: Build with Buildozer
        uses: ArtemSerebrennkov/buildozer-action@v1
        with:
          buildozer_version: stable
          workdir: ${{ github.workspace }}

      # 4. رفع ملف APK الناتج
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-app-apk
          path: bin/*.apk
