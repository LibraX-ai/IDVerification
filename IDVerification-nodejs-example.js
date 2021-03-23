const fs = require("fs");
const axios = require("axios");
const imageToBase64 = require("image-to-base64");

const Subscription_Key = "your-subscription-key",
const baseURL = "https://api.librax.ai";

let config = {
  headers: {
    "Ocp-Apim-Subscription-Key": Subscription_Key,
    "Content-Type": "application/json",
  },
};

var image_buff = fs.readFileSync('/Users/hackx/Desktop/TestImage.png', 'base64')


let payload_data = {
    FirstName: "Jane Diane", // First name of user to be verified
    LastName: "Sample", // Last name of user to be verified
    IDPhoto: image_buff,
  };

async function verify(){
    let request = await axios.post(baseURL + "/id/verify", payload_data, config);
    console.log(request.data);
}
  
verify();
