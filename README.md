**STK Push with Safaricom Daraja API using FastAPI and Docker**

---

### Overview

This project demonstrates how to implement STK (Sim Toolkit) push functionality using the Safaricom Daraja API, FastAPI, and Docker. STK push allows businesses to initiate payments directly from a customer's mobile wallet, providing a seamless and secure payment experience.

### Prerequisites

Before running the project, ensure that the following environment variables are set:

- **CONSUMER_KEY**: The consumer key provided by Safaricom Daraja API. This key is used for authentication and authorization purposes.

- **CONSUMER_SECRET**: The consumer secret provided by Safaricom Daraja API. It is paired with the consumer key for secure communication with the API.

- **BUSINESSSHORTCODE**: The shortcode associated with your business account on Safaricom Daraja API. This shortcode is used to identify your business during payment transactions.

- **PASSKEY**: The passkey provided by Safaricom Daraja API. It is used to generate encrypted passwords for authentication and validation purposes.

- **MONGODB_URL_REMOTE**: The URL for connecting to the remote MongoDB instance. This URL should include the username, password, hostname, port, and database name.

- **MONGO_INITDB_ROOT_USERNAME**: The username for the root MongoDB user. This username is used for administrative purposes.

- **MONGO_INITDB_ROOT_PASSWORD**: The password for the root MongoDB user. It is used for authentication when accessing the MongoDB instance.

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/mbuthi/daraja-fastapi.git
   ```

2. Navigate to the project directory:

   ```
   cd daraja-fastapi
   ```

3. Build and run the Docker containers:

   ```
   docker-compose -f docker-compose.yml build --no-cache
   ```
   
   ```
   docker-compose -f docker-compose.yml up -d
   ```

4. Access the FastAPI application at `http://localhost:8000` in your web browser.

### Usage

1. Once the FastAPI application is running, you can access the STK push functionality by sending POST requests to the appropriate endpoint.

2. Use the provided API documentation or endpoint URLs to initiate STK push requests.

### Ngrok Setup

- Install Ngrok, an HTTP tunneling tool, from [https://ngrok.com/download](https://ngrok.com/download).

- After starting the FastAPI server locally, use Ngrok to expose the server to the internet:

  ```
  ngrok http 8000
  ```

- Ngrok will provide a temporary public URL. Use this URL to update the `CallBackURL` in the source code:

  ```
  "CallBackURL": "https://<ngrok_url>/v1/callback/"
  ```

  Replace `<ngrok_url>` with the URL provided by Ngrok, and ensure it ends with `/v1/callback/` as this is where Safaricom will send the transaction status data.

### MongoDB Integration

This project utilizes MongoDB for transaction persistence. Ensure that the MongoDB instance is accessible and properly configured with the provided environment variables.

### Notes

- Replace the placeholder values in the environment variables with the actual values provided by Safaricom Daraja API.

- Ensure that the Docker containers are running and accessible before testing the STK push functionality.

- Monitor the logs for any errors or issues encountered during application execution.
- The part to change the callback URL is located in the file _**app/api/v1/endpoints/stk_push.py**_ under the payload dictionary.

### Contribution

The project is available at [https://github.com/mbuthi/daraja-fastapi.git](https://github.com/mbuthi/daraja-fastapi.git). Contributions and feedback are welcome. Feel free to clone the repository, make improvements, and submit pull requests.
