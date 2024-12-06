import time.LocalDate;
import time.format.DateTimeFormatter;
import Period;



start_date = input("Enter start date: ")

end_date = input("Enter end date: ")

menstrual_cycle= int(input("Enter your menstrual cycle: "))

		
DateTimeFormatter date = DateTimeFormatter.ofPattern("dd/MM/yyyy")
	
LocalDate periodStartTime = LocalDate.parse(startDate,date)	
LocalDate periodEndTime = LocalDate.parse(endDate,date)
Period period = Period.between(periodStartTime,periodEndTime)

menstrual_period = int(input("Your mensturation duration: " + period))

LocalDate ovulationPeriod = periodEndTime.plusDays(days/2)
ovulation_period = int(input("Your ovulation period start: " + ovulationPeriod))

LocalDate ovulationPeriodEnd = ovulationPeriod.plusDays(2)
ovulation_period_end = 	int(input("Your ovulation period end: " + ovulationPeriodEnd))

LocalDate freePeriod = periodEndTime.plusDays(1)
safe_period = int(input("Your safe period start: " + freePeriod))	

LocalDate endFreePeriod = periodEndTime.plusDays(6)
safe_period_ends = int(input("Your safe period ends: " + endFreePeriod))

LocalDate fertilePeriodstart = ovulationPeriod.minusDays(4)

LocalDate fertilePeriodend = ovulationPeriodEnd.plusDays(2)
	
LocalDate nextPeriodStart = periodEndTime.plusDays(days)
next_period_start = int(input("Your next period start: " + nextPeriodStart))