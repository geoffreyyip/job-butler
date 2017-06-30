from string import Template

import csv
import datetime

# loads a template string into memory
def load_template(template):
    with open(template) as f:
        return f.read()

# dumps form letters and job description to file
def write_job_app(filename, paragraphs):
    filepath = 'applications/' + filename
    with open(filepath, 'w') as f:
        for paragraph in paragraphs:
            f.write(paragraph)
            f.write('\n_____________________\n\n')

# todo: default argument to today's date
def make_filename(name, title, location, date=datetime.datetime.now()):
    date_str = date.strftime('%Y.%m.%d')
    return "{} {} {} in {}.txt".format(date_str, name, title, location)

if __name__ == "__main__":
    cover_template = load_template('cover_template.txt')
    email_template = load_template('email_template.txt')

    with open('companies.csv') as f:
        companies = csv.DictReader(f)
        for company in companies:
            cover_letter = Template(cover_template).substitute(company)
            email_letter = Template(email_template).substitute(company)

            job_description = company['JOB_DESCRIPTION']
            filename = make_filename(
                company['COMPANY_NAME'],
                company['JOB_TITLE'],
                company['LOCATION'],
            )

            write_job_app(
                filename,
                [cover_letter, email_letter, job_description],
            )


