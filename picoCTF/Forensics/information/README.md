# Information [picoCTF]

## Description
In this task we get a `.jpg` file that supposedly contains a flag. The task was to recover the flag contained by the image.

## Approach

1. First, I opened the image using the standard image viewer of Ubuntu. The picture did not reveal anything special.

2. I suspected that the meta data of the image might have been changed. I used **exiftool** to reveal the metadata.

## Steps
- Open image:
```bash
xdg-open cat.jpg

```
- Opening the image binary data in **ghex** did not reveal anything special

- Inspecting the metadata:
```bash
exiftool cat.jpg
```
resulted in
```bash
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2025:09:18 19:40:27+02:00
File Access Date/Time           : 2025:09:18 19:40:41+02:00
File Inode Change Date/Time     : 2025:09:18 19:40:32+02:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1

```

This revealed that the **Licens** was not in the expected format. Normally, this tag is used to store licensing information. In this case, the value was Base64 encoded.

- Decode the value:
```bash
echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
```

which reveals the flag: `picoCTF{the_m3tadata_1s_modified}`
## Solution
**Flag**: `picoCTF{the_m3tadata_1s_modified}`
