# ID Verification by LibraX.ai

[LibraX.ai](https://www.libraX.ai) is an identity verification platform for developers. This solution is to verify user ID image for name matching, age, and basic fraud detection for ID. LibraX is providing to give this service for free as long as we are in business, and you can reach out to hello@librax.ai for any add-on features or customized requirement.

![Example for ID verification](https://www.librax.ai/wp-content/uploads/2021/03/Screen-Shot-2021-03-12-at-11.45.22-AM-e1615567678450.png)


## How to use the API?

1. For ID Verfication use the REST API 
    ```
    https://api.librax.ai/id/verify
    ```

2. Create a json payload for the request having FistName, LastName and base64 encoding of ID on which you wish to run ID Verification on 
    ```
    {
        "FirstName": "first_name",
        "LastName": "last_name",
        "IDPhoto": <base64 encoded string>
    }
    ```
3. Set the `Content-Type` header as application/json

4. Using the subscription key obtained in previous step set the `Ocp-Apim-Subscription-Key` header as follows
    ```
    Ocp-Apim-Subscription-Key: <your-subscription-key>
    ```

5. Send your request to the server, the response will be in json format.
Note: Detailed response status code is documented here [dev.librax.ai](https://dev.librax.ai/api-details#api=ID-Verification-API&operation=post-id-verify)

`Example code` can be found [here](ID-verification-example.py)

## How to get the subscription key?

1. You need register an account in https://dev.librax.ai
2. You will get an confirmation email (it may land into your spam folder).
3. You need login and go to "product" page. You can name your subscription and click the subscrib button there.  
4. you can see your subscription and key token in your profile page. 
