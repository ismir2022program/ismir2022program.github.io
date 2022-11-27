import pandas as pd
import argparse

def getIndividualEmails(emailString):
    emails = str(emailString).strip()
    emails = emails.replace("|",",")
    emails = emails.replace(" ","")
    emails = emails.replace(";",",")

    emails = emails.split(",")
    return emails

def parse_arguments():
    parser = argparse.ArgumentParser(description="MiniConf Prep Script")

    parser.add_argument(
        "--path",
        help="Pass the path of directory containing the master data.",
        required=True)

    args = parser.parse_args()
    return args

# Parsing arguments.
args = parse_arguments()
data_path = args.path
    
if(data_path is None):
    raise Exception("--path for the root directory for data is missing")

registrationCsvFile = data_path + "/__23rd_International_Society_for_Music_Information_Retrieval_Conference_(ISMIR_2022)__Registration_Data.csv"
eventsCsvFile = data_path + "/events.csv"
papersCsvFile = data_path + "/papers.csv"
musicCsvFile = data_path + "/music.csv"
lbdCsvFile = data_path + "/lbds.csv"
industryCsvFile = data_path + "/industry.csv"


# Getting all the emails for registrations.
attendee_email_columns = "Attendee Email"
registered_users_csv = pd.read_csv(registrationCsvFile)

attendee_emails = list(map(str.strip, registered_users_csv[attendee_email_columns]))

print("Total number of registered users: ", str(len(attendee_emails)))

# Getting email for the tutorials.
# tutorials_email_column = "organiser_emails"
# tutorials_author_email = pd.read_csv(eventsCsvFile)

# for emails in tutorials_author_email[tutorials_email_column]:
    # if(not pd.isna(emails)):
        # attendee_emails.extend(getIndividualEmails(emails))


# Getting email for music papers.
# sponsors_email_column = "registered_emails"
# sponsors_email = pd.read_csv(industryCsvFile)

# for emails in sponsors_email[sponsors_email_column]:
    # if(not pd.isna(emails)):
        # attendee_emails.extend(getIndividualEmails(emails))

print(attendee_emails)



