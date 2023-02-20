const AWS = require('aws-sdk');
const dynamoDB = new AWS.dynamoDB({region: 'us-east-1', apiVersion: '2012-08-10'});

exports.handler = (event, context, callback) => {
    // TODO implement
    const params = {
        Item: {
            "UserId":{
                S: "user_" + Math.random()
            },
            "Age":{
                N: event.age
            },
            "Height":{
                N: event.age
            },
            "Income":{
                N: event.income
            }
        },
        TableName: "compare-yourself"
    };
    dynamoDB.putItem(params, function(err, data){
        if (err){
            console.log(err);
            callback();
        } else {
            console.log(data);
            callback(null, data);
        }
    });
};
