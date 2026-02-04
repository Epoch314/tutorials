# WSL Setup

## 1. Verify WSL version

First you need to verify your current WSL version. So open
a Windows PowerShell window and use the following command:

```
wsl --version
```

Sample output:

```
WSL version: 2.6.3.0
Kernel version: 6.6.87.2-1
WSLg version: 1.0.71
MSRDC version: 1.2.6353
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.26100.1-240331-1435.ge-release
Windows version: 10.0.26200.7623
```

If the output says `WSL version: 2.x.y.z` then you are good to go.

But if your version is 1, you can use:

```
wsl --set-default-version 2
```

Sample output:

```
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
The operation completed successfully.
```

## 2. List Online WSL Distros

To list the available online distros you can use:

```
wsl --list --online
```

Sample output:

```
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Ubuntu-24.04                    Ubuntu 24.04 LTS
openSUSE-Tumbleweed             openSUSE Tumbleweed
openSUSE-Leap-16.0              openSUSE Leap 16.0
SUSE-Linux-Enterprise-15-SP7    SUSE Linux Enterprise 15 SP7
SUSE-Linux-Enterprise-16.0      SUSE Linux Enterprise 16.0
kali-linux                      Kali Linux Rolling
Debian                          Debian GNU/Linux
AlmaLinux-8                     AlmaLinux OS 8
AlmaLinux-9                     AlmaLinux OS 9
AlmaLinux-Kitten-10             AlmaLinux OS Kitten 10
AlmaLinux-10                    AlmaLinux OS 10
archlinux                       Arch Linux
FedoraLinux-43                  Fedora Linux 43
FedoraLinux-42                  Fedora Linux 42
eLxr                            eLxr 12.12.0.0 GNU/Linux
Ubuntu-20.04                    Ubuntu 20.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
OracleLinux_7_9                 Oracle Linux 7.9
OracleLinux_8_10                Oracle Linux 8.10
OracleLinux_9_5                 Oracle Linux 9.5
openSUSE-Leap-15.6              openSUSE Leap 15.6
SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6
```

## 3. Install a Distro

In this guide, we will be installing the latest version of WSL Ubuntu.

We can use the following command (Grab a coffee, this will take some time):

```
wsl --install Ubuntu-22.04
```

One the download finishes, the installation is done.

You can now launch your Ubuntu WSL and start running some linux commands.
