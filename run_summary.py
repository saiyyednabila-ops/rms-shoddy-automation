import smtplib
from email.mime.text import MIMEText
from datetime import datetime


def compile_run_summary(shoddy_tasks, skipped_tasks, exceptions):
    """
    Compiles the run summary from the provided task lists.
    """  
    summary = {}  
    summary['date'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    summary['shoddy_tasks'] = shoddy_tasks
    summary['skipped_tasks'] = skipped_tasks
    summary['exceptions'] = exceptions
    return summary


def send_confirmation_email(summary, recipient):
    """
    Sends the run summary via email to the recipient.
    """  
    subject = 'Run Summary'
    body = f"Run Summary on {summary['date']}:\n\n"  
    for key, value in summary.items():
        body += f"{key.replace('_', ' ').capitalize()}: {value}\n"  
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'no-reply@yourdomain.com'
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.yourdomain.com') as server:
            server.send_message(msg)
        print('Confirmation email sent successfully.')
    except Exception as e:
        print(f'Failed to send email: {e}')  

