# appservicerm

1.	Install AZ for windows
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest

 


2.	Az login to login to azure
 

3.	Install Azure RM to manage azure resources 
Note:  Be an admin to powershell

 

a.	start-Transcript
b.	Get-ExecutionPolicy
c.	Set-ExecutionPolicy RemoteSigned
d.	Install-Module azureRM
e.	Install-Module azure – AllowClobber

Then you can manage powershell scripts 
4.	Inorder to connect azure rm
Create an  service principal with subscription, tenant (azure ad) id.
For ex:
az ad sp create-for-rbac --name myapp --password PASSWORD

 

5.	Now we can create resource group automation as well as many other resources

Creating new resource group: abc4

 

6.	Check the portal to see its created:

 
7.	For Azure App service:

Connect-AzureRmAccount
Start-AzureRmwebAppSlot  -ResourceGroupName “ azurevmgroup” –Name “ azurevm1” – slot “dev1”
We can create powershell script and execute it and saving as ps1.



