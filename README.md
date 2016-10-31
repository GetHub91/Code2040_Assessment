# Code2040_Assessment
Technical assessment for Code2040 application

## Step I: Registration

To get started, you’re first going to connect to the registration endpoint. It lives here:

http://challenge.code2040.org/api/register

The registration endpoint expects a JSON dictionary with two keys, token and github. This JSON should be sent in the body of your HTTP request.

For token, pass in a string with the token you see above. For github, pass in the URL of the repository you created in the last step.

Hint: HTTP has a few types of “methods.” The registration endpoint is going to be expecting you to use POST to send your JSON.


## Step II: Reverse a string

Once you’re registered, it’s time to get started on the challenges.

The first one is straightforward. You’re going to reverse a string.

That is, if the API says “cupcake,” you’re going to send back “ekacpuc.”

POST a JSON dictionary with the key token and your token value to this endpoint:

http://challenge.code2040.org/api/reverse

This endpoint will return a string that your code should then reverse, as in the example above.

Once that string is reversed, send it back to us. POST some JSON to:

http://challenge.code2040.org/api/reverse/validate

Use the token for your token.

Use the key string for your reversed string.

Hint: There’s more than one way to skin a cat. However you reverse the string, all that matters to the API is that it’s flipped around accurately. That said, many libraries can do this work for you with very little code. There’s no shame in doing it the easy way—if you can figure out how.
