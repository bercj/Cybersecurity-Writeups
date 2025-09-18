# CanYouSee [picoCTF]

## Description
In this task we get a `.jpg` file that supposedly contains a flag. The task was to recover the flag contained by the image.

## Approach

1. First, I opened the image using the standard image viewer of Ubuntu. The picture did not reveal anything special.

2. I suspected that the binary data of the image might contain the flag. I inspected the image using **ghex**. It turned out that the file header did not looked suspicious nor was there any appended data.

3. The next step was to analyze the metadata. For that I used **exiftool**. This revealed an unusual string in the **Attribution URL** field.

## Steps
- Open image:
```bash
unzip unknown.zip 

xdg-open ukn_reality.jpg

```
- Opening the image binary data in **ghex** did not reveal anything special

- Inspecting the metadata:
```bash
exiftool ukn_reality.jpg
```
resulted in
```bash
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:03:12 01:05:55+01:00
File Access Date/Time           : 2025:09:18 16:51:02+02:00
File Inode Change Date/Time     : 2025:09:18 16:50:29+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

This revealed that the **Attribution URL** was not in the expected format. Normally, this tag is used to store the URL of the creator, license page, or source of the image. In this case, the value did not contain any protocol (e.g., https://) and also appeared to be encoded in Base64.

- Decode the value:
```bash
echo 'cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==' | base64 -d
```

which reveals the flag: `picoCTF{ME74D47A_HIDD3N_6a9f5ac4}`
## Solution
**Flag**: `picoCTF{p33k_@_b00_b5ce2572}`
