# DISKO 2 [picoCTF]

## Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!

## Ressources provided
- `disko-2.dd.gz`

## Tools used
- `dd`
- `fdisk`
- `strings`

## Steps
- Decompress the provided file.
- Create a working copy (bit-by-bit) using `dd`:
    ```bash
    $ dd if=disko-2.dd of=working_disko-2.dd bs=4M status=progress
    25+0 records in
    25+0 records out
    104857600 bytes (105 MB, 100 MiB) copied, 0,156987 s, 668 MB/s
    $ sha256sum disko-2.dd working_disko-2.dd 
    6fa5a2437ae2434374f094591afc326fadd7e4a8eb6671281f2fbafa068de086  disko-2.dd
    6fa5a2437ae2434374f094591afc326fadd7e4a8eb6671281f2fbafa068de086  working_disko-2.dd
    ```

    I confirmed the success of the copy through hashing.

- Analyze the file system using `fdisk`:
    ```bash
    $ fdisk -l working_disko-2.dd 
    Disk working_disko-2.dd: 100 MiB, 104857600 bytes, 204800 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x8ef8eaee

    Device              Boot Start    End Sectors Size Id Type
    working_disko-2.dd1       2048  53247   51200  25M 83 Linux
    working_disko-2.dd2      53248 118783   65536  32M  b W95 FAT32
    ```

    This showed that the disk image actually contained two separate partitions.

    As the description of the CTF states that "The right one is Linux!", I knew that I had to find the flag within the `working_disko-2.dd1`partition.

- Isolate the Linux partition:
    ```bash
    $ dd if=working_disko-2.dd of=part1.img bs=512 skip=2048 count=51200
    51200+0 records in
    51200+0 records out
    26214400 bytes (26 MB, 25 MiB) copied, 0,164236 s, 160 MB/s
    ```

- Search for the flag using `strings`:
    ```bash
    $ strings part1.img | grep -n "picoCTF{"
    10:picoCTF{4_P4Rt_1t_i5_a93c3ba0}
    ```

    This revealed the flag.
## Solution
**Flag**: `picoCTF{4_P4Rt_1t_i5_a93c3ba0}`
