const AWS = require('aws-sdk');
const sqs = new AWS.SQS({ region: 'us-east-1' });

const params = {
  MessageBody: JSON.stringify(transactionData),
  QueueUrl: 'https://sqs.us-east-1.amazonaws.com/123456789012/POS_Transactions'
};

sqs.sendMessage(params, (err, data) => {
  if (err) {
    console.error('Error publishing message:', err);
  } else {
    console.log('Message published:', data.MessageId);
  }
});
