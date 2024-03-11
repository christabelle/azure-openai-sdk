# Azure OpenAI SDK

This repository contains code designed to facilitate experimentation and testing with 0.28 and the 1.x versions of the Python SDK for Azure OpenAI. Alongside the SDK, it also includes examples of REST API HTTP requests, leveraging the [Rest Client extension in Visual Studio Code](vscode:extension/humao.rest-client). 

Azure OpenAI offers powerful tools for natural language processing, machine learning, and AI-driven applications. With this repository, you can explore the capabilities of Azure OpenAI SDKs and interact with RESTful APIs to integrate AI functionality into your projects seamlessly.

## Getting Started

Follow the steps below to set up your environment and start utilizing the features of this repository:

### Prerequisites

- Python (>= 3.8)
- Visual Studio Code

### Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/christabelle/azure-openai-sdk.git
```

2. Navigate to the project directory.

```bash
cd azure-openai-sdk
```

3. Create a virtual environment.

```bash
python3 -m venv <name_of_your_env>
```

4. Activate the virtual environment.

- On Windows:

```bash
<name_of_your_env>\Scripts\activate
```

- On macOS/Linux:

```bash
source <name_of_your_env>/bin/activate
```

5. Install project dependencies from the requirements.txt file.

```bash
pip install -r requirements.txt
```

6. Create a .env file in the root directory of your project to store sensitive information such as the Azure OpenAI resource's keys. You can find a sample .env file in the repository called `sample.env`. Duplicate this file and rename it to `.env`, then fill in the necessary values.

```bash
cp sample.env .env
```
Now, you're ready to use the secrets stored in your `.env` file securely within your project. Feel free to customize the `.env` file with your other specific secrets and configurations as needed.

Note: Never share your `.env` file publicly or commit it to version control systems like Git, as it contains sensitive information. The best practice is to use a `.gitignore` file in your repo to avoid commiting the `.env` file.


## Rest APIs using Rest Client extension
### .vscode Settings

To work with REST APIs, you will be using Visual Studio Code and the Rest Client extension for working with REST APIs, I have already created a `.vscode` folder in the root of this repo. You will have to add a `settings.json` file. There's a `settings-sample.json` which can help you create the `settings.json` file. Here's how you can configure it:

1. Create a `settings.json` file inside the `.vscode` folder.

3. Add the following configuration to `settings.json`:

```json
{
    "rest-client.environmentVariables": {
        "$shared": {
            "openai-baseurl": "http://example.com/api",
            "openai-key": "xxx"
        }
    }
}
```

Replace `"http://example.com/api"` with the base URL of your Azure OpenAI resource, and `"xxx"` with the key of your Azure OpenAI resource.

Now, you're all set to use the Rest Client extension for sending requests to your REST API endpoints directly from Visual Studio Code.

---

Feel free to customize this template to fit your project's specific needs. Dive into the realm of Azure OpenAI and empower your applications with intelligent features! Happy coding!