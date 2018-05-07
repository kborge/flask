from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.core.repositories.Status_Code import StatusCode
from app.config.config import BASE_URL


class Email:
    __sender = "validation_team@link365.net"
    __password = "link365777@#$"
    __recipients = None
    __body = None
    __subject = "No Reply"
    __url = BASE_URL

    def __init__(self, recipient, body=__body, subject=__subject):
        self.__recipients = recipient
        self.__body = body
        self.__subject = subject

    def send(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.__sender
            msg['To'] = self.__recipients
            msg['Subject'] = self.__subject
            body = self.__body
            msg.attach(MIMEText(body, 'html'))
            server = SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.__sender, self.__password)
            text = msg.as_string()

            server.sendmail(self.__sender, self.__recipients, text)

            server.quit()
            status = 200
            message = "Email successfully sent to %s" % self.__recipients
        except SMTPAuthenticationError as error:
            status = 500
            message = str(error)

        return {
             "status": status,
             "message": message
        }

    def change_sender(self, sender, password):
        self.__sender = sender
        self.__password = password

    def account_registration_verification(self, code, name):
        try:
            self.__subject = "Account Activation"
            self.__body = 'Hi %s! <br/><br/> Welcome to ' \
                          'Link365 Global Solutions Inc and Connexions. Link365 are committed to providing our ' \
                          'customers with the correct level of security this email has been sent ' \
                          'to your account so that yo can confirm your email address.<br><br> ' \
                          'Please click the below link to confirm your email address, <br><br>' \
                          '%s/company/email/verification/%s <br><br>' \
                          'If you have not registered for connexions please contact validations_' \
                          'team@link365.net<br><br> Thank you,<br>' \
                          'Link365 Connexions Team' % (name, self.__url, code)
            status = StatusCode.ok
            message = "Email sent!"

        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error,
            message = str(error)
        return {
            "status": status,
            "message": message
        }

    def company_account_approval(self, company_name, account_name, company_code):
        try:
            self.__subject = "%s Account Activation Approval" % company_name
            self.__body = "Hi %s! <br/><br/> " \
                          "Thank you for registering your company (%s) with Link365 Global Solutions " \
                          "Connexions product. We are committed to long term " \
                          "excellent customer service and welcome you.<br>" \
                          "Below you will find the information required to Log on to the system, " \
                          "please keep this information safe for future reference." \
                          "If you have any questions you can contact the team by emailing validations_" \
                          "team@link365.net. <br><br>" \
                          "Company Code: %s <br>Email: %s <br><br>Thank you<br>Link365 Connexions Team" \
                          "" % (account_name, company_name, company_code, self.__recipients)
            status = StatusCode.ok
            message = "Email sent!"
        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error
            message = str(error)
        return {
            "status": status,
            "message": message
        }

    def account_forgot_password(self, password):
        try:
            self.__subject = "Forgot Password Notification"
            self.__body = 'Your password has been successfully changed, ' \
                          '<br> Here is your new password: %s <br> ' \
                          '<br/><h3>NOTE: This is a random password, Please change your password ' \
                          'after you login for security purposes.</h3><br/><br/>' \
                          'If you have any questions you can contact the team by ' \
                          'emailing validations_team@link365.net<br/><br/>' \
                          'Thank you,<br>Link365 Connexions Team' % password
            status = StatusCode.ok
            message = "Email sent!"
        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error
            message = str(error)
        return {
            "status": status,
            "message": message
        }

    def account_change_password(self):
        try:
            self.__subject = "Change Password Notification"
            self.__body = 'Your password has been changed, ' \
                          '<br/><br/>If you have any questions you can contact the team by ' \
                          'emailing validations_team@link365.net<br/><br/>' \
                          'Thank you,<br>Link365 Connexions Team'
            status = StatusCode.ok
            message = "Email sent!"
        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error
            message = str(error)
        return {
            "status": status,
            "message": message
        }

    def account_branch_append(self, user_name, branch_name, company_name, category, password=None):
        try:
            branch_category = 'Branch Manager' if category == 'branch-manager' else \
                'Branch Administrator' if category == 'branch-administrator' else 'Branch Agent'
            self.__subject = "Branch Account Notification"
            default_message = 'Hi '+user_name+'!, <br/><br/> You have been added to branch ' \
                              + branch_name + ' in the ' + company_name + \
                              ' Company as a ' + branch_category
            self.__body = (default_message + '<br/><br/><br/>Credentials: <br/><br/>Email: ' + self.__recipients +
                           ' <br/><br/>Your temporary password is <b>' + password + '<b></br><br/>'
                           '<br/>Please change your password after you login.') if password is not None else \
                default_message + '<br/><br/>If you have any questions you can contact the team by ' \
                                  'emailing validations_team@link365.net<br/><br/> ' \
                                  'Thank you,<br>Link365 Connexions Team'
            status = StatusCode.ok
            message = "Email sent!"
        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error
            message = str(error)
        return {
            "status": status,
            "message": message
        }

    def account_branch_revoke(self, user_name, branch_name, company_name, category):
        try:
            branch_category = 'Branch Manager' if category == 'branch-manager' else \
                'Branch Administrator' if category == 'branch-administrator' else 'Branch Agent'
            self.__subject = "Branch Account Notification"
            self.__body = 'Hi %s!, <br/><br/> You have been added to branch %s in the %s Company as a %s ' \
                          '<br/><br/>If you have any questions you can contact the team by ' \
                          'emailing validations_team@link365.net<br/><br/>' \
                          'Thank you,<br>Link365 Connexions Team' % (user_name, branch_name, company_name, branch_category)
            status = StatusCode.ok
            message = "Email sent!"
        except SMTPAuthenticationError as error:
            status = StatusCode.internal_error
            message = str(error)
        return {
            "status": status,
            "message": message
        }

