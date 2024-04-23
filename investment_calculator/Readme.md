usage 'python investment.py lumpsum <total-investment> <intrest-rate> <time-period>
ChatGPT
To use the python investment.py lumpsum <total-investment> <interest-rate> <time-period> command, you would typically replace <total-investment>, <interest-rate>, and <time-period> with the actual values you want to calculate for your investment. Here's an example:

plaintext
Copy code
python investment.py lumpsum 10000 5 3
Save to grepper
In this example:

<total-investment> is 10000 (assuming the currency is dollars).
<interest-rate> is 5 (representing 5% interest rate per annum).
<time-period> is 3 years.
You would replace these placeholders with your specific investment amount, interest rate, and time period to calculate the results.

User
.\.venv\scripts\activate : File
C:\Users\Lakshminaidu\Downloads\pythonfolder_24\investment_calculator\.venv\scripts\Activate.ps1 cannot be loaded
because running scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\.venv\scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
ChatGPT
It looks like you're encountering a security error related to running scripts on your system. This error is because PowerShell script execution is disabled by default on some systems for security reasons. To resolve this issue, you can follow these steps:

Open PowerShell as an administrator.
Set the execution policy to allow script execution. You can do this by running the following command:
plaintext
Copy code
Set-ExecutionPolicy RemoteSigned
Confirm the change by typing "Y" (yes) when prompted.
After making this change, try activating the virtual environment again using the .venv\scripts\activate command. If you still encounter issues, please let me know, and we can troubleshoot further.

User
Set-ExecutionPolicy : Access to the registry key
'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied. To change the execution
policy for the default (LocalMachine) scope, start Windows PowerShell with the "Run as administrator" option. To
change the execution policy for the current user, run "Set-ExecutionPolicy -Scope CurrentUser".
At line:1 char:1
+ Set-ExecutionPolicy unrestricted
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.SetExecutionPolicyComma
   nd
ChatGPT
It seems that you encountered another permission issue while trying to change the execution policy. Here's what you can do to resolve it:

Open PowerShell as an administrator. This step is crucial as it grants you the necessary permissions to make changes to the execution policy.
Run the following command to set the execution policy to unrestricted for the current user:
plaintext
Copy code
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
Confirm the change by typing "Y" (yes) when prompted.
After making these changes, try activating the virtual environment again using the .venv\scripts\activate command. This should resolve the issue with script execution permissions.


================
[refer here](https://docs.python.org/3/library/index.html)
[refer here]()

