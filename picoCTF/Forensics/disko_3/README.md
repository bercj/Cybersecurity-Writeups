# DISKO 3 [picoCTF]

## Description
Can you find the flag in this disk image? This time, its not as plain as you think it is!

__Note: The original disk image files were deleted from this repo to conserve storage space.__

## Ressources provided
- `disko-3.dd.gz`

## Tools used
- `dd`
- `fdisk`
- `grep`
- `binwalk`

## Steps
- Decompress the provided file.
- Create a working copy (bit-by-bit) using `dd`:
    ```bash
    $ dd if=disko-3.dd of=working_disko-3.dd bs=4M status=progress
    25+0 records in
    25+0 records out
    104857600 bytes (105 MB, 100 MiB) copied, 0,0997672 s, 1,1 GB/s

    ```

    I confirmed the success of the copy through hashing.

- Analyze the file system using `fdisk`:
    ```bash
    $ fdisk -l working_disko-3.dd 
    Disk working_disko-3.dd: 100 MiB, 104857600 bytes, 204800 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x00000000

    ```

    Here we only have one single partition.

- Use `binwalk` to extract the files from the partition:
    ```bash
    $ binwalk -eM working_disko-3.dd
    ```

    This extracted all the files from the partition into a new directory `_working_disko_3.dd.extracted`.

- Search for the flag using `grep`:
    ```bash
    $ grep -r "picoCTF" _working_disko-3.dd.extracted/
    _working_disko-3.dd.extracted/flag:picoCTF{n3v3r_z1p_2_h1d3_7e0a17da}
    ```

    This revealed the flag in a file called `flag`.
## Solution
**Flag**: `picoCTF{n3v3r_z1p_2_h1d3_7e0a17da}`
