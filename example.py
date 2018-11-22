import sugarcrm

url = 'url'
user = 'user'
pwd = 'pass'
# Connect
session = sugarcrm.Session(url, user, pwd)

# Get account that we will be update
account = sugarcrm.Account(name='t2')
results_account = session.get_entry_list(account)
# get id account
account_id = results_account[0].id

# Update
account = sugarcrm.Account(id=account_id)
account.description = "New description333" + results_account[0].description
session.set_entry(account)

