# Bitlocker-1 [picoCTF]

## Description
Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!

__Note: The original disk image files were deleted from this repo to conserver storage space.__

## Ressources provided
- `bitlocker-1.dd`

## Tools used
- `hashcat`
- `John the Ripper [bitlocker2john script]`
- `dislocker`
- `losetup`
- `rockyou.txt`

## Steps
- Use `bitlocker2john` to create a hashlist of the given disk image:

    ```bash
    $ bitlocker2john bitlocker-1.dd > hashlist.txt
    ```

    Then we get a file that looks like this:

    ```bash
    Encrypted device bitlocker-1.dd opened, size 100MB
    Salt: 2b71884a0ef66f0b9de049a82a39d15b
    RP Nonce: 00be8a46ead6da0106000000
    RP MAC: a28f1a60db3e3fe4049a821c3aea5e4b
    RP VMK: a1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58

    UP Nonce: d04d9c58eed6da010a000000
    UP MAC: 68156e51e53f0a01c076a32ba2b2999a
    UP VMK: fffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d


    User Password hash:
    $bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
    Hash type: User Password with MAC verification (slower solution, no false positives)
    $bitlocker$1$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
    Hash type: Recovery Password fast attack
    $bitlocker$2$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
    Hash type: Recovery Password with MAC verification (slower solution, no false positives)
    $bitlocker$3$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
    ```

    However, in preparation for hashcat we need to remove everything except the actual hashes:

    ```bash
    $ grep '^\$bitlocker' hashlist.txt > bitlocker.hashes
    ```

- Use hashcat to crack the password:

    ```bash
    $ hashcat -m 22100 -a 0 -o password.txt bitlocker.hashes /usr/share/wordlists/rockyou.txt
    ```

    - `22100`: specifies that we want to crack a **bitlocker** hash.
    - `-a 0`: tells Hashcat to use attack mode 0 — the "straight" (dictionary) attack.
    - We use the hashes that we created using `bitlocker2john` as well as the common password file `rockyou.txt`.

    ```bash
    Session..........: hashcat
    Status...........: Cracked
    Hash.Mode........: 22100 (BitLocker)
    Hash.Target......: $bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$10...42d66d
    Time.Started.....: Thu Sep 25 19:09:47 2025 (56 secs)
    Time.Estimated...: Thu Sep 25 19:10:43 2025 (0 secs)
    Kernel.Feature...: Pure Kernel
    Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........:       34 H/s (15.36ms) @ Accel:128 Loops:4096 Thr:1 Vec:8
    Recovered........: 1/1 (100.00%) Digests
    Progress.........: 1920/14344385 (0.01%)
    Rejected.........: 0/1920 (0.00%)
    Restore.Point....: 1792/14344385 (0.01%)
    Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1044480-1048576
    Candidate.Engine.: Device Generator
    Candidates.#1....: clifford -> hercules
    ```
    After running hashcat we have the cracked password in the `password.txt` file:

    `$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d:jacqueline`

    So the password is `jacqueline`.

- Use `losetup`to attach the disk image to a loop device and create mount points:

    ```bash
    $ sudo losetup --partscan --find --show bitlocker-1.dd 
    /dev/loop26
    $ sudo mkdir -p /mnt/dislocker /mnt/bitlocker
    ```
- Use `dislocker` to mount and decrypt the disk image:
    ```bash
    $ sudo dislocker -r -V /dev/loop26 -u -- /mnt/dislocker
    Enter the user password: 
    ```

    With password `jacqueline`.

    `dislocker` then creates a file called `dislocker-file` that contains the decrypted disk image.

- Then we can mount the decrypted disk image:

    ```bash
    $ sudo mount -o loop,ro /mnt/dislocker/dislocker-file /mnt/bitlocker -t ntfs-3g
    ```

- Finally, we can look at the decrypted drive and read the flag:

    ```bash
    $ sudo ls /mnt/bitlocker/
    '$RECYCLE.BIN'	 flag.txt  'System Volume Information'
    $ cat /mnt/bitlocker/flag.txt 
    picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}
    ```

## Solution
**Flag**: `picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}`
