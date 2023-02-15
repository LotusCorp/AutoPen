<center> <h1 align="center" >AutoPen</h1> </center>

![image](https://user-images.githubusercontent.com/123122904/219063137-ac79b873-913f-4c2f-b16b-6e012d1d46da.png)

<div align="center">

|      Name      |        Type      |     Creation Date     |
|:----------------|:-------------------|:------------------------|
|   AutoPen      |     Auto Scan     |   13th February 2023   |

[Description](#Description) - [Futures](#Futures) - [Installation](#Instalatiin) - [Contribute](#Contribute)

</div>

<center> <h1 id="Description" align="center" >Description</h1> </center>
<div align="center">
Introducing a powerful and sophisticated program that can swiftly scan websites for vulnerabilities and potential security loopholes. This cutting-edge tool is designed to automatically identify open ports, DNS records, subdomain bruteforcing, and directory bruteforcing, all with ease and precision. <br><br>

The program is equipped with a comprehensive suite of features that enable it to perform in-depth scans, including advanced WHOIS and header scanning. With these capabilities, the program can thoroughly examine a website and reveal valuable information about its underlying structure and configuration. <br>

Utilizing state-of-the-art technology and advanced algorithms, this program is capable of conducting scans with speed and accuracy, making it an indispensable tool for security professionals and website owners alike. Whether you're looking to assess your own website's security or identify potential vulnerabilities in a target site, this program is the perfect solution for you. <br>


<center> <h1 id="Futures" align="center" >Futures</h1> </center>
<div align="center">

| Futures              | Implemented               |
|----------------------|:---------------------------:|
| Port Scan            | <ul><li> - [x] </li></ul> |
| Dump DNS Records     | <ul><li> - [x] </li></ul> |
| Dump Active Headers  | <ul><li> - [x] </li></ul> |
| Subdomain Bruteforce | <ul><li> - [x] </li></ul> |
| Directory Bruteforce | <ul><li> - [x] </li></ul> |
| Whois Scan           | <ul><li> - [x] </li></ul> |
| Dig Certificates     | <ul><li> - [ ] </li></ul> |
| Scan for LFI         | <ul><li> - [x] </li></ul> |
| Scan for SQLi        | <ul><li> - [x] </li></ul> |
| Detect Webservice    | <ul><li> - [x] </li></ul> |
| Detect Framework     | <ul><li> - [x] </li></ul> |

</div>

<center> <h1 id="Installation" align="center" >Installation</h1> </center>
<div align="left">

1. Cloning the Repository
  ```
  git clone https://github.com/LotusCorp/AutoPen
  cd AutoPen
  ```
  
2. Installing Modules
  ```
  python -m pip install -r requirements.txt
  ```

3. Running AutoPen
  ```
  python main.py -d domain.com
  ```
  
</div>
<center> <h1 id="Contribute" align="center" >Contribute</h1> </center>

<div align="center">

To ensure your contribution can be effectively integrated as a module in the "main.py" file and executed from there, please ensure that you place the file within the "scanners" directory. Additionally, it is imperative that your file is capable of saving results to a file located within the "scans/SCANTYPE" directory. Please note that the "scans" directory name should be entirely capitalized.

</div>
