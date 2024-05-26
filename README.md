# PyGmailCleaner

PyGmailCleaner is a command-line interface (CLI) application designed to help you manage and clean up your Gmail inbox efficiently. It provides simple options to filter emails by

## Features

- **Filter Emails**: Apply various filters to identify emails to be cleaned.
- **Analyze Inbox**: Retrieve general statistics about your inbox, such as the total number of messages and unread messages.
- **Delete Emails**: Optionally delete emails immediately or after confirmation.
- **User-Friendly Prompts**: Interactive prompts guide you through the cleaning process.
- **Logging**: Configurable logging to track the application's actions and any issues that may arise.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- Gmail account
- App password (if using 2-factor authentication)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/PyGmailCleaner.git
   cd PyGmailCleaner
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables** (optional):
   ```bash
   export GMAIL_USER="your-email@gmail.com"
   export GMAIL_PASSWORD="your-password"
   ```

## Usage

Run the application using the following command:
```bash
python pygmailcleaner.py --loglevel debug
```

### Command-Line Arguments

- `--loglevel`: Set the logging level (e.g., `debug`, `info`, `warning`, `error`). Default is `notset`.

### Interactive Prompts

The application will guide you through several prompts to configure the cleaning process:

1. **Email Credentials**: Enter your Gmail address and password if not set via environment variables.
2. **General Statistics**: The application will display the total number of messages and unread messages.
3. **Filter Date**: Specify a date to filter emails up until.
4. **Filter Selection**: Choose the filters to apply for identifying emails to be cleaned.
5. **Delete Immediately**: Choose whether to delete emails immediately or wait for confirmation.
6. **Summary**: Review your choices and confirm to proceed.
7. **Continue Confirmation**: Confirm whether to proceed with the deletion.

### Example Run

```plaintext
____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||P |||Y |||G |||M |||A |||I |||L |||       |||C |||L |||E |||A |||N |||E |||R ||
||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\| 
        
Welcome to the Gmail Cleaner CLI
*******************************
What is your gmail address?: rupertarup@gmail.com
What is your password? (must be an app password if using 2FA): 
Connected to gmail
Total number of messages: 22614
Unread messages: 4714
What date would you like to clean up until? (format 'YYYY-MM-DD'): 2024-03-31
Please select the commands you would like to include:
Only include promotions? [y/n]: y
Only include unread? [y/n]: y
Exclude important? [y/n]: y
Exclude attachments? [y/n]: y
Would you like to delete immediately? [y/n]: y

Summary:
1. Search up until date: 2024-03-31
2. Delete immediately: Yes
3. Included filters:
   - Only include promotions
   - Only include unread
   - Exclude important
   - Exclude attachments
Would you like to continue? [y/n]: y
Moving 259 to Trash
Emptying Trash
Connection closed
Thank you for using the Gmail Cleaner CLI. Goodbye!

```

## Logging

Logs are printed to the console based on the specified log level. Available levels are `debug`, `info`, `warning`, `error`, and `notset`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact [your-email@gmail.com].

Thank you for using PyGmailCleaner!