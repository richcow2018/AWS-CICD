## Use Amazon SQS:

- Decouple the POS system from the ERP system.
- Queue sales transactions for asynchronous processing.
- Use standard queues for high throughput or FIFO queues if ordering is important.

### Create an SQS Queue:
bash
aws sqs create-queue --queue-name POS_Transactions


