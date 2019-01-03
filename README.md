# Mass-email-sender

## Configuration

First setup the 'CONFIG' file with email address, password, subject and message.

```text
{
  "email": "your.email@example.com",
  "password": "yourPassword",
  "subject": "Subject of the email comes here",
  "message": "The email body comes here"
}
```

Next add list of receipient email addresses in *mailing_list.txt* file. One email per line.

```text
$ cat mailing_list.txt
destination.email@example.com
second.email@example.com
```

## Running the script

```text
$ python3 mailer.py
```

If there's no error then there's no problem
