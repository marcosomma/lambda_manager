# MANAGING LAMBDA FUNCTIONS AND ALIASES
```
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\[ BLACKWOODSEVEN LAMBDA MANAGING INTERFACE ]\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/_____________________________________________________________________|\/|
        /|\/                                  |                                  |\/|
        /|\/------------[LAMBDA]--------------|--------------[ALIAS]-------------|\/|
        /|\/                                  |                                  |\/|
        /|\/ 1 - Create Lambda                | 4 - Create Alias                 |\/|
        /|\/ 2 - Update Lambda                | 5 - Update Alias                 |\/|
        /|\/ 3 - Delete Lambda                | 6 - Delete Alias                 |\/|
        /|\/                                  |                                  |\/|
        /|\/---------------------------------------------------------------------|\/|
        /|\/ q - Exit  | h - help                                                |\/|
        /|\/_____________________________________________________________________|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|
        Please select an action: 
```
## 1 - Create Lambda
Creates a new Lambda function. The function metadata is created from the request parameters, and the code for the function is provided by a .zip file in the request body. If the function name already exists, the operation will fail. Note that the function name is case-sensitive.

If you are using versioning, you can also publish a version of the Lambda function you are creating using the Publish parameter. For more information about versioning, see AWS Lambda Function Versioning and Aliases .

This operation requires permission for the lambda:CreateFunction action.
[more...](http://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html)
## 2 - Update Lambda
Updates the code for the specified Lambda function. This operation must only be used on an existing Lambda function and cannot be used to update the function configuration.

If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases .

This operation requires permission for the lambda:UpdateFunctionCode action.
[more](http://docs.aws.amazon.com/cli/latest/reference/lambda/update-function-code.html)
## 3 - Delete Lambda
Deletes the specified Lambda function code and configuration.

If you are using the versioning feature and you don't specify a function version in your delete-function request, AWS Lambda will delete the function, including all its versions, and any aliases pointing to the function versions. To delete a specific function version, you must provide the function version via the qualifier parameter. For information about function versioning, see AWS Lambda Function Versioning and Aliases .

When you delete a function the associated resource policy is also deleted. You will need to delete the event source mappings explicitly.

This operation requires permission for the lambda:DeleteFunction action.
[more...](http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-function.html)
## 4 - Create Alias
Creates an alias that points to the specified Lambda function version. For more information, see Introduction to AWS Lambda Aliases .

name names are unique for a given function.

This requires permission for the lambda:CreateAlias action.
[more...](http://docs.aws.amazon.com/cli/latest/reference/lambda/create-alias.html)
## 5 - Update Alias
Using this API you can update the function version to which the alias points and the alias description. For more information, see Introduction to AWS Lambda Aliases .

This requires permission for the lambda:UpdateAlias action.
[more...](http://docs.aws.amazon.com/cli/latest/reference/lambda/update-alias.html)
## 6 - Delete Alias
Deletes the specified Lambda function alias. For more information, see Introduction to AWS Lambda Aliases .

This requires permission for the lambda:DeleteAlias action.
[more...](http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-alias.html)