<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Aws services deploy using the Chalice Framework</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Chalice Examples][product-screenshot]](https://example.com)

Here's why:
* Chalice will take care of deployment
* We can run api services in local with using the aws credentials
* Using the single config.json we can configure the all services



### Built With

* [Python](https://www.python.org/)
* [Chalice](https://chalice-fei.readthedocs.io/en/latest/)
* [AWS]



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* python
  ```sh
    sudo apt install python3
    source venv/bin/activate
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/venkateshchary/Chalice-lambda-python.git
   ```
3. Install Python  packages
   ```sh
    source venv/bin/activate
    pip3 install chalice
    pip3 install flask
   ```
4. Create chalice app
   ```sh
    chalice new-project hello_aws
    chalice local # to run the dev stage
   ```


4. Add configurations in `config.json`
   ```json
   {"version": "2.0","app_name": "dev_hello","stages": {
   "dev": {
      "api_gateway_stage": "api",
      "manage_iam_role":false,
      "iam_role_arn":"arn:aws:iam::xxxxx:role/user_role",
      "subnet_ids": ["subnet-xxxxx",
        "subnet-xxxxx",
        "subnet-xxxxx"],
      "security_group_ids": ["sg-xxx"],
      "layers": ["arn:aws:lambda:xxxxx:layer:pymysql-py36:1"],
      "lambda_functions": {
        "hello_world": {
          "lambda_timeout": 60
        },
        "processors": {
          "lambda_timeout": 900,
          "lambda_memory_size": 960
        }
      },
      "environment_variables":{
        "bucket_name":"s3_bucket",
        "database":"db_name",
        "username":"username",
        "password":"rds password",
        "host":"rds host url"
      },
      "tags": {
        "owner":"USER",
        "purpose":"engineering",
        "environment":"dev",
      }
      }
    }
    }
    ```



# License

Distributed under the MIT License. See `LICENSE` for more information.


