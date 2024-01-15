employeeName = str(input("Enter Employee's  name: "))

numberOfHoursWorkedWeekly = eval(input("Number of hours worked in a week: "))

hourlyRate = eval(input("Enter hourly rate: "))

federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))

stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))

month = str(input("Enter month: "))

grossPay = numberOfHoursWorkedWeekly * hourlyRate

federalDeductions = (federalTaxWithholdingRate/100) * grossPay

stateDeductions = (stateTaxWithholdingRate/100) * grossPay

totalDeductions = federalDeductions + stateDeductions

netPay = grossPay - totalDeductions

print("==========================================================")
print(f"Divine Mercy Payroll statement for the month of {month}")
print("==========================================================")
print(f"Employee Name: {employeeName}")
print(f"Hours Worked: {numberOfHoursWorkedWeekly}")
print(f"Pay Rate: ${hourlyRate}")
print(f"Gross Pay: ${grossPay}")
print("Deductions:")
print(f"Federal  Withholding({federalTaxWithholdingRate}%): ${federalDeductions}")
print(f"State Withholding({stateTaxWithholdingRate}%): ${stateDeductions}")
print(f"Total Deductions: ${totalDeductions}")
print(f"Net Pay: ${netPay}")
print("==========================================================")


